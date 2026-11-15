"""Gera a prévia em PDF de um capítulo: Markdown -> HTML -> PDF (Chrome headless).

Uso: python build/build.py manuscript/cap01-principios-cadeia-seguranca.md
Saída: build/out/<nome>.html e build/out/<nome>.pdf
Prévia de rascunho: os selos (PREENCHER [Qn]) ficam destacados em vermelho.
"""
import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build" / "out"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
ALERTAS = {"PERIGO": "perigo", "ATENÇÃO": "atencao", "CUIDADO": "cuidado", "NOTA": "nota"}


def alertas(html: str) -> str:
    """Transforma blockquote cujos parágrafos começam com **PERIGO.** etc. em caixas de alerta (uma por parágrafo)."""
    def caixa(rotulo, resto):
        nome = "Nota" if rotulo == "NOTA" else rotulo.title()
        return f'<div class="alerta {ALERTAS[rotulo]}"><p><span class="rotulo">{nome}</span>{resto}</p></div>'

    def bloco(m):
        interno = m.group(1)
        paras = re.findall(r"<p>(.*?)</p>", interno, re.S)
        casados = [re.match(r"<strong>(PERIGO|ATENÇÃO|CUIDADO|NOTA)\.</strong>(.*)", q, re.S) for q in paras]
        if not paras or not all(casados):
            return m.group(0)
        return "".join(caixa(c.group(1), c.group(2)) for c in casados)

    return re.sub(r"<blockquote>(.*?)</blockquote>", bloco, html, flags=re.S)


def selos(html: str) -> str:
    return re.sub(r"<code>(PREENCHER \[Q\d+\]|\[Certeza\]|\[Provável\]|\[Chute\])</code>", r'<code class="selo">\1</code>', html)


_CONTADOR_SVG = [0]


def isola_estilo(svg_texto: str) -> str:
    """Prefixa os seletores do <style> de cada SVG com o id dele, para que as classes
    (.b, .c, .k...) de uma figura não sobrescrevam as de outra no HTML do livro."""
    _CONTADOR_SVG[0] += 1
    ident = f"fig{_CONTADOR_SVG[0]}"

    def prefixa(m):
        css = m.group(1)
        regras = re.findall(r"([^{}]+)\{([^{}]*)\}", css)
        novo = []
        for seletores, corpo in regras:
            ss = ",".join(f"#{ident} {s.strip()}" for s in seletores.split(",") if s.strip())
            novo.append(f"{ss}{{{corpo}}}")
        return "<style>" + "".join(novo) + "</style>"

    svg_texto = re.sub(r"<style>(.*?)</style>", prefixa, svg_texto, flags=re.S)
    return re.sub(r"<svg ", f'<svg id="{ident}" ', svg_texto, count=1)


def inline_svg(html: str, base: Path) -> str:
    def troca(m):
        svg = (base / m.group(2)).resolve()
        if svg.suffix == ".svg" and svg.exists():
            return f'<figure class="fig">{isola_estilo(svg.read_text(encoding="utf-8"))}</figure>'
        return m.group(0)
    return re.sub(r'<p><img alt="([^"]*)" src="([^"]+)"\s*/?></p>', troca, html)


def main(md_path: str) -> None:
    src = (ROOT / md_path).resolve()
    texto = src.read_text(encoding="utf-8")
    html = markdown.markdown(texto, extensions=["tables", "sane_lists"])
    html = alertas(selos(html))
    html = inline_svg(html, src.parent)
    tokens = (ROOT / "build" / "tokens.css").read_text(encoding="utf-8")
    css = (ROOT / "build" / "print.css").read_text(encoding="utf-8")
    logo = (ROOT / "assets" / "logos" / "logo-color.png").resolve().as_uri()
    pagina = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{src.stem}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{tokens}\n{css}</style></head><body>
<img class="logo" src="{logo}" alt="VerticalParts">
{html}
</body></html>"""
    OUT.mkdir(parents=True, exist_ok=True)
    saida_html = OUT / f"{src.stem}.html"
    saida_pdf = OUT / f"{src.stem}.pdf"
    saida_html.write_text(pagina, encoding="utf-8")
    subprocess.run(
        [str(CHROME), "--headless", "--disable-gpu", "--no-pdf-header-footer",
         "--virtual-time-budget=8000", f"--print-to-pdf={saida_pdf}", saida_html.as_uri()],
        check=True, capture_output=True, timeout=120,
    )
    print(saida_pdf)


if __name__ == "__main__":
    main(sys.argv[1])
