"""Monta manuscript/cap13-diagnostico-de-falhas.md a partir da cabeça escrita à mão e dos dois extratos traduzidos.

Origens: manuscript/_cap13-cabeca.md, sources/cap13_falhas_err02_err34.md, sources/cap13_falhas_err35_err69.md
Regras: tira o Err01 (não consta na tabela) e os preâmbulos dos extratos; deixa só os blocos "### ErrNN".
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def blocos(arquivo: str, primeiro: str) -> str:
    txt = (ROOT / "sources" / arquivo).read_text(encoding="utf-8")
    i = txt.index(primeiro)
    return txt[i:].strip()


def main():
    cabeca = (ROOT / "manuscript" / "_cap13-cabeca.md").read_text(encoding="utf-8").strip()
    a = blocos("cap13_falhas_err02_err34.md", "### Err02.")
    b = blocos("cap13_falhas_err35_err69.md", "### Err35.")
    # blocos adicionais do segundo arquivo (ex.: "Outros conteúdos do capítulo 7") vão para o fim
    m = re.search(r"\n## Outros conte", b)
    extra = ""
    if m:
        extra = b[m.start():].strip()
        b = b[: m.start()].strip()
    partes = ("\n" + b).split("\n### ")
    b = "\n### ".join(p for p in partes if p.strip() and "Não consta" not in p.split("\n")[0]).strip()
    b = "### " + b if not b.startswith("###") else b
    corpo = f"{cabeca}\n\n{a}\n\n{b}\n"
    if extra:
        corpo += f"\n{extra}\n"
    corpo += "\n## Fontes do capítulo\n\n- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf` (368 páginas, edição 20181130), capítulo 7, págs. PDF 264 a 289.\n"
    # limpeza de observações redundantes deixadas na tradução
    for velho, novo in (
        (' (texto original: "shorting PMSM stator contactor")', ""),
        (" (Ver o Err35 citado em outros capítulos fora da tabela; não faz parte do escopo.)", ""),
        ("Notas do manual: nenhuma específica.", "Notas do manual: nenhuma."),
    ):
        corpo = corpo.replace(velho, novo)
    (ROOT / "manuscript" / "cap13-diagnostico-de-falhas.md").write_text(corpo, encoding="utf-8")
    print(len(corpo.split()), "palavras;", corpo.count("\n### Err"), "códigos")


if __name__ == "__main__":
    main()
