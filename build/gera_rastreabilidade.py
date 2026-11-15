"""Gera o Apêndice F (rastreabilidade) a partir dos capítulos.

F.1 Documentos-fonte: cada documento da base e os capítulos que o citam.
F.2 Fontes por seção: as linhas "Fonte:" de cada seção, como estão no texto.
F.3 Selos abertos por seção: cada PREENCHER [Qn] com o assunto (tirado do ISSUES.md).

Uso: python build/gera_rastreabilidade.py
"""
import re
from collections import defaultdict, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAN = ROOT / "manuscript"
SAIDA = MAN / "ap-f-rastreabilidade.md"

# (nome no livro, arquivo ou identificação, padrão que reconhece a citação)
DOCUMENTOS = [
    ("Esquema elétrico Vitinho 19061867-ZL (2023-07-18), revisão de esquema válida", "Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf", r"Vitinho|19061867"),
    ("Esquema elétrico VerticalParts 19060918-ZL (2022-10-11), só referência", "Esquema Elétrico Elevadores Verticalparts.pdf", r"19060918|esquema VerticalParts"),
    ("Manual do controlador NICE3000new (368 págs., edição 20181130)", "Manual_Usuario_Controlador_NICE3000new_Completo.pdf", r"[Mm]anual (do )?NICE3000new|Manual_Usuario_Controlador|manual do controlador"),
    ("Manual do resgate elétrico MCTC-ERB-A (19010850-B01)", "Manual_Dispositivo_Resgate_Eletrico_ERB-A1_EN.pdf", r"[Mm]anual (do )?(resgate elétrico|ERB)|Manual_Dispositivo_Resgate|MCTC-ERB-A,"),
    ("Manual da caixa de teto MCTC-CTW-B3 (edição A02, julho de 2022)", "Manual_Caixa_de_Teto_MCTC-CTW-B3_EN.pdf", r"[Mm]anual (da )?(caixa de teto|CTW-B3)|Manual_Caixa_de_Teto"),
    ("Manual do encoder EI53C9.25-2048", "Manual_Encoder_Seno_Cosseno_EI53C9.25-2048.pdf", r"Manual_Encoder|manual do encoder"),
    ("Boletim \"Parametrização de Controlador de Porta NICE900\" (AD30)", "Parametrização do AD30 (Motor Síncrono).pdf", r"[Bb]oletim"),
    ("Manual de comissionamento do NICE900 (versão 1.0, fevereiro de 2026)", "Manual_Comissionamento_NICE900_VerticalParts.pdf", r"manual de comissionamento"),
    ("Manual da máquina de porta J4210 (22/03/2024)", "Manual_Instrucoes_Operador_de_Porta_J4210-T2.pdf", r"[Mm]anual (da máquina )?J4210|J4210, seç"),
    ("POP-ISO-PCP, planejamento, produção e controle de quadros de comando (Rev. 00)", "POP-ISO-PCP ... QUADROS DE COMANDO.pdf", r"POP-ISO-PCP"),
    ("Cartilha \"Manual de Resgate\" VP-RES-01 Rev. 02 (versão para validação técnica)", "VerticalParts_Manual_de_Resgate-2.pdf", r"VP-RES-01|[Cc]artilha"),
    ("Fotos do quadro de 12 e 13/11/2026", "Fotos do quadro", r"[Ff]otos? (do quadro|de 1[23]/11)"),
    ("Livro do Quadro de Comando Rev. 11 e a auditoria dele", "Livro_..._Rev11.pdf; auditoria/", r"Rev\. 11|auditoria"),
]


def capitulos():
    out = []
    for arq in sorted(MAN.glob("cap*.md")):
        m = re.match(r"cap(\d+)", arq.stem)
        out.append((int(m.group(1)), arq.read_text(encoding="utf-8")))
    return out


def secoes(texto):
    """[(numero, titulo, corpo)] das seções ## n.m."""
    partes = re.split(r"^## ", texto, flags=re.M)[1:]
    out = []
    for p in partes:
        titulo, _, corpo = p.partition("\n")
        m = re.match(r"(\d+\.\d+)\s+(.*)", titulo)
        if m:
            out.append((m.group(1), m.group(2).strip(), corpo))
    return out


def assuntos_dos_selos():
    assunto = {}
    for linha in (ROOT / "ISSUES.md").read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in linha.split("|")]
        if len(c) > 3 and re.fullmatch(r"Q\d+|CREA", c[1]):
            assunto[c[1]] = c[2]
    return assunto


def limpa(s):
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("|", "/")
    return s


def main():
    caps = capitulos()
    assunto = assuntos_dos_selos()

    # F.1
    usos = OrderedDict((d[0], set()) for d in DOCUMENTOS)
    for n, txt in caps:
        for nome, _, pad in DOCUMENTOS:
            if re.search(pad, txt):
                usos[nome].add(n)

    # F.2 e F.3
    linhas_f2, linhas_f3 = [], []
    sem_fonte = []
    for n, txt in caps:
        for num, titulo, corpo in secoes(txt):
            if titulo.startswith(("O que você vai aprender", "Teste o que você aprendeu")):
                continue
            fontes = []
            for m in re.finditer(r"^(?:\*\*)?Fonte[s]?(?: \([^)]*\))?:?(?:\*\*)?\s*(.+)$", corpo, flags=re.M):
                f = limpa(m.group(1))
                if f and f not in fontes:
                    fontes.append(f)
            if fontes:
                linhas_f2.append(f"| {num} {limpa(titulo)} | {'; '.join(fontes)} |")
            else:
                sem_fonte.append(f"{num} {limpa(titulo)}")
            selos = sorted(set(re.findall(r"PREENCHER \[(Q\d+)\]", corpo)), key=lambda q: int(q[1:]))
            for q in selos:
                linhas_f3.append(f"| {num} | {q} | {assunto.get(q, 'ver Apêndice C')} |")

    L = [
        "# Apêndice F. Rastreabilidade",
        "",
        "> VERSÃO v0.2 de 15/11/2026. Aprovado pelo Gelson em 15/11/2026. Gerado por `build/gera_rastreabilidade.py` a partir dos capítulos. "
        "Mostra de onde vem cada informação do livro: os documentos da base (F.1), as fontes citadas em cada seção (F.2) "
        "e os dados que ainda faltam (F.3). A regra do livro é: toda afirmação técnica cita documento e página; "
        "o que não tem fonte fica com selo, nunca com suposição.",
        "",
        "## F.1 Documentos-fonte",
        "",
        "| Documento | Arquivo na base de conhecimento | Capítulos que citam |",
        "|---|---|---|",
    ]
    for nome, arquivo, _ in DOCUMENTOS:
        caps_doc = ", ".join(str(c) for c in sorted(usos[nome])) or "nenhum"
        L.append(f"| {nome} | `{arquivo}` | {caps_doc} |")
    L += [
        "",
        "Hierarquia: quando dois documentos divergem, vale o esquema Vitinho 19061867-ZL para ligações e o manual do "
        "fabricante para valores e parâmetros. A lista de fios da produção não é fonte: ela é conferida contra o esquema "
        "(Apêndice A). Documentos de outros fabricantes (BST, Glarie) e edições antigas de manual foram lidos só como apoio "
        "e não são citados como fonte.",
        "",
        "## F.2 Fontes por seção",
        "",
        "Cada linha traz as fontes exatamente como a seção as cita (linhas \"Fonte:\"). As seções sem linha própria usam as "
        "fontes do fim do capítulo.",
        "",
        "| Seção | Fontes citadas |",
        "|---|---|",
    ] + linhas_f2
    L += ["", "**Seções sem linha \"Fonte:\" própria** (citam a fonte dentro do texto ou das tabelas, ou usam as fontes do fim do capítulo): " + "; ".join(sem_fonte) + ".", ""]
    L += [
        "## F.3 Dados que ainda faltam, por seção",
        "",
        "Cada selo `PREENCHER [Qn]` é um dado sem fonte. O livro só é liberado sem nenhum. O assunto vem do controle de "
        "issues do projeto.",
        "",
        "| Seção | Selo | Assunto |",
        "|---|---|---|",
    ] + linhas_f3 + [""]
    SAIDA.write_text("\n".join(L), encoding="utf-8")
    print(f"F.2: {len(linhas_f2)} seções com fonte, {len(sem_fonte)} sem linha própria; F.3: {len(linhas_f3)} selos")


if __name__ == "__main__":
    main()
