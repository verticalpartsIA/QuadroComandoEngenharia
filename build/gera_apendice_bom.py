"""Gera o Apêndice B (lista de materiais e comparativo das variantes).

Fonte: aba "COMANDO " do Compilado de Materiais (quatro blocos, um por variante),
e a aba "ERP x Materiais" para o resumo da conciliação com o ERP.
Quantidades por quadro, como a planilha traz.

Uso: python build/gera_apendice_bom.py
"""
import re
from collections import OrderedDict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT.parent / "Conhecimento_Claude" / "Excel"
PLANILHA = BASE / "Compilado_Materiais Quadro de comando NICE3000 MRL BST VerticalParts.xlsx"
SAIDA = ROOT / "manuscript" / "ap-b-lista-de-materiais.md"
ORDEM_VAR = ["7,5 kW / 380 V", "15 kW / 380 V", "7,5 kW / 220 V", "15 kW / 220 V"]


def variante(titulo):
    m = re.search(r"([\d,]+)KW/(\d+)V", titulo.upper().replace(" ", ""))
    return f"{m.group(1)} kW / {m.group(2)} V"


def fmt(q):
    if q is None:
        return "-"
    if isinstance(q, float) and q.is_integer():
        q = int(q)
    return str(q).replace(".", ",")


def le_comando(ws):
    dados = OrderedDict()  # codigo -> {"desc":..., "tipo": set, var: qtd}
    atual = None
    for r in ws.iter_rows(values_only=True):
        c1 = r[1]
        if isinstance(c1, str) and c1.upper().startswith("QUADRO DE COMANDO"):
            atual = variante(c1)
            continue
        if not atual or c1 not in ("FIXO", "VARIÁVEL"):
            continue
        cod, desc, qtd = r[3], r[4], r[5]
        if not cod:
            continue
        cod = str(cod).strip()
        d = dados.setdefault(cod, {"desc": str(desc).strip() if desc else "", "tipo": set()})
        d["tipo"].add(c1)
        d[atual] = (d.get(atual) or 0) + (qtd or 0)
    return dados


def le_conciliacao(ws):
    linhas = []
    for r in ws.iter_rows(min_row=4, max_row=9, values_only=True):
        if r[0]:
            linhas.append(r)
    return linhas


def main():
    wb = openpyxl.load_workbook(PLANILHA, data_only=True)
    dados = le_comando(wb["COMANDO "])
    conc = le_conciliacao(wb["ERP x Materiais"])

    comuns, variam = [], []
    for cod, d in dados.items():
        qs = [d.get(v) for v in ORDEM_VAR]
        if all(q is not None for q in qs) and len(set(qs)) == 1:
            comuns.append((cod, d["desc"], qs[0]))
        else:
            variam.append((cod, d["desc"], qs))
    comuns.sort(key=lambda x: x[1].lower())
    variam.sort(key=lambda x: x[1].lower())

    L = [
        "# Apêndice B. Lista de materiais e comparativo das variantes",
        "",
        "> RASCUNHO v0.1 de 15/11/2026. Gerado por `build/gera_apendice_bom.py` a partir do Compilado de Materiais "
        "(`Compilado_Materiais Quadro de comando NICE3000 MRL BST VerticalParts.xlsx`, aba COMANDO). Os códigos são os "
        "códigos internos da VerticalParts (VPMP, VPB, VPEL), incluídos por decisão do responsável técnico em 15/11/2026. "
        "Quantidades **por quadro**. A lista de materiais não é fonte técnica: quando ela diverge do esquema ou do manual, "
        "vale o esquema ou o manual, e a divergência está na seção B.4.",
        "",
        "## B.1 Como ler este apêndice",
        "",
        "1. A planilha traz quatro variantes do quadro: 7,5 kW e 15 kW, em 380 V e em 220 V. O livro descreve a variante "
        "de **7,5 kW em 380 V**; as de 220 V são adendo futuro.",
        "2. B.2 lista os itens com a mesma quantidade nas quatro variantes. B.3 lista os que mudam (ou que não existem em "
        "alguma), com a quantidade de cada variante; \"-\" quer dizer que o item não aparece naquela variante.",
        "3. Fios e canaletas: a planilha não declara a unidade (metro ou peça). O comprimento de cada fio está na lista de "
        "fios (Apêndice A), não aqui.",
        f"4. Total: {len(dados)} códigos distintos, {len(comuns)} comuns às quatro variantes e {len(variam)} que variam.",
        "",
        "## B.2 Itens comuns às quatro variantes",
        "",
        "| Código | Descrição na planilha | Qtd. por quadro |",
        "|---|---|---|",
    ]
    L += [f"| {c} | {d.replace('|', '/')} | {fmt(q)} |" for c, d, q in comuns]
    L += [
        "",
        "## B.3 Itens que mudam por variante",
        "",
        "| Código | Descrição na planilha | " + " | ".join(ORDEM_VAR) + " |",
        "|---|---|" + "---|" * len(ORDEM_VAR),
    ]
    L += [f"| {c} | {d.replace('|', '/')} | " + " | ".join(fmt(q) for q in qs) + " |" for c, d, qs in variam]
    L += [
        "",
        "## B.4 Divergências conhecidas entre a lista de materiais, o esquema e o manual",
        "",
        "| Item | Lista de materiais | Esquema ou manual | O que vale |",
        "|---|---|---|---|",
        "| Disjuntor geral QF | C50 nas variantes de 7,5/380, 15/380 e 7,5/220; C70 na de 15/220 | Manual NICE3000new, Tabela 3-2: 32 A (NICE-L-C-4007), 50 A, 50 A e 80 A (220-NICE-L-C-4022). O esquema desenha o QF de 4 polos, sem corrente | O manual. C70 fica abaixo do recomendado em 15 kW/220 V; C50 fica acima em 7,5 kW/380 V. Etiqueta real: capítulo 3 (selo Q82, dados do QF) |",
        "| Transformador | 220 V para 110 V, 150 VA | Esquema Vitinho, folha /10: 63 VA, primário 220V/0P, secundário 125V/0S | O esquema para os bornes; a etiqueta real decide a potência (pendência P3 do Apêndice C) |",
        "| Disjuntores de comando | DR 2P de 30 mA (três) e minidisjuntores 1P C6 (três) | Esquema, folhas /8 e /10: QFB1 1P+N 10 A curva C; QFB2 2P 6 A curva C; QFB3 e QFB4 DR 2P 6 A 30 mA. O esquema não tem DQFB | O esquema (capítulo 3, seção 3.8) |",
        "| Inversor da variante 7,5 kW/220 V | Código VPB-196 com descrição de potência e tensão conflitantes | Manual NICE3000new, Tabela 1-1: 220-NICE-L-C-4015 | O manual; corrigir o cadastro (pendência P1) |",
        "| Terminal tubular de 6 mm² | 16 no BOM | 19 na lista de fios | Recalcular a compra (pendência P13) |",
        "| Inversor da variante 15 kW/220 V | Código VPB-224 descrito como NICE-L-C-2015-KZG | Manual NICE3000new, Tabela 1-1: 220-NICE-L-C-4022; o modelo \"2015\" não existe no manual | O manual; corrigir o cadastro (pendência P1) |",
        "| Cabo de terra de potência | Variantes de 7,5 kW (380 V e 220 V) trazem cabo verde e amarelo de 6 mm² e de 10 mm² juntos | Manual NICE3000new, Tabelas 2-8 e 3-2: terra de 4 mm² (NICE-L-C-4007), 6, 6 e 10 mm² | Conferir com a lista de fios (Apêndice A), que usa um só cabo de terra de potência |",
        "| Cabo de potência da variante 15 kW/220 V | Cabo preto de 6 mm² (VPMP-263), igual às outras variantes, com terminal tubular de 10 mm² | Manual NICE3000new, Tabela 3-2: 10 mm² para o 220-NICE-L-C-4022 | O manual; a lista precisa do cabo de 10 mm² nessa variante (o ERP 702b tem o VPMP-702, de 10 mm²) |",
        "| Terminal olhal de 6 mm² (VPMP-212) | Quantidade 0 em três variantes e ausente na de 15 kW/220 V | Sem fonte técnica | Confirmar com o PCP se o item sai da lista |",
        "| Resistores de frenagem | 75 Ω/2500 W; 40 Ω/4500 W; 25 Ω/4500 W; 13 Ω/4500 W | Manual NICE3000new, Tabela 3-12: todos dentro da faixa recomendada | Conferem |",
        "| Contatores | CWB25, CWB40, CWB40 e CWB50 | Manual NICE3000new, Tabela 3-2: 25, 38, 38 e 50 A | Compatíveis; sem folha de dados da marca na base |",
        "",
        "Fonte: `auditoria/lote7a_livro_p7_a_p42.md`, linhas 13 a 23; Apêndice C.",
        "",
        "## B.5 Conciliação com as estruturas do ERP",
        "",
        "A planilha compara a lista de fabricação com duas estruturas do ERP (por código de insumo e por quadro). As demais "
        "variantes não foram conciliadas.",
        "",
        "| Estrutura ERP | Variante | Códigos no ERP | Códigos na lista | Em ambos | Só no ERP | Só na lista | Quantidade diferente |",
        "|---|---|---|---|---|---|---|---|",
    ]
    var_erp = {"VPEL-702b": "7,5 kW / 220 V", "VPEL-704b": "15 kW / 380 V"}
    for r in conc:
        if r[0] in var_erp:
            L.append(f"| {r[0]} | {var_erp[r[0]]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    L += [
        "",
        "Exemplos que a planilha aponta como críticos: VPB-196 (potência e tensão conflitantes), VPMP-841 e VPMP-842 "
        "(duas caixas 1), VPMP-702 (cabo de 10 mm² só na 702b), placa leitora de encoder VPB-112 só no ERP e resistores "
        "fora das estruturas. A estrutura da variante de referência (7,5 kW/380 V) não está entre as conciliadas.",
        "",
        "> **NOTA.** Na aba COMANDO, as quatro tabelas usam o total de quadros da primeira (célula E2); os campos E74, E147 "
        "e E218 não alimentam os totais das outras variantes. Isso afeta só a coluna \"QTD TOTAL\" da planilha, que este "
        "apêndice não usa.",
        "",
        "Fonte: Compilado de Materiais, abas COMANDO, Endereçamento e ERP x Materiais.",
        "",
    ]
    SAIDA.write_text("\n".join(L), encoding="utf-8")
    print(f"{len(dados)} códigos; {len(comuns)} comuns; {len(variam)} variam")


if __name__ == "__main__":
    main()
