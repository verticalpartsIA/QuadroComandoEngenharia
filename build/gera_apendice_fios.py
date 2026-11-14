"""Gera o Apêndice A (lista de fios conferida contra o esquema) em Markdown.

Fontes:
- Lista de fios original: Conhecimento_Claude/ArquivosParaTratar/Lista de fios.xlsx
- Resultado da conferência: auditoria/lote2_kcb.md, lote3_contatores_resgate.md, lote4_potencia_terra.md
  (tabelas fio a fio) e o lote 1 (feito à mão, fios abaixo), mais correções do lote 6 (fios 90 e 120).
Saída: manuscript/ap-a-lista-de-fios.md
A lista NÃO é a base do livro; o apêndice mostra a lista e o que o esquema confirma de cada fio.
"""
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = Path(r"C:\dev\SitesProjetos\Conhecimento_Claude\ArquivosParaTratar\Lista de fios.xlsx")
AUD = ROOT / "auditoria"

# Lote 1 (conferido diretamente nas folhas /14 e /22 do Vitinho)
LOTE1 = {6, 7, 8, 9, 10, 11, 12, 13, 17, 38, 39, 40, 41, 42, 43, 49, 50, 95, 96, 110, 111}
# Lote 6 (esquema VerticalParts confirma): fios 90 e 120 deixam de ser "não verificável"
LOTE6 = {90: "XB 202 aparece nos dois esquemas (Vitinho /22; VerticalParts pág. 15)", 120: "XB 202 aparece nos dois esquemas (Vitinho /22; VerticalParts pág. 15)"}


def le_lotes():
    res = {}
    for nome in ("lote2_kcb.md", "lote3_contatores_resgate.md", "lote4_potencia_terra.md"):
        for linha in (AUD / nome).read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*(\d{1,3})\s*\|(.*)\|\s*$", linha)
            if not m:
                continue
            cols = [c.strip() for c in m.group(2).split("|")]
            # colunas: ligação, evidência, resultado, confiança, observação
            if len(cols) < 5:
                continue
            resultado = cols[2].upper()
            if resultado not in ("CONFERE", "DIVERGE", "NÃO VERIFICÁVEL"):
                continue
            res[int(m.group(1))] = (resultado, cols[3], cols[4], cols[1])
    return res


def main():
    res = le_lotes()
    for n in LOTE1:
        res[n] = ("CONFERE", "alta/média", "", "Vitinho /14 e /22")
    for n, obs in LOTE6.items():
        res[n] = ("CONFERE", "média", obs, "Vitinho /22 e VerticalParts pág. 15")
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    ws = wb.active
    linhas = []
    n = 0
    for r in ws.iter_rows(min_row=4, values_only=True):
        if not (r[2] or r[5]):
            continue
        n += 1
        tag = r[1] or ""
        orig = f"{r[2]} {r[3]}"
        dest = f"{r[5]} {r[6]}"
        cor, bit, cm = r[8], r[9], r[10]
        if n in res:
            resultado, conf, obs, evid = res[n]
        else:
            resultado, conf, obs, evid = ("NÃO VERIFICÁVEL", "", "fora dos lotes conferidos", "")
        linhas.append((n, tag, orig, dest, cor, bit, cm, resultado, conf, obs, evid))

    conta = {"CONFERE": 0, "DIVERGE": 0, "NÃO VERIFICÁVEL": 0}
    for l in linhas:
        conta[l[7]] += 1

    out = []
    out.append("# Apêndice A. Lista de fios conferida contra o esquema\n")
    out.append("> RASCUNHO v0.1 de 14/11/2026.\n")
    out.append(
        "Esta lista vem do arquivo `Lista de fios.xlsx` da produção (125 ligações internas do quadro de comando). "
        "Ela não é a base do livro: cada ligação foi conferida contra o esquema Vitinho 19061867-ZL, que é a revisão de esquema "
        "válida para produção (decisão do Gelson em 14/11/2026). A coluna \"Esquema\" diz o que o desenho mostra.\n"
    )
    out.append(
        f"Resultado: **{conta['CONFERE']} conferem**, **{conta['DIVERGE']} divergem** e **{conta['NÃO VERIFICÁVEL']} não são verificáveis** "
        "(terras que o esquema só mostra como símbolo, e componentes que o esquema não desenha). "
        "Divergência não quer dizer erro de fiação: em vários casos é só diferença de numeração entre o desenho e a peça física.\n"
    )
    out.append(
        "Legenda das cores de fio da lista: PT = preto, AZ = azul, VD+AM = verde e amarelo. A bitola vem da lista; nenhum esquema lido indica bitola.\n"
    )
    out.append("| # | Rede | Origem | Destino | Cor | mm² | cm | Esquema | Confiança | Observação |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for (n, tag, orig, dest, cor, bit, cm, resultado, conf, obs, evid) in linhas:
        obs = obs.replace("|", "/").replace("Ver seção 4.", "Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela.")
        bit = str(bit).replace(".", ",")
        out.append(f"| {n} | {tag} | {orig} | {dest} | {cor} | {bit} | {cm} | {resultado.title() if resultado != 'NÃO VERIFICÁVEL' else 'Não verificável'} | {conf} | {obs} |")
    out.append("")
    out.append("> **PERIGO.** Os fios 62 a 66 (jumpers) não existem no esquema Vitinho nem no esquema VerticalParts. Pelas redes do desenho, o fio 64 liga o início da cadeia de segurança (rede 110) ao fim dela (rede 130, entrada X25), e os fios 65 e 66 fazem o mesmo com as fechaduras das portas. Instalados num quadro de campo, eles anulam essas proteções. O responsável técnico indicou que são jumpers só de bancada, sem confirmação em campo. Remova-os antes de ligar os cabos de campo. Os fios 61 e 67 são diferentes: o esquema os prevê para elevador de porta única.\n")
    out.append("> **NOTA.** Nos fios 29, 32, 36, 37 e 105 a 109 o SZ aparece numerado em pares (1-2, 3-4, 13-14, 23-24 e 33-34). Segundo o responsável técnico, é assim que o quadro real implementa a tomada de 9 pinos do esquema, com bornes pequenos em pares. A divergência desses fios é de numeração, e a rede e o pino da KCB conferem. O mapa entre os pares e os pinos da tomada ainda precisa de confirmação visual no quadro.\n")
    out.append("Fonte: `Lista de fios.xlsx` (produção); conferência contra o esquema Vitinho 19061867-ZL, lotes 1 a 6 da auditoria (arquivos em `auditoria/`).\n")
    (ROOT / "manuscript" / "ap-a-lista-de-fios.md").write_text("\n".join(out), encoding="utf-8")
    print(conta, len(linhas))


if __name__ == "__main__":
    main()
