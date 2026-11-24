# Aula 03 — Fundamentos do HTML

## Objetivo da aula

Estruturar um documento HTML5 e organizar o conteúdo com elementos semânticos, títulos, parágrafos, links e comentários.

## Conteúdo abordado

- HTML como linguagem de marcação.
- Estrutura do documento: `<!DOCTYPE html>`, `html`, `head` e `body`.
- Tags de abertura e fechamento e elementos sem conteúdo interno.
- Atributos, como `href`, `src` e `alt`.
- Elementos semânticos: `header`, `nav`, `main`, `section`, `article`, `aside` e `footer`.
- Hierarquia de títulos de `h1` a `h6`.
- Formatação com `strong`, `em`, `sub` e `sup`.
- Parágrafos, quebras de linha e comentários HTML.

## Atividade indicada no PDF

Criar um documento HTML5 em português; adicionar um cabeçalho com títulos de `h1` a `h6` com alinhamentos solicitados; criar uma navegação com âncoras para posts, lateral e rodapé; estruturar uma seção de posts e um artigo; formatar texto em negrito, itálico, sublinhado, riscado, subscrito e sobrescrito; aplicar texto azul e maior com CSS inline; centralizar uma frase com uma classe CSS; justificar um parágrafo com quebra de linha; criar `aside` e `footer`; comentar todo o código e documentar com código, repositório e prints.

## Resolução

A solução completa está em `exemplos/aula-03/index.html` e `exemplos/aula-03/style.css`.

### Como a solução atende ao enunciado

1. O `DOCTYPE` declara HTML5; `lang="pt-BR"` identifica o idioma; `meta charset="UTF-8"` define a codificação.
2. O `header` apresenta `h1` centralizado, `h2` à esquerda, `h3` à direita e os níveis `h4`, `h5` e `h6`.
3. O `nav` contém três links de âncora separados por barras verticais.
4. O `section#posts` contém `article.post` e seu cabeçalho.
5. `strong` e `em` comunicam ênfase semântica; sublinhado e tachado são aplicados por CSS; `sub` e `sup` ilustram índices.
6. O parágrafo azul usa `style` inline, conforme solicitado no item da atividade. Em projetos reais, o ideal é mover esse estilo para o CSS externo.
7. `.center` aplica `text-align: center`.
8. O parágrafo justificado usa `text-align: justify` e `br` para uma quebra de linha.
9. O `aside#lateral` apresenta conteúdo relacionado.
10. O `footer#rodape` contém a mensagem de copyright didática solicitada.
11. Comentários HTML identificam as principais partes.

## Resultado esperado

Uma página de blog simples, navegável pelas âncoras internas, com a hierarquia visual e a formatação textual especificadas.

## Conceitos-chave

Estrutura HTML5, semântica, atributos, hierarquia de headings, âncoras, classes, IDs e comentários.
