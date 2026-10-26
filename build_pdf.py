#!/usr/bin/env python3
"""
Build a single PDF from the Syhunt documentation in this repository.

The pages are taken in the order they are linked from README.md, grouped
under README's "##" sections. Internal links between pages become links
inside the PDF, images are embedded from images/, and the PDF gets a cover,
a table of contents with page numbers, bookmarks and running headers.

The PDF is written one level above the repository root (../), so it never
ends up inside the repository itself.

Requirements (Python 3.8+):
    pip install markdown-it-py pygments weasyprint

WeasyPrint also needs the Pango libraries:
    - Debian/Ubuntu: sudo apt install libpango-1.0-0 libpangoft2-1.0-0
    - macOS:         brew install pango
    - Windows:       see https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

If WeasyPrint is not available, the script falls back to Playwright/Chromium
(pip install playwright && playwright install chromium); in that case the
table of contents has no page numbers.

Usage:
    python3 build_pdf.py                 # uses VERSION below
    python3 build_pdf.py --version 7.3   # override the version
    python3 build_pdf.py --html          # also keep the intermediate HTML
"""

import argparse
import datetime
import html
import os
import re
import sys
import unicodedata

# --------------------------------------------------------------------------
# Settings
# --------------------------------------------------------------------------

VERSION = "7.2"
PRODUCT = "Syhunt Hybrid"

ROOT = os.path.dirname(os.path.abspath(__file__))       # repository root
OUT_DIR = os.path.abspath(os.path.join(ROOT, ".."))       # one level down
README = os.path.join(ROOT, "README.md")

STRINGS = {
    "en": {
        "title": "Documentation",
        "subtitle": "User and Integration Guide",
        "version": "Version",
        "generated": "Generated on",
        "contents": "Contents",
        "page": "Page",
        "of": "of",
        "alerts": {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important",
                   "WARNING": "Warning", "CAUTION": "Caution"},
        "filename": "Syhunt-Hybrid-{version}-Documentation-EN.pdf",
    },
    "pt": {
        "title": "Documentação",
        "subtitle": "Guia do Usuário e de Integração",
        "version": "Versão",
        "generated": "Gerado em",
        "contents": "Sumário",
        "page": "Página",
        "of": "de",
        "alerts": {"NOTE": "Observação", "TIP": "Dica", "IMPORTANT": "Importante",
                   "WARNING": "Atenção", "CAUTION": "Cuidado"},
        "filename": "Syhunt-Hybrid-{version}-Documentacao-PT.pdf",
    },
}


# --------------------------------------------------------------------------
# README parsing
# --------------------------------------------------------------------------

def detect_language(readme_text):
    first = readme_text.strip().splitlines()[0].lower() if readme_text.strip() else ""
    return "pt" if ("documentação" in first or "documentacao" in first) else "en"


def read_structure(readme_text):
    """Return [(part_title, [relative .md paths])] in README order."""
    parts, seen = [], set()
    current = None
    link_re = re.compile(r"\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")
    for line in readme_text.splitlines():
        h2 = re.match(r"^##\s+(.+?)\s*$", line)
        if h2:
            current = (h2.group(1), [])
            parts.append(current)
            continue
        for target in link_re.findall(line):
            if re.match(r"^[a-z]+://", target):
                continue
            path = os.path.normpath(target).replace("\\", "/")
            if path in seen or path.lower() == "readme.md" or path.startswith("images/"):
                continue
            if not os.path.isfile(os.path.join(ROOT, path)):
                print("warning: README links to a missing file: " + path, file=sys.stderr)
                continue
            if current is None:
                continue          # links in the intro are repeated below
            seen.add(path)
            current[1].append(path)
    return [p for p in parts if p[1]]


def intro_html(readme_text, md):
    """README text before the first '##', minus the H1, shown on the cover."""
    body = readme_text.split("\n## ", 1)[0]
    body = re.sub(r"^#\s+.*\n", "", body, count=1)
    body = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", body)   # drop links
    return md.render(body.strip())


# --------------------------------------------------------------------------
# Markdown -> HTML
# --------------------------------------------------------------------------

def make_renderer():
    from markdown_it import MarkdownIt
    try:
        from pygments import highlight
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import get_lexer_by_name
        from pygments.util import ClassNotFound

        def hl(code, lang, _attrs):
            if not lang:
                return ""
            alias = {"bat": "batch", "ps": "powershell", "yml": "yaml"}.get(lang, lang)
            try:
                lexer = get_lexer_by_name(alias)
            except ClassNotFound:
                return ""
            return highlight(code, lexer, HtmlFormatter(nowrap=True))
    except ImportError:
        hl = None

    md = MarkdownIt("commonmark", {"html": True, "highlight": hl})
    md.enable(["table", "strikethrough"])
    return md


def github_slug(text):
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).strip().lower()
    text = "".join(c for c in text if c.isalnum() or c in " -_" or unicodedata.category(c).startswith("M"))
    return text.replace(" ", "-")


def doc_id(path):
    return re.sub(r"[^a-z0-9]+", "-", path.lower().rsplit(".md", 1)[0]).strip("-")


def convert_alerts(body, labels):
    """GitHub '> [!NOTE]' blocks -> styled boxes."""
    def repl(m):
        kind = m.group(1).upper()
        title = labels.get(kind, kind.title())
        return ('<blockquote class="alert alert-%s"><p><strong class="alert-title">%s</strong><br>'
                % (kind.lower(), title))
    return re.sub(r"<blockquote>\s*<p>\[!(\w+)\]\s*(?:<br\s*/?>)?\s*", repl, body)


def render_doc(path, md, docs, labels):
    did = doc_id(path)
    base = os.path.dirname(path)
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        text = f.read()
    body = md.render(text)

    # add GitHub-style ids to headings
    def add_id(m):
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        return '<h%s%s id="%s">%s</h%s>' % (level, attrs, github_slug(inner), inner, level)
    body = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", add_id, body, flags=re.S)

    body = convert_alerts(body, labels)

    # namespace ids so they are unique across the whole PDF
    body = re.sub(r'\bid="([^"]+)"', lambda m: 'id="%s--%s"' % (did, m.group(1)), body)

    # rewrite links
    def link(m):
        href = html.unescape(m.group(1))
        if re.match(r"^(https?|mailto|ftp):", href):
            return m.group(0)
        target, _, anchor = href.partition("#")
        if not target:
            return 'href="#%s--%s"' % (did, anchor)
        tpath = os.path.normpath(os.path.join(base, target)).replace("\\", "/")
        if tpath in docs:
            tid = doc_id(tpath)
            return 'href="#%s"' % ("%s--%s" % (tid, anchor) if anchor else tid)
        if tpath.lower() == "readme.md":
            return 'href="#toc"'
        # a folder or any other file in the repo: keep it as plain text
        return 'href="#%s"' % did
    body = re.sub(r'href="([^"]*)"', link, body)

    # images -> absolute file URIs
    def img(m):
        src = html.unescape(m.group(1))
        if re.match(r"^(https?|data|file):", src):
            return m.group(0)
        p = os.path.normpath(os.path.join(ROOT, base, src))
        return 'src="%s"' % ("file://" + p.replace("\\", "/") if os.name != "nt" else "file:///" + p.replace("\\", "/"))
    body = re.sub(r'src="([^"]*)"', img, body)

    # the page's H1 becomes the document title (one per document)
    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.S)
    title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else path
    body = re.sub(r"<h1([^>]*)>", r'<h1 class="doc-title"\1>', body, count=1)
    return did, title, body


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------

CSS = r"""
@page {
  size: A4;
  margin: 22mm 18mm 20mm 18mm;
  @top-left   { content: string(doctitle); font-size: 8pt; color: #6b7280; }
  @top-right  { content: "%(product)s %(version)s"; font-size: 8pt; color: #6b7280; }
  @bottom-right { content: "%(page)s " counter(page) " %(of)s " counter(pages); font-size: 8pt; color: #6b7280; }
}
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-right { content: none } }
@page toc   { @top-left { content: none } }

html { font-family: "Inter", "Segoe UI", "Helvetica Neue", Arial, "Liberation Sans", sans-serif; font-size: 10pt; color: #1f2328; line-height: 1.5; }
body { margin: 0; }

/* cover */
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 60mm 22mm 25mm;
         background: #0f172a; color: #f8fafc; position: relative; break-after: page; }
.cover .brand { font-size: 12pt; letter-spacing: .25em; text-transform: uppercase; color: #ef4444; font-weight: 700; }
.cover h1 { font-size: 34pt; line-height: 1.15; margin: 8mm 0 4mm; color: #fff; border: 0; bookmark-level: none; }
.cover .sub { font-size: 15pt; color: #cbd5e1; }
.cover .ver { display: inline-block; margin-top: 12mm; padding: 2mm 5mm; border: 1.5pt solid #ef4444; border-radius: 2mm; font-size: 13pt; font-weight: 700; }
.cover .intro { margin-top: 18mm; max-width: 140mm; color: #cbd5e1; font-size: 10.5pt; }
.cover .intro a { color: #cbd5e1; }
.cover .foot { position: absolute; bottom: 20mm; left: 22mm; font-size: 9pt; color: #94a3b8; }

/* table of contents */
.toc { page: toc; break-after: page; }
.toc h1 { font-size: 22pt; border: 0; margin-top: 0; bookmark-level: 1; }
.toc .part { font-weight: 700; font-size: 11pt; margin: 5mm 0 1.5mm; color: #b91c1c; text-transform: uppercase; letter-spacing: .05em; }
.toc ul { list-style: none; margin: 0; padding: 0; }
.toc li { margin: 1mm 0; }
.toc a { color: #1f2328; text-decoration: none; }
.toc a::after { content: leader('.') target-counter(attr(href), page); color: #6b7280; }

/* parts and documents */
.part-title { break-before: page; font-size: 26pt; color: #b91c1c; margin: 70mm 0 0; border: 0;
              bookmark-level: 1; padding-bottom: 3mm; border-bottom: 2pt solid #b91c1c; }
.doc { break-before: page; }
h1.doc-title { string-set: doctitle content(); bookmark-level: 2; font-size: 20pt; border-bottom: 1pt solid #d0d7de; padding-bottom: 2mm; margin-top: 0; }
h1, h2, h3, h4, h5, h6 { line-height: 1.25; break-after: avoid; color: #111827; }
h2 { font-size: 14.5pt; margin-top: 7mm; bookmark-level: 3; border-bottom: .5pt solid #e5e7eb; padding-bottom: 1mm; }
h3 { font-size: 12pt; margin-top: 5mm; bookmark-level: none; }
h4, h5, h6 { font-size: 10.5pt; bookmark-level: none; }

p, li { orphans: 3; widows: 3; }
a { color: #0969da; text-decoration: none; }
img { max-width: 100%%; height: auto; }
li img, p img { vertical-align: middle; }
img[src*="icon_"] { width: 14mm; }
img[src*="micon_"] { width: 6mm; }

code { font-family: "JetBrains Mono", "DejaVu Sans Mono", Consolas, "Liberation Mono", monospace; font-size: 8.6pt;
       background: #f3f4f6; padding: .2mm 1mm; border-radius: 1mm; }
pre { background: #f6f8fa; border: .5pt solid #d0d7de; border-radius: 1.5mm; padding: 3mm; font-size: 8.4pt;
      white-space: pre-wrap; word-wrap: break-word; line-height: 1.4; }
pre code { background: none; padding: 0; font-size: inherit; }

table { border-collapse: collapse; width: 100%%; margin: 3mm 0; font-size: 8.8pt; }
th, td { border: .5pt solid #d0d7de; padding: 1.5mm 2mm; vertical-align: top; text-align: left; }
th { background: #f3f4f6; }
tr { break-inside: avoid; }
td code, th code { word-break: break-all; }

blockquote { margin: 3mm 0; padding: 1mm 4mm; border-left: 2.5pt solid #d0d7de; color: #4b5563; }
blockquote.alert { color: #1f2328; border-radius: 1mm; padding: 2mm 4mm; break-inside: avoid; }
.alert-title { display: inline-block; margin-bottom: .5mm; }
.alert-note      { border-left-color: #0969da; background: #f0f6ff; } .alert-note .alert-title { color: #0969da; }
.alert-tip       { border-left-color: #1a7f37; background: #f0fff4; } .alert-tip .alert-title { color: #1a7f37; }
.alert-important { border-left-color: #8250df; background: #f7f2ff; } .alert-important .alert-title { color: #8250df; }
.alert-warning   { border-left-color: #9a6700; background: #fff8e5; } .alert-warning .alert-title { color: #9a6700; }
.alert-caution   { border-left-color: #cf222e; background: #fff0f0; } .alert-caution .alert-title { color: #cf222e; }
hr { border: 0; border-top: .5pt solid #d0d7de; }
"""


def pygments_css():
    try:
        from pygments.formatters import HtmlFormatter
        return HtmlFormatter(style="friendly").get_style_defs("pre code")
    except ImportError:
        return ""


def build_html(version, lang, s, md, readme_text, structure):
    docs = {p for _, paths in structure for p in paths}
    parts_html, toc_html = [], []
    for pi, (part, paths) in enumerate(structure):
        part_id = "part-%d" % (pi + 1)
        if part:
            parts_html.append('<h1 class="part-title" id="%s">%s</h1>' % (part_id, html.escape(part)))
            toc_html.append('<div class="part">%s</div>' % html.escape(part))
        toc_html.append("<ul>")
        for path in paths:
            did, title, body = render_doc(path, md, docs, s["alerts"])
            parts_html.append('<section class="doc" id="%s">%s</section>' % (did, body))
            toc_html.append('<li><a href="#%s">%s</a></li>' % (did, html.escape(title)))
        toc_html.append("</ul>")

    readme_title = re.sub(r"^#\s*", "", readme_text.strip().splitlines()[0]).strip()
    today = datetime.date.today().isoformat()
    cover = (
        '<section class="cover">'
        '<div class="brand">Syhunt</div>'
        '<h1>%s</h1>'
        '<div class="sub">%s</div>'
        '<div class="ver">%s %s</div>'
        '<div class="intro">%s</div>'
        '<div class="foot">%s %s · www.syhunt.com</div>'
        "</section>"
    ) % (html.escape(readme_title or "%s %s" % (PRODUCT, s["title"])), html.escape(s["subtitle"]),
         html.escape(s["version"]), html.escape(version), intro_html(readme_text, md),
         html.escape(s["generated"]), today)

    toc = '<section class="toc" id="toc"><h1>%s</h1>%s</section>' % (html.escape(s["contents"]), "".join(toc_html))
    css = CSS % {"product": PRODUCT, "version": version, "page": s["page"], "of": s["of"]}
    return (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8">'
        "<title>%s %s %s</title><style>%s\n%s</style></head><body>%s%s%s</body></html>"
    ) % ("pt-BR" if lang == "pt" else "en", PRODUCT, version, s["title"], css, pygments_css(),
         cover, toc, "\n".join(parts_html))


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def render_pdf(html_text, out_path, version, s):
    try:
        from weasyprint import HTML
    except (ImportError, OSError) as e:
        print("WeasyPrint not available (%s); trying Playwright/Chromium." % e, file=sys.stderr)
        return render_with_chromium(html_text, out_path, version, s)
    HTML(string=html_text, base_url=ROOT).write_pdf(out_path)
    return True


def render_with_chromium(html_text, out_path, version, s):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Neither WeasyPrint nor Playwright is installed. Run: pip install weasyprint")
    import tempfile
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=ROOT, encoding="utf-8")
    tmp.write(html_text)
    tmp.close()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("file://" + tmp.name.replace("\\", "/"))
            page.pdf(path=out_path, format="A4", print_background=True, outline=True,
                     display_header_footer=True,
                     header_template='<div style="font-size:8px;width:100%%;text-align:right;padding-right:18mm;color:#6b7280">%s %s</div>' % (PRODUCT, version),
                     footer_template='<div style="font-size:8px;width:100%%;text-align:right;padding-right:18mm;color:#6b7280">%s <span class="pageNumber"></span> %s <span class="totalPages"></span></div>' % (s["page"], s["of"]),
                     margin={"top": "22mm", "bottom": "20mm", "left": "18mm", "right": "18mm"})
            browser.close()
    finally:
        os.unlink(tmp.name)
    return True


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Build the Syhunt documentation PDF.")
    ap.add_argument("--version", default=VERSION, help="product version shown in the PDF (default: %s)" % VERSION)
    ap.add_argument("--html", action="store_true", help="also save the intermediate HTML next to the PDF")
    args = ap.parse_args()

    with open(README, encoding="utf-8") as f:
        readme_text = f.read()
    lang = detect_language(readme_text)
    s = STRINGS[lang]
    structure = read_structure(readme_text)
    count = sum(len(p) for _, p in structure)
    print("%d documents in %d sections (language: %s, version: %s)" % (count, len(structure), lang, args.version))

    md = make_renderer()
    html_text = build_html(args.version, lang, s, md, readme_text, structure)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, s["filename"].format(version=args.version))
    if args.html:
        with open(out_path[:-4] + ".html", "w", encoding="utf-8") as f:
            f.write(html_text)
    render_pdf(html_text, out_path, args.version, s)
    print("PDF written to " + out_path)


if __name__ == "__main__":
    main()
