from __future__ import annotations

from html import escape
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

import mistune


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
EXAMPLES = ROOT / "exemplos"
BUILD_DIR = ROOT / ".site-build-tmp"

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

MARKDOWN = mistune.create_markdown(
    plugins=["table", "task_lists", "strikethrough"]
)

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
  'use strict';

  const search = document.querySelector('#lesson-search');
  const items = [...document.querySelectorAll('.nav-list li')];
  const emptyMessage = document.querySelector('.empty-search');

  if (search) {
    search.addEventListener('input', () => {
      const term = search.value.trim().toLocaleLowerCase('pt-BR');
      let visibleCount = 0;

      items.forEach((item) => {
        const matches = item.textContent.toLocaleLowerCase('pt-BR').includes(term);
        item.hidden = !matches;
        if (matches) visibleCount += 1;
      });

      if (emptyMessage) {
        emptyMessage.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    });
  }

  const printButton = document.querySelector('[data-print-page]');
  if (printButton) {
    printButton.addEventListener('click', () => window.print());
  }
})();
"""


def validate_project() -> None:
    """Confere os arquivos obrigatórios antes de iniciar a geração."""
    required_files = [
        DOCS / "index.md",
        DOCS / "projetos" / "pastelaria-da-sogra.md",
        ROOT / "requirements.txt",
    ]
    required_files.extend(DOCS / "aulas" / f"{slug}.md" for slug, _, _ in LESSONS)

    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.is_file()]
    if missing:
        formatted = "\n - ".join(missing)
        raise FileNotFoundError(
            "Não foi possível gerar a apostila. Arquivos obrigatórios ausentes:\n - "
            + formatted
        )

    if not EXAMPLES.is_dir():
        raise FileNotFoundError(
            "A pasta 'exemplos/' não foi encontrada. Ela é necessária para copiar os projetos de aula."
        )


def render_markdown(path: Path) -> str:
    """Converte um arquivo Markdown em HTML e remove seu H1 duplicado."""
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"\A# [^\n]*\n+", "", source, count=1)
    return MARKDOWN(source)


def build_navigation(prefix: str, active: str | None) -> str:
    """Monta o menu lateral sem expressões complexas dentro de f-strings."""
    home_current = ' aria-current="page"' if active == "home" else ""
    nav_items = [
        f'<li><a href="{prefix}index.html"{home_current}>Início</a></li>'
    ]

    for number, (slug, name, _) in enumerate(LESSONS, start=1):
        current = ' aria-current="page"' if active == slug else ""
        safe_name = escape(name)
        nav_items.append(
            f'<li><a href="{prefix}aulas/{slug}.html"{current}>'
            f'<span class="nav-number">{number:02d}</span>{safe_name}</a></li>'
        )

    project_current = ' aria-current="page"' if active == "project" else ""
    nav_items.append(
        f'<li><a href="{prefix}projetos/pastelaria-da-sogra.html"{project_current}>'
        "Projeto em grupo: Pastelaria</a></li>"
    )
    return "\n".join(nav_items)


def build_page_navigation(prev_next: tuple | None) -> str:
    if prev_next is None:
        return ""

    before, after = prev_next
    # Os arquivos de aula ficam todos no mesmo diretório (site/aulas/).
    # Portanto, os links de navegação usam apenas o nome do arquivo; não
    # devem receber o prefixo ../ utilizado pelo menu lateral.
    if before:
        prev_link = (
            f'<a href="{before[0]}">'
            f'← {escape(before[1])}</a>'
        )
    else:
        prev_link = "<span></span>"

    if after:
        next_link = (
            f'<a href="{after[0]}">'
            f'{escape(after[1])} →</a>'
        )
    else:
        next_link = "<span></span>"

    return (
        '<nav class="page-nav" aria-label="Navegação entre capítulos">'
        f"{prev_link}{next_link}</nav>"
    )


def html_shell(
    title: str,
    subtitle: str,
    content: str,
    active: str | None,
    depth: int,
    prev_next: tuple | None = None,
) -> str:
    """Aplica o layout editorial comum às páginas da apostila."""
    prefix = "../" if depth else ""
    safe_title = escape(title)
    safe_subtitle = escape(subtitle)
    navigation = build_navigation(prefix, active)
    page_navigation = build_page_navigation(prev_next)

    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Apostila acadêmica de Web Design da FACENS, organizada por aulas e exemplos práticos.">
  <title>{safe_title} | Apostila Web Design — FACENS</title>
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
      <ul class="nav-list">{navigation}</ul>
      <p class="empty-search">Nenhum item encontrado.</p>
      <div class="sidebar-meta">O número das aulas segue os títulos dos oito PDFs recebidos, não a numeração dos encontros no plano de aprendizagem.</div>
    </aside>
    <main class="paper" id="conteudo">
      <div class="page-tools"><button type="button" data-print-page>Imprimir capítulo</button></div>
      <div class="page-heading"><p class="eyebrow">Caderno acadêmico · Web Design</p><h1>{safe_title}</h1><p>{safe_subtitle}</p></div>
      <article class="prose">{content}</article>
      {page_navigation}
    </main>
  </div>
  <footer class="site-footer">
    Material independente de estudo baseado nos materiais fornecidos para a disciplina. Não é publicação oficial da FACENS nem substitui orientações do docente ou do Canvas.<br>
    <a href="{prefix}projetos/pastelaria-da-sogra.html">Ver referência do projeto acadêmico em grupo</a>
  </footer>
</body>
</html>'''


def build_home(site_root: Path) -> None:
    home_content = render_markdown(DOCS / "index.md")
    cards = ['<div class="home-grid" aria-label="Acesso às aulas">']

    for number, (slug, name, topic) in enumerate(LESSONS, start=1):
        cards.append(
            '<section class="home-card">'
            f'<h3>Aula {number:02d} · {escape(name)}</h3>'
            f'<p>{escape(topic)}</p>'
            f'<a href="aulas/{slug}.html">Estudar esta aula</a>'
            '</section>'
        )

    cards.append(
        '<section class="home-card">'
        '<h3>Projeto em grupo</h3>'
        '<p>Uma referência prática para relacionar os conteúdos ao projeto Pastelaria da Sogra.</p>'
        '<a href="projetos/pastelaria-da-sogra.html">Consultar a referência</a>'
        '</section>'
    )
    cards.append("</div>")
    cards_html = "".join(cards)

    # Insere os cartões logo após o título Conteúdo. Se o título for alterado,
    # adiciona os cartões ao final em vez de simplesmente descartá-los.
    heading_pattern = re.compile(r"(<h3>\s*Conteúdo\s*</h3>)", flags=re.IGNORECASE)
    if heading_pattern.search(home_content):
        home_content = heading_pattern.sub(
            lambda match: match.group(1) + cards_html,
            home_content,
            count=1,
        )
    else:
        home_content += cards_html

    # O Markdown da página inicial usa um caminho relativo ao diretório docs/.
    home_content = home_content.replace(
        "../projetos/pastelaria-da-sogra.html",
        "projetos/pastelaria-da-sogra.html",
    )

    page = html_shell(
        "Apostila Acadêmica de Web Design",
        "FACENS · Engenharia da Computação · Oito aulas organizadas para estudo",
        home_content,
        "home",
        0,
    )
    (site_root / "index.html").write_text(page, encoding="utf-8")


def build_lessons(site_root: Path) -> None:
    lessons_dir = site_root / "aulas"
    lessons_dir.mkdir(parents=True, exist_ok=True)

    for index, (slug, name, topic) in enumerate(LESSONS):
        markdown_path = DOCS / "aulas" / f"{slug}.md"
        content = render_markdown(markdown_path)
        example_dir = EXAMPLES / slug
        example_index = example_dir / "index.html"

        if example_index.is_file():
            example_link = (
                '<div class="callout"><strong>Arquivos práticos da aula:</strong> '
                f'<a class="example-link" href="../exemplos/{slug}/index.html">'
                "Abrir exemplo resolvido no navegador</a>"
            )
            if (example_dir / "style.css").is_file():
                example_link += (
                    f' <a href="../exemplos/{slug}/style.css">Ver CSS</a>'
                )
            if (example_dir / "script.js").is_file():
                example_link += (
                    f' · <a href="../exemplos/{slug}/script.js">Ver JavaScript</a>'
                )
            example_link += "</div>"
            # O H1 do Markdown é removido porque o layout já fornece o título.
            # Por isso, o bloco de exemplo deve ser inserido no início do artigo.
            content = example_link + content
        elif slug == "aula-01":
            # A atividade desta aula é administrativa e não requer código.
            pass
        else:
            content = (
                '<div class="callout"><strong>Exemplo ainda não disponível:</strong> '
                "os arquivos práticos desta aula não foram encontrados na pasta exemplos.</div>"
                + content
            )

        previous = None if index == 0 else (
            f"aula-{index:02d}.html",
            f"Aula {index:02d}",
        )
        following = None if index == len(LESSONS) - 1 else (
            f"aula-{index + 2:02d}.html",
            f"Aula {index + 2:02d}",
        )

        page = html_shell(
            f"Aula {index + 1:02d} — {name}",
            topic,
            content,
            slug,
            1,
            (previous, following),
        )
        (lessons_dir / f"{slug}.html").write_text(page, encoding="utf-8")


def build_project_page(site_root: Path) -> None:
    project_content = render_markdown(
        DOCS / "projetos" / "pastelaria-da-sogra.md"
    )
    page = html_shell(
        "Projeto de referência — Pastelaria da Sogra",
        "Trabalho acadêmico desenvolvido em grupo",
        project_content,
        "project",
        1,
    )
    project_dir = site_root / "projetos"
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "pastelaria-da-sogra.html").write_text(
        page,
        encoding="utf-8",
    )


def validate_generated_site(site_root: Path) -> None:
    """Executa verificações simples nas páginas geradas antes de publicar."""
    expected_pages = [
        site_root / "index.html",
        *[site_root / "aulas" / f"{slug}.html" for slug, _, _ in LESSONS],
        site_root / "projetos" / "pastelaria-da-sogra.html",
    ]
    missing = [str(path.relative_to(site_root)) for path in expected_pages if not path.is_file()]
    if missing:
        raise RuntimeError(
            "A geração terminou sem produzir todas as páginas esperadas: "
            + ", ".join(missing)
        )

    for page_path in expected_pages:
        page_text = page_path.read_text(encoding="utf-8")
        if "<!doctype html>" not in page_text.lower():
            raise RuntimeError(f"Doctype ausente em {page_path.relative_to(site_root)}")
        if '<html lang="pt-BR">' not in page_text:
            raise RuntimeError(f"Idioma do documento ausente em {page_path.relative_to(site_root)}")
        if "assets/css/estilo.css" not in page_text:
            raise RuntimeError(f"CSS principal não referenciado em {page_path.relative_to(site_root)}")

    if not (site_root / ".nojekyll").exists():
        raise RuntimeError("O arquivo .nojekyll não foi criado.")


def build() -> None:
    """Gera a apostila em uma pasta temporária e substitui o site apenas ao final."""
    validate_project()

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    (BUILD_DIR / "assets" / "css").mkdir(parents=True, exist_ok=True)
    (BUILD_DIR / "assets" / "js").mkdir(parents=True, exist_ok=True)
    (BUILD_DIR / "aulas").mkdir(parents=True, exist_ok=True)
    (BUILD_DIR / "projetos").mkdir(parents=True, exist_ok=True)

    (BUILD_DIR / "assets" / "css" / "estilo.css").write_text(
        STYLE,
        encoding="utf-8",
    )
    (BUILD_DIR / "assets" / "js" / "site.js").write_text(
        SCRIPT,
        encoding="utf-8",
    )
    (BUILD_DIR / ".nojekyll").write_text("", encoding="utf-8")

    build_home(BUILD_DIR)
    build_lessons(BUILD_DIR)
    build_project_page(BUILD_DIR)

    # Mantém os caminhos relativos dos exemplos e suas mídias.
    shutil.copytree(EXAMPLES, BUILD_DIR / "exemplos")

    validate_generated_site(BUILD_DIR)

    # Só substitui a pasta site/ depois que toda a geração e validação terminar.
    if SITE.exists():
        shutil.rmtree(SITE)
    BUILD_DIR.rename(SITE)

    page_count = 1 + len(LESSONS) + 1
    print(f"Site gerado com sucesso em: {SITE}")
    print(f"Páginas principais geradas: {page_count}")
    print("Verificações básicas: OK")


if __name__ == "__main__":
    try:
        build()
    except Exception as error:
        raise SystemExit(f"ERRO AO GERAR O SITE: {error}") from error

