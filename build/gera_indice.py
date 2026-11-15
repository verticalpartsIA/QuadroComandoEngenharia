"""Gera o Apêndice E (índice remissivo) a partir do Apêndice D e dos capítulos.

Para cada termo fixo e cada sigla do Apêndice D, procura as seções (## n.m) dos
capítulos em que ele aparece e lista os números das seções. Remete por seção,
não por página, porque o PDF é paginado só na impressão.

Uso: python build/gera_indice.py
"""
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAN = ROOT / "manuscript"
SAIDA = MAN / "ap-e-indice-remissivo.md"
IGNORA_SECOES = ("Fontes do capítulo", "Teste o que você aprendeu", "O que você vai aprender")
# Siglas que aparecem em quase toda citação de fonte e não ajudam a achar assunto
FORA_DO_INDICE = {"PDF", "ZL"}
PALAVRAS_LIGACAO = {"e", "a", "de", "do", "da", "MCTC", "Err", "E"}


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def secoes_dos_capitulos():
    """Devolve [(numero_secao, texto)] de todos os capítulos."""
    out = []
    for arq in sorted(MAN.glob("cap*.md")):
        atual, buf = None, []
        for linha in arq.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^## (\d+\.\d+)\s+(.*)", linha)
            if m or linha.startswith("## Fontes"):
                if atual:
                    out.append((atual, "\n".join(buf)))
                atual, buf = None, []
                if m and not any(m.group(2).startswith(x) for x in IGNORA_SECOES):
                    atual = m.group(1)
                continue
            if atual:
                buf.append(linha)
        if atual:
            out.append((atual, "\n".join(buf)))
    return out


def verbetes_do_apendice_d():
    """Lê as tabelas do Apêndice D. Devolve [(rotulo, [padrões])]."""
    texto = (MAN / "ap-d-glossario-e-siglas.md").read_text(encoding="utf-8")
    parte = re.split(r"^## D\.3", texto, flags=re.M)[0]
    itens = []
    em_termos = False
    for linha in parte.splitlines():
        if linha.startswith("## D.1"):
            em_termos = True
        elif linha.startswith("## D.2"):
            em_termos = False
        if not linha.startswith("| ") or linha.startswith("| Termo") or linha.startswith("| Sigla"):
            continue
        rotulo = linha.split("|")[1].strip()
        if not rotulo or rotulo.startswith("---"):
            continue
        if em_termos:
            pads = [re.compile(r"\b" + re.escape(rotulo) + r"s?\b", re.I)]
        else:
            base = re.sub(r"\(.*?\)", " ", rotulo)
            toks = [t for t in re.split(r"[ ,;/]+", base) if t and t not in PALAVRAS_LIGACAO]
            # "QFB1 a QFB4", "KY2 a KY12", "PT1 a PT4": expande a faixa
            m = re.match(r"([A-Z]+)(\d+) a [A-Z]*?(\d+)", base.strip())
            if m:
                toks = [f"{m.group(1)}{n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)]
            if rotulo in FORA_DO_INDICE:
                continue
            pads = []
            for t in toks:
                if len(t) < 2 or t.isdigit():
                    continue
                # F3 é o fusível; "F3-08" é parâmetro do grupo F3
                fim = r"(?![A-Za-z0-9-])" if t == "F3" else r"(?![A-Za-z0-9])"
                pads.append(re.compile(r"(?<![A-Za-z0-9])(?<!V )" + re.escape(t) + fim))
        if pads:
            itens.append((rotulo, pads))
    return itens


def chave_secao(s):
    a, b = s.split(".")
    return (int(a), int(b))


def main():
    secoes = secoes_dos_capitulos()
    entradas = []
    for rotulo, pads in verbetes_do_apendice_d():
        achados = sorted({n for n, txt in secoes if any(p.search(txt) for p in pads)}, key=chave_secao)
        if achados:
            entradas.append((rotulo, achados))
    entradas.sort(key=lambda e: sem_acento(e[0]).lower())

    grupos = defaultdict(list)
    for rotulo, achados in entradas:
        ini = sem_acento(rotulo)[0].upper()
        grupos[ini if ini.isalpha() else "#"].append((rotulo, achados))

    linhas = [
        "# Apêndice E. Índice remissivo",
        "",
        "> VERSÃO v0.2 de 15/11/2026. Aprovado pelo Gelson em 15/11/2026. Gerado por `build/gera_indice.py` a partir dos termos e siglas do Apêndice D. "
        "Os números são **seções** (por exemplo, 3.6 é a seção 6 do capítulo 3), e não páginas, para que o índice "
        "continue certo quando a paginação mudar. As seções \"O que você vai aprender\", \"Teste o que você aprendeu\" "
        "e as listas de fontes não entram.",
        "",
    ]
    for ini in sorted(grupos):
        linhas.append(f"### {'Símbolos e números' if ini == '#' else ini}")
        linhas.append("")
        for rotulo, achados in grupos[ini]:
            linhas.append(f"- **{rotulo}**: {', '.join(achados)}")
        linhas.append("")
    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    print(f"{len(entradas)} verbetes gravados em {SAIDA.name}")


if __name__ == "__main__":
    main()
