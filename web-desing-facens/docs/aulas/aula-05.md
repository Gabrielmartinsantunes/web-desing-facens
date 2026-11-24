# Aula 05 — SEO com HTML

## Objetivo da aula

Aplicar fundamentos de otimização para mecanismos de busca (SEO) à estrutura e ao conteúdo de uma página.

## Conteúdo abordado nos slides

- SEO orgânico e diferença em relação a links patrocinados.
- Rastreamento (crawling) e indexação.
- Arquitetura, autoridade, HTTPS, conteúdo único, URLs amigáveis, responsividade e velocidade.
- Título único, meta description, canonical, viewport, favicon e manifest.
- Idioma do documento e tags semânticas.
- Hierarquia de headings, com um `h1` que descreva o tema principal.
- Links descritivos, navegação interna e breadcrumbs.
- Texto alternativo em imagens e dimensões para estabilidade do layout.
- Dados estruturados em JSON-LD.
- Meta robots para páginas que não devem ser indexadas.
- Acessibilidade, rótulos, contraste e navegação por teclado.

## Atividade indicada no PDF

Elaborar uma página web em HTML com pelo menos 200 linhas, tema livre, acrescentando elementos para melhorar a interface e o design e reutilizando mídias e recursos das atividades anteriores. Em seguida, usar uma ferramenta de PageRank para verificar a nota da página otimizada. Por fim, comentar o código, explicar as técnicas de SEO aplicadas e documentar o trabalho.

## Resolução

A página de exemplo em `exemplos/aula-05/index.html` ultrapassa 200 linhas e usa o tema “Guia acadêmico de Web Design”. O exemplo incorpora metadados, headings organizados, links internos, breadcrumb, conteúdo semântico, imagens com `alt`, `width` e `height`, além de um bloco JSON-LD de tipo `Article`.

### Sobre canonical e dados estruturados

O endereço canonical do exemplo está marcado como valor de demonstração. Antes de publicar, substitua-o pelo endereço público definitivo. Da mesma forma, os dados estruturados devem descrever conteúdo real da página; não mantenha informações fictícias na versão publicada.

### Sobre a avaliação PageRank

Os slides apresentam PageRank como métrica histórica de autoridade por links e citam SEO Site Checkup e SmallSEOTools como referências de ferramenta. O PDF não define qual serviço deve ser usado, nem fornece uma nota de avaliação. Portanto, esta apostila não inventa uma pontuação. Depois do deploy, registre a ferramenta escolhida, a data, o endereço avaliado e a captura do resultado para anexar à documentação.

### Técnicas presentes na solução

- Título e descrição específicos.
- `lang="pt-BR"`, `charset` e `viewport`.
- `canonical` de demonstração, a substituir pelo URL real.
- Estrutura semântica e hierarquia de títulos.
- Navegação por âncoras e breadcrumb.
- Links com texto descritivo.
- Imagens com texto alternativo e dimensões explícitas.
- JSON-LD coerente com o artigo da página.
- Contraste, foco visível e rótulos claros.

## Resultado esperado

Uma página HTML com mais de 200 linhas e uma documentação que explique cada técnica aplicada. A nota de PageRank exige avaliação externa após a publicação e não pode ser simulada no código.

## Conceitos-chave

SEO, crawling, indexação, PageRank, canonical, meta description, viewport, semântica, headings, breadcrumbs, alt, JSON-LD e acessibilidade.
