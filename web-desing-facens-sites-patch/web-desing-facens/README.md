# Apostila Acadêmica de Web Design — FACENS

Material de apoio acadêmico organizado a partir dos oito arquivos de aula e do Plano de Aprendizagem de Web Design (CATIN1).

> **Escopo:** esta versão acompanha os arquivos nomeados de Aula 01 a Aula 08. A numeração segue os títulos dos PDFs enviados, não a numeração dos encontros no cronograma do Plano de Aprendizagem.

## Objetivo

Reunir os conteúdos das aulas, explicar os conceitos em linguagem didática e apresentar resoluções de referência para as atividades localizadas nos materiais. O repositório possui duas camadas: uma apostila navegável com resumo e resolução por aula e um site prático independente para cada uma das oito aulas.

## Organização

```text
web-desing-facens/
├── README.md
├── requirements.txt
├── build_site.py
├── .github/workflows/pages.yml
├── docs/
│   ├── index.md
│   ├── aulas/                 # conteúdo, enunciados e resoluções
│   │   ├── aula-01.md
│   │   ├── aula-02.md
│   │   ├── aula-03.md
│   │   ├── aula-04.md
│   │   ├── aula-05.md
│   │   ├── aula-06.md
│   │   ├── aula-07.md
│   │   └── aula-08.md
│   └── projetos/pastelaria-da-sogra.md
├── exemplos/                  # oito sites práticos independentes
│   ├── aula-01/               # apresentação e organização do grupo
│   ├── aula-02/               # base para versionamento com Git
│   ├── aula-03/               # blog em HTML semântico
│   ├── aula-04/               # página com mídias e formulário
│   ├── aula-05/               # página de demonstração de SEO
│   ├── aula-06/               # portfólio com CSS externo
│   ├── aula-07/               # Box Model e Flexbox
│   └── aula-08/               # painel com interações em JavaScript
└── site/                      # site estático gerado por build_site.py
```

## Sites práticos por aula

Os oito sites ficam em `exemplos/aula-XX/` e têm um `index.html` próprio. O catálogo dos projetos fica em `exemplos/index.html`. Após a publicação pelo GitHub Pages, o catálogo estará em `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/` e os endereços individuais seguem este padrão:

- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-01/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-02/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-03/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-04/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-05/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-06/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-07/`
- `https://gabrielmartinsantunes.github.io/web-desing-facens/exemplos/aula-08/`

A Aula 01 exige formação de grupo e envio dos nomes pelo Canvas, não um exercício de programação. Por isso, seu site é um material visual complementar de apresentação da disciplina e apoio à organização do grupo; não é apresentado como atividade oficial do professor.

## Como visualizar localmente

Requer Python 3.10 ou superior.

```bash
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000 --directory site
```

Abra `http://localhost:8000` no navegador. Os sites práticos também podem ser abertos diretamente a partir de `site/exemplos/aula-XX/index.html` depois da geração.

## Publicação no GitHub Pages

O arquivo `.github/workflows/pages.yml` prepara a publicação automática a cada atualização na branch `main`.

1. Mantenha o repositório público `Gabrielmartinsantunes/web-desing-facens`.
2. Envie as alterações para a branch `main`.
3. Em **Settings → Pages → Build and deployment → Source**, mantenha **GitHub Actions**.
4. Acompanhe o workflow `Publicar apostila no GitHub Pages` na aba **Actions**.
5. Após uma execução concluída com sucesso, acesse `https://gabrielmartinsantunes.github.io/web-desing-facens/`.

## Fontes e fidelidade ao material

- As explicações e os enunciados são fundamentados nos PDFs Aula 01 a Aula 08 e no Plano de Aprendizagem enviados.
- Quando um PDF menciona um código fornecido em aula que não aparece no arquivo recebido, a lacuna é explicitada. O exemplo de partida criado para estudo é identificado como material de referência, não como código oficial do professor.
- A Aula 01 contém uma atividade de organização de grupo, não um exercício de programação.
- A Aula 02 menciona códigos fornecidos que não constam no PDF recebido; o projeto inicial é uma base didática própria.
- As atividades que dependem de vídeo e áudio indicam os caminhos previstos, mas os arquivos binários não vieram nos materiais.

## Projeto acadêmico em grupo

O projeto **Pastelaria da Sogra** é citado como experiência prática coletiva, sem atribuir o desenvolvimento a uma única pessoa. Repositório: <https://github.com/vitorhugo-santos/projeto-web-pastelaria-da-sogra>.

## Referências de apoio indicadas nas aulas

- Repositório de materiais do docente: <https://github.com/deivisontakatu/aula-web-design>
- Perfil GitHub do docente: <https://github.com/deivisontakatu>
- Material complementar de CSS: <https://github.com/deivisontakatu/aula-css>
- Material complementar de JavaScript: <https://github.com/deivisontakatu/aula-javascript>

## Aviso acadêmico

Este repositório é um material independente de estudo. Não é publicação oficial da FACENS nem substitui as orientações do docente, o Canvas ou os critérios de avaliação vigentes. Antes de enviar qualquer atividade, confira as instruções e os prazos na plataforma da disciplina.
