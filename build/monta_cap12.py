"""Monta manuscript/cap12-energizacao-parametros-autoajuste.md a partir da cabeça e dos extratos traduzidos.

Origens: manuscript/_cap12-cabeca.md, sources/cap12_manual_5-1_a_5-4.md, sources/cap12_manual_cap4_5-5_5-6.md,
         sources/cap12_esquema_parametros_e_ajuste.md (se existir) e manuscript/_cap12-cauda.md (se existir).
Renumera os títulos do manual para 12.x e troca "Figura 5-N" (fluxograma do manual) por "Fluxograma do manual (figura 5-N)".
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# mapa de números de seção do manual para o livro
MAPA = [
    (r"^5\.1\b", "12.2"), (r"^5\.2\b", "12.3"), (r"^5\.3\b", "12.4"), (r"^5\.4\b", "12.5"),
    (r"^5\.5\b", "12.6"), (r"^5\.6\b", "12.7"),
    (r"^4\.1\b", "12.1.1"), (r"^4\.2\b", "12.1.2"), (r"^4\.3\b", "12.1.3"),
]


def renumera(titulo: str) -> str:
    m = re.match(r"^(\d+(?:\.\d+)*)(\s.*)?$", titulo)
    if not m:
        return titulo
    num, resto = m.group(1), m.group(2) or ""
    for padrao, novo in MAPA:
        if re.match(padrao, num):
            return re.sub(padrao, novo, num, count=1) + resto
    return titulo


def ajusta(texto: str, demote: int = 0, manter: str | None = None) -> str:
    saida = []
    for linha in texto.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*)$", linha)
        if m:
            nivel = len(m.group(1)) + (0 if (manter and re.match(manter, m.group(2))) else demote)
            nivel = min(6, nivel)
            linha = "#" * nivel + " " + renumera(m.group(2))
        linha = re.sub(r"\*\*Figura (5-\d+):", r"**Fluxograma do manual (figura \1):", linha)
        linha = linha.replace("seção 7.4", "capítulo 13")
        for velho, novo in (
            ("comissionamento da caixa de corrida", "comissionamento da placa de chamada dos pavimentos (HCB)"),
            ("HCB (caixa de corrida)", "HCB (placa de chamada dos pavimentos)"),
            ("estado de resgate elétrico", "estado de operação elétrica de emergência"),
            ("no resgate elétrico", "na operação elétrica de emergência"),
            ("Velocidade do resgate elétrico", "Velocidade da operação elétrica de emergência"),
            ("velocidade do resgate elétrico", "velocidade da operação elétrica de emergência"),
            ('"emergency electric RUN" (resgate elétrico)', '"emergency electric RUN" (operação elétrica de emergência)'),
            ("primeiro resgate elétrico (emergency electric RUN)", "primeira operação elétrica de emergência (emergency electric RUN)"),
            ('(ordem das caixas conforme o padrão das Figuras 5-5 e 5-9; ver nota em "Lacunas e dúvidas")', "(a ordem das caixas segue o padrão das figuras 5-5 e 5-9 e não foi conferida na imagem do manual; confira no original antes de usar)"),
            ("(mesma ressalva de ordem)", "(a mesma ressalva: ordem das caixas não conferida na imagem do manual)"),
        ):
            linha = linha.replace(velho, novo)
        saida.append(linha)
    return "\n".join(saida)


def entre(texto: str, inicio: str, fim: str | None) -> str:
    i = texto.index(inicio)
    j = texto.index(fim, i + 1) if fim else len(texto)
    return texto[i:j].strip()


def main():
    cabeca = (ROOT / "manuscript" / "_cap12-cabeca.md").read_text(encoding="utf-8").strip()
    a = (ROOT / "sources" / "cap12_manual_5-1_a_5-4.md").read_text(encoding="utf-8")
    b = (ROOT / "sources" / "cap12_manual_cap4_5-5_5-6.md").read_text(encoding="utf-8")

    corpo_a = entre(a, "## 5.1 ", "## Lacunas")
    # capítulo 4, 5.5 e 5.6 do segundo arquivo (a cauda "# Lacunas" fica de fora)
    marca = chr(10) + "# Lacunas"
    fim_b = b.index(marca) if marca in b else len(b)
    b = b[:fim_b]
    cap4 = entre(b, "## 4.1 ", chr(10) + "# 5.5 ")
    s55 = entre(b, "# 5.5 ", chr(10) + "# 5.6 ")
    s56 = b[b.index("# 5.6 "):].strip()

    partes = [cabeca]
    partes.append("## 12.1 Ferramentas de comissionamento" + chr(10) + chr(10) + ajusta(cap4, demote=1))
    partes.append(ajusta(corpo_a, demote=0))
    partes.append(ajusta(s55, demote=1))
    partes.append(ajusta(s56, demote=1))

    esq = ROOT / "sources" / "cap12_esquema_parametros_e_ajuste.md"
    cauda = ROOT / "manuscript" / "_cap12-cauda.md"
    if esq.exists():
        e = esq.read_text(encoding="utf-8")
        lista = entre(e, "## 1. Lista de parâmetros da folha /5", "## 2. Instruções")
        lista = re.sub(r"^## 1\. .*$", "### 12.8.1 Lista de parâmetros da folha /5", lista, count=1, flags=re.M)
        lista = re.sub(r"^### 1\.\d+ (.*)$", r"#### \1", lista, flags=re.M)
        instr = entre(e, "## 2. Instruções", "## 3. ")
        instr = re.sub(r"^## 2\. .*$", '### 12.8.2 Instruções de ajuste da folha /6 ("Tuning instruction")', instr, count=1, flags=re.M)
        dados = entre(e, "### 4.1 ", "### 4.2 ")
        dados = re.sub(r"^### 4\.1 .*$", "### 12.8.3 Dados que o esquema deixa para o projeto", dados, count=1, flags=re.M)
        diverg = entre(e, "### 4.2 ", "### 4.3 ")
        diverg = re.sub(r"^### 4\.2 .*$", "### 12.8.4 Divergências entre o esquema e o manual (conferidas, não corrigidas)", diverg, count=1, flags=re.M)
        intro = (
            "## 12.8 Parâmetros do projeto (esquema Vitinho)\n\n"
            "O esquema traz a lista de parâmetros do projeto na folha /5 e as instruções de ajuste na folha /6. "
            "Cada parâmetro abaixo foi confrontado com o manual NICE3000new (nome, faixa, padrão e página PDF). "
            "Onde o desenho diz \"Model dependent\" ou \"Based on actual conditions\", o valor depende do motor e do projeto e não é dado aqui. "
            "A tabela completa de todos os parâmetros do manual (F0 a FE, Fb, Fr e FP) fica em apêndice próprio. "
            "Fonte: esquema Vitinho 19061867-ZL, folhas /5 e /6 (págs. PDF 7 e 8); manual NICE3000new, págs. PDF 159 a 215."
        )
        partes.append(intro + "\n\n" + lista + "\n\n" + instr + "\n\n" + dados + "\n\n" + diverg)
    if cauda.exists():
        partes.append(cauda.read_text(encoding="utf-8").strip())

    texto = "\n\n".join(partes) + "\n"
    texto += "\n## Fontes do capítulo\n\n- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf` (368 páginas, edição 20181130), capítulo 4 e seções 5.1 a 5.6, págs. PDF 134 a 177.\n- Esquema Vitinho 19061867-ZL, folhas /5 e /6 (págs. PDF 7 e 8).\n"
    (ROOT / "manuscript" / "cap12-energizacao-parametros-autoajuste.md").write_text(texto, encoding="utf-8")
    print(len(texto.split()), "palavras;", texto.count("\n## "), "seções de nível 2;", "esquema extraído:", esq.exists())


if __name__ == "__main__":
    main()
