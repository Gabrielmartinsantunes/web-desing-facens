from __future__ import annotations

from pathlib import Path
import shutil
import re
import mistune

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
EXAMPLES = ROOT / "exemplos"

LESSONS = [
    ("aula-01", "Apresentação da Disciplina", "Organização acadêmica e visão geral"),
    ("aula-02", "Introdução ao Web Design e Git", "Fundamentos e controle de versões"),
    ("aula-03", "Fundamentos do HTML", "Estrutura, semântica e conteúdo"),
    ("aula-04", "Mídias em HTML", "Imagens, áudio, vídeo e formulários"),
    ("aula-05", "SEO com HTML", "Metadados, estrutura e acessibilidade"),
    ("aula-06", "CSS: Fundamentos e Layouts", "Seletores, cores e tipografia"),
    ("aula-07", "Box Model e Flexbox", "Caixas e layouts flexíveis"),
    ("aula-08", "JavaScript: Sintaxe e Estruturas", "Variáveis, lógica e DOM"),
]

MARKDOWN = mistune.create_markdown(plugins=["table", "task_lists", "strikethrough"])

STYLE = r"""/* Apostila acadêmica — identidade visual editorial. */
:root {
  --ink: #22333b;
  --muted: #5e6d72;
  --paper: #fbf8f1;
  --paper-strong: #fffdf8;
  --line: #d9d2c4;
  --blue: #23495b;
  --blue-soft: #e7eef0;
  --gold: #b78a45;
  --gold-soft: #f4ecd9;
  --shadow: 0 14px 36px rgb(35 48 54 / 8%);
  font-family: Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: #e9e5dc;
  line-height: 1.72;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; min-width: 320px; background: #e9e5dc; }
a { color: #20536a; text-decoration-thickness: 1px; text-underline-offset: 3px; }
a:hover { color: #8a5a19; }
a:focus-visible, button:focus-visible, input:focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
.site-header { background: var(--blue); color: #fff; border-bottom: 5px solid var(--gold); }
.header-inner { width: min(1240px, calc(100% - 2rem)); margin: 0 auto; padding: 1.2rem 0 1.35rem; display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; }
.brand { display: flex; align-items: center; gap: .9rem; color: #fff; text-decoration: none; }
.brand-mark { display: grid; place-items: center; width: 48px; height: 48px; border: 1px solid #d7bd8e; border-radius: 50%; color: #f2dba9; font-size: 1rem; letter-spacing: .08em; }
.brand-title { display: block; font-size: 1.12rem; font-weight: 700; letter-spacing: .02em; }
.brand-subtitle { display: block; color: #d4e0e3; font: .75rem/1.4 Arial, sans-serif; letter-spacing: .13em; text-transform: uppercase; }
.header-note { color: #e6e0d4; font: .82rem Arial, sans-serif; text-align: right; }
.layout { width: min(1240px, calc(100% - 2rem)); margin: 1.8rem auto 3rem; display: grid; grid-template-columns: 260px minmax(0, 1fr); gap: 1.4rem; align-items: start; }
.sidebar { position: sticky; top: 1rem; max-height: calc(100vh - 2rem); overflow: auto; padding: 1.2rem; border: 1px solid var(--line); border-radius: 8px; background: var(--paper-strong); box-shadow: var(--shadow); }
.sidebar-heading { margin: 0 0 .85rem; color: var(--blue); font-size: 1.02rem; }
.search-label { display: block; margin-bottom: .35rem; color: var(--muted); font: .72rem Arial, sans-serif; letter-spacing: .08em; text-transform: uppercase; }
#lesson-search { width: 100%; padding: .65rem .7rem; border: 1px solid #c9c1b2; border-radius: 5px; background: #fff; color: var(--ink); font: .88rem Arial, sans-serif; }
.nav-list { margin: 1rem 0 0; padding: 0; list-style: none; }
.nav-list li { border-top: 1px solid #eee8dd; }
.nav-list a { display: block; padding: .56rem .35rem; color: #394e56; text-decoration: none; font: .87rem/1.4 Arial, sans-serif; }
.nav-list a:hover, .nav-list a[aria-current="page"] { color: #8b5e20; background: var(--gold-soft); }
.nav-number { display: inline-block; min-width: 2rem; color: var(--gold); font-weight: 700; }
.sidebar-meta { margin-top: 1.2rem; padding-top: .9rem; border-top: 1px solid var(--line); color: var(--muted); font: .75rem/1.55 Arial, sans-serif; }
.paper { min-width: 0; padding: clamp(1.3rem, 4vw, 3.4rem); border: 1px solid var(--line); border-radius: 8px; background: var(--paper-strong); box-shadow: var(--shadow); }
.eyebrow { margin: 0 0 .55rem; color: #936d32; font: .72rem Arial, sans-serif; letter-spacing: .16em; text-transform: uppercase; }
.page-heading { margin: 0 0 1.5rem; padding-bottom: 1.15rem; border-bottom: 1px solid var(--line); }
.page-heading h1 { margin: 0; color: var(--blue); font-size: clamp(1.9rem, 4vw, 2.75rem); line-height: 1.18; font-weight: 600; }
.page-heading p { margin: .5rem 0 0; color: var(--muted); font: .94rem/1.5 Arial, sans-serif; }
.prose { max-width: 850px; font-size: 1.015rem; }
.prose h1 { color: var(--blue); font-size: 2rem; }
.prose h2 { margin: 2.1rem 0 .7rem; padding-bottom: .35rem; border-bottom: 1px solid #e7e0d4; color: var(--blue); font-size: 1.48rem; line-height: 1.3; }
.prose h3 { margin: 1.45rem 0 .45rem; color: #415b64; font-size: 1.16rem; }
.prose p { margin: .65rem 0 1rem; }
.prose li { margin: .3rem 0; }
.prose blockquote { margin: 1.2rem 0; padding: .8rem 1.15rem; border-left: 4px solid var(--gold); background: #f7f1e5; color: #49585d; }
.prose table { width: 100%; border-collapse: collapse; margin: 1rem 0 1.4rem; font: .9rem/1.5 Arial, sans-serif; }
.prose th, .prose td { padding: .65rem .75rem; border: 1px solid #dcd5c9; text-align: left; vertical-align: top; }
.prose th { background: var(--blue-soft); color: var(--blue); }
.prose code { padding: .1rem .3rem; border-radius: 3px; background: #f1eee7; color: #7a442a; font-family: Consolas, monospace; font-size: .88em; }
.prose pre { overflow: auto; padding: 1rem 1.1rem; border-radius: 6px; background: #263b45; color: #f6f2e9; line-height: 1.5; }
.prose pre code { padding: 0; background: transparent; color: inherit; }
.prose hr { border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }
.prose .callout { margin: 1.4rem 0; padding: 1rem 1.1rem; border: 1px solid #e0cfaa; border-left: 4px solid var(--gold); background: var(--gold-soft); }
.prose .example-link { display: inline-block; margin: .8rem 0 1rem; padding: .65rem .9rem; border: 1px solid var(--blue); border-radius: 4px; background: var(--blue); color: #fff; font: .86rem Arial, sans-serif; text-decoration: none; }
.prose .example-link:hover { background: #173745; }
.page-tools { display: flex; justify-content: flex-end; margin-bottom: .8rem; }
.page-tools button { padding: .5rem .75rem; border: 1px solid #c9c1b2; border-radius: 4px; background: #fff; color: var(--blue); cursor: pointer; font: .82rem Arial, sans-serif; }
.page-nav { display: flex; justify-content: space-between; gap: 1rem; margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--line); font: .88rem Arial, sans-serif; }
.page-nav a { max-width: 48%; text-decoration: none; }
.site-footer { padding: 1.8rem 1rem; background: #203d49; color: #e4e0d6; text-align: center; font: .78rem/1.6 Arial, sans-serif; }
.site-footer a { color: #efd49e; }
.home-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: .9rem; margin: 1.25rem 0; }
.home-card { padding: 1rem; border: 1px solid var(--line); border-top: 3px solid var(--gold); border-radius: 5px; background: #fff; }
.home-card h3 { margin: 0 0 .35rem; color: var(--blue); font-size: 1.1rem; }
.home-card p { margin: 0 0 .6rem; color: var(--muted); font: .86rem/1.55 Arial, sans-serif; }
.home-card a { font: .84rem Arial, sans-serif; }
.empty-search { display: none; color: var(--muted); font: .82rem Arial, sans-serif; }
@media (max-width: 850px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: static; max-height: none; }
  .nav-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0 .8rem; }
  .header-note { display: none; }
}
@media (max-width: 520px) {
  .header-inner { align-items: flex-start; }
  .brand-mark { width: 40px; height: 40px; }
  .paper { padding: 1.1rem; }
  .page-nav { flex-direction: column; }
  .page-nav a { max-width: 100%; }
  .prose table { display: block; overflow-x: auto; }
}
@media print {
  :root, body { background: #fff; }
  .site-header, .sidebar, .page-tools, .page-nav, .site-footer { display: none !important; }
  .layout { display: block; width: 100%; margin: 0; }
  .paper { padding: 0; border: 0; box-shadow: none; }
}
"""

SCRIPT = r"""(() => {
  const search = document.querySelector('#lesson-search');
  const links = [...document.querySelectorAll('.nav-list li')];
  const empty = document.querySelector('.empty-search');

  if (search) {
    search.addEventListener('input', () => {
      const term = search.value.trim().toLocaleLowerCase('pt-BR');
      let visible = 0;
      links.forEach((item) => {
        const match = item.textContent.toLocaleLowerCase('pt-BR').includes(term);
        item.hidden = !match;
        if (match) visible += 1;
      });
      if (empty) empty.style.display = visible === 0 ? 'block' : 'none';
    });
  }

  const printButton = document.querySelector('[data-print-page]');
  if (printButton) printButton.addEventListener('click', () => window.print());
})();
"""


def html_shell(title: str, subtitle: str, content: str, active: str | None, depth: int, prev_next=None) -> str:
    prefix = "../" if depth else ""
    nav_items = [f'<li><a href="{prefix}index.html"{" aria-current=\"page\"" if active == "home" else ""}>Início</a></li>']
    for idx, (slug, name, topic) in enumerate(LESSONS, 1):
        current = ' aria-current="page"' if active == slug else ''
        nav_items.append(
            f'<li><a href="{prefix}aulas/{slug}.html"{current}><span class="nav-number">{idx:02d}</span>{name}</a></li>'
        )
    current = ' aria-current="page"' if active == "project" else ''
    nav_items.append(f'<li><a href="{prefix}projetos/pastelaria-da-sogra.html"{current}>Projeto em grupo: Pastelaria</a></li>')

    prev_html = ""
    if prev_next:
        before, after = prev_next
        prev_link = f'<a href="{before[0]}">← {before[1]}</a>' if before else '<span></span>'
        next_link = f'<a href="{after[0]}">{after[1]} →</a>' if after else '<span></span>'
        prev_html = f'<nav class="page-nav" aria-label="Navegação entre capítulos">{prev_link}{next_link}</nav>'

    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Apostila acadêmica de Web Design da FACENS, organizada por aulas e exemplos práticos.">
  <title>{title} | Apostila Web Design — FACENS</title>
  <link rel="stylesheet" href="{prefix}assets/css/estilo.css">
  <script src="{prefix}assets/js/site.js" defer></script>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{prefix}index.html">
        <span class="brand-mark" aria-hidden="true">WD</span>
        <span><span class="brand-title">Apostila de Web Design</span><span class="brand-subtitle">FACENS · Engenharia da Computação</span></span>
      </a>
      <div class="header-note">Material acadêmico de estudo<br>Conteúdo organizado por aula</div>
    </div>
  </header>
  <div class="layout">
    <aside class="sidebar" aria-label="Navegação da apostila">
      <h2 class="sidebar-heading">Sumário</h2>
      <label class="search-label" for="lesson-search">Localizar conteúdo</label>
      <input id="lesson-search" type="search" placeholder="Buscar uma aula..." autocomplete="off">
      <ul class="nav-list">{''.join(nav_items)}</ul>
      <p class="empty-search">Nenhum item encontrado.</p>
      <div class="sidebar-meta">O número das aulas segue os títulos dos oito PDFs recebidos, não a numeração dos encontros no plano de aprendizagem.</div>
    </aside>
    <main class="paper">
      <div class="page-tools"><button type="button" data-print-page>Imprimir capítulo</button></div>
      <div class="page-heading"><p class="eyebrow">Caderno acadêmico · Web Design</p><h1>{title}</h1><p>{subtitle}</p></div>
      <article class="prose">{content}</article>
      {prev_html}
    </main>
  </div>
  <footer class="site-footer">
    Material independente de estudo baseado nos materiais fornecidos para a disciplina. Não é publicação oficial da FACENS nem substitui orientações do docente ou do Canvas.<br>
    <a href="{prefix}projetos/pastelaria-da-sogra.html">Ver referência do projeto acadêmico em grupo</a>
  </footer>
</body>
</html>'''


def render_markdown(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    # O título principal já aparece no cabeçalho do layout; evita dois h1 na mesma página.
    source = re.sub(r"\A# [^\n]*\n+", "", source, count=1)
    return MARKDOWN(source)


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets/css").mkdir(parents=True, exist_ok=True)
    (SITE / "assets/js").mkdir(parents=True, exist_ok=True)
    (SITE / "aulas").mkdir(parents=True, exist_ok=True)
    (SITE / "projetos").mkdir(parents=True, exist_ok=True)

    (SITE / "assets/css/estilo.css").write_text(STYLE, encoding="utf-8")
    (SITE / "assets/js/site.js").write_text(SCRIPT, encoding="utf-8")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    # Home — acrescenta cartões de acesso sem duplicar a tabela da página-fonte.
    home = render_markdown(DOCS / "index.md")
    cards = '<div class="home-grid">'
    for idx, (slug, name, topic) in enumerate(LESSONS, 1):
        cards += f'<section class="home-card"><h3>Aula {idx:02d} · {name}</h3><p>{topic}</p><a href="aulas/{slug}.html">Estudar esta aula</a></section>'
    cards += '<section class="home-card"><h3>Projeto em grupo</h3><p>Uma referência prática para relacionar os conteúdos ao projeto Pastelaria da Sogra.</p><a href="projetos/pastelaria-da-sogra.html">Consultar a referência</a></section></div>'
    home = home.replace('<h3>Conteúdo</h3>', '<h3>Conteúdo</h3>' + cards)
    home = home.replace('../projetos/pastelaria-da-sogra.html', 'projetos/pastelaria-da-sogra.html')
    (SITE / "index.html").write_text(html_shell("Apostila Acadêmica de Web Design", "FACENS · Engenharia da Computação · Oito aulas organizadas para estudo", home, "home", 0), encoding="utf-8")

    for idx, (slug, name, topic) in enumerate(LESSONS):
        md_path = DOCS / "aulas" / f"{slug}.md"
        content = render_markdown(md_path)
        example = EXAMPLES / slug
        if (example / "index.html").exists():
            example_link = f'<div class="callout"><strong>Arquivos práticos da aula:</strong> <a class="example-link" href="../exemplos/{slug}/index.html">Abrir exemplo resolvido no navegador</a>'
            if (example / "style.css").exists():
                example_link += f' <a href="../exemplos/{slug}/style.css">Ver CSS</a>'
            if (example / "script.js").exists():
                example_link += f' · <a href="../exemplos/{slug}/script.js">Ver JavaScript</a>'
            example_link += '</div>'
        else:
            example_link = '<div class="callout"><strong>Atividade sem código:</strong> esta aula solicita a organização do grupo e o envio dos integrantes no Canvas. O procedimento e um modelo preenchível estão descritos nesta página.</div>'
        # Place the project link after the main title within the markdown body.
        first_end = content.find('</h1>')
        if first_end >= 0:
            content = content[:first_end + 5] + example_link + content[first_end + 5:]
        prev_item = None if idx == 0 else (f"aula-{idx:02d}.html", f"Aula {idx:02d}")
        next_item = None if idx == len(LESSONS) - 1 else (f"aula-{idx+2:02d}.html", f"Aula {idx+2:02d}")
        (SITE / "aulas" / f"{slug}.html").write_text(
            html_shell(f"Aula {idx+1:02d} — {name}", topic, content, slug, 1, (prev_item, next_item)),
            encoding="utf-8",
        )

    project = render_markdown(DOCS / "projetos/pastelaria-da-sogra.md")
    (SITE / "projetos/pastelaria-da-sogra.html").write_text(
        html_shell("Projeto de referência — Pastelaria da Sogra", "Trabalho acadêmico desenvolvido em grupo", project, "project", 1),
        encoding="utf-8",
    )

    # Copia os projetos executáveis sem modificar a estrutura relativa de seus recursos.
    shutil.copytree(EXAMPLES, SITE / "exemplos")
    print(f"Site gerado em: {SITE}")
    print(f"Páginas da apostila: {1 + len(LESSONS) + 1}")


if __name__ == "__main__":
    build()
