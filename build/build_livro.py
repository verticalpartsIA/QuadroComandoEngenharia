"""Monta o PDF do livro (Rev. 12 base) a partir de vários arquivos Markdown.

Uso: python build/build_livro.py
Saída: build/out/Livro_Quadro_de_Comando_NICE3000_VerticalParts_Rev12_base_v0-1.html e .pdf
"""
import re
import subprocess
import sys
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, OUT, CHROME, alertas, inline_svg  # noqa: E402

NOME = "Livro_Quadro_de_Comando_NICE3000_VerticalParts_Rev12_base_v0-1"
ORDEM = [
    ("capa", "manuscript/00-frente.md"),
    ("cap", "manuscript/cap01-principios-cadeia-seguranca.md"),
    ("cap", "manuscript/cap02-visao-geral-sistema.md"),
    ("cap", "manuscript/cap03-componentes-do-quadro.md"),
    ("cap", "manuscript/cap04-montagem-e-pre-energizacao.md"),
    ("cap", "manuscript/cap05-testes-de-bancada-e-relatorio-de-cq.md"),
    ("cap", "manuscript/cap07-motor-freio-encoder.md"),
    ("cap", "manuscript/cap08-caixa-de-teto-e-cabina.md"),
    ("cap", "manuscript/cap09-operador-de-porta.md"),
    ("cap", "manuscript/cap10-caixa-de-corrida-e-cabos.md"),
    ("cap", "manuscript/cap11-poco.md"),
    ("cap", "manuscript/cap12-energizacao-parametros-autoajuste.md"),
    ("cap", "manuscript/cap13-diagnostico-de-falhas.md"),
    ("cap", "manuscript/cap14-resgate-eletrico-e-manutencao.md"),
    ("ap", "manuscript/ap-a-lista-de-fios.md"),
    ("ap", "manuscript/ap-c-pendencias-e-correcoes.md"),
]
SELOS = r"<code>(PREENCHER \[Q\d+\]|PENDENTE-REGISTRO|\[Certeza\]|\[Provável\]|\[Chute\])</code>"


def selos(html):
    return re.sub(SELOS, r'<code class="selo">\1</code>', html)


def slug(txt, n):
    base = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", txt).lower()).strip("-")
    return f"s{n}-{base[:40]}"


def main():
    secoes, toc, n = [], [], 0
    for tipo, caminho in ORDEM:
        src = (ROOT / caminho).resolve()
        html = markdown.markdown(src.read_text(encoding="utf-8"), extensions=["tables", "sane_lists"])
        html = alertas(selos(html))
        html = inline_svg(html, src.parent)

        def com_id(m):
            nonlocal n
            n += 1
            nivel, texto = m.group(1), m.group(2)
            ident = slug(texto, n)
            if tipo != "capa" or nivel == "2":
                toc.append((nivel, re.sub(r"<[^>]+>", "", texto), ident))
            return f'<h{nivel} id="{ident}">{texto}</h{nivel}>'

        html = re.sub(r"<h([12])>(.*?)</h\1>", com_id, html)
        secoes.append(f'<section class="{tipo}">{html}</section>')

    itens = "".join(
        f'<li class="n{nv}"><a href="#{i}">{t}</a></li>' for nv, t, i in toc if nv == "1" or True
    )
    sumario = f'<section class="sumario"><h1>Sumário</h1><ul>{itens}</ul></section>'
    corpo = secoes[0] + sumario + "".join(secoes[1:])

    tokens = (ROOT / "build" / "tokens.css").read_text(encoding="utf-8")
    css = (ROOT / "build" / "print.css").read_text(encoding="utf-8")
    logo = (ROOT / "assets" / "logos" / "logo-color.png").resolve().as_uri()
    pagina = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{NOME}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{tokens}\n{css}</style></head><body>
<img class="logo" src="{logo}" alt="VerticalParts">
{corpo}
</body></html>"""
    OUT.mkdir(parents=True, exist_ok=True)
    h = OUT / f"{NOME}.html"
    pdf = OUT / f"{NOME}.pdf"
    h.write_text(pagina, encoding="utf-8")
    import time
    inicio = time.time()

    def imprime(destino):
        subprocess.run(
            [str(CHROME), "--headless", "--disable-gpu", "--no-pdf-header-footer", "--generate-pdf-document-outline",
             "--virtual-time-budget=8000", f"--print-to-pdf={destino}", h.as_uri()],
            check=True, capture_output=True, timeout=180,
        )

    imprime(pdf)
    if not pdf.exists() or pdf.stat().st_mtime < inicio:
        # o arquivo costuma estar aberto em um leitor de PDF (Windows trava a gravação): grava com outro nome
        pdf = OUT / f"{NOME}_atualizado.pdf"
        imprime(pdf)
        print("AVISO: o PDF anterior estava em uso; gerado com outro nome.")
    print(pdf)


if __name__ == "__main__":
    main()
