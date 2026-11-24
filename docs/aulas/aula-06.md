# Aula 06 — CSS: Seletores, Cores, Tipografia e Layouts Básicos

## Objetivo da aula

Separar apresentação e estrutura, aplicar seletores e propriedades CSS e produzir um layout claro e responsivo.

## Conteúdo abordado

- Benchmarking e prototipação como etapas de preparação do projeto.
- Sintaxe CSS: seletor, propriedade e valor.
- CSS inline, interno e externo; os slides recomendam CSS externo em projetos maiores.
- Propriedades trabalhadas: `color`, `background-color`, `font-family`, `font-size`, `margin`, `padding`, `border`, `width`, `height`, `display`, `position`, `top`, `right`, `bottom`, `left` e `text-align`.
- Classes para agrupar estilos e IDs para alvos específicos.

## Atividade indicada no PDF

Criar um projeto com `index.html` e `style.css`, vincular o CSS externamente, aplicar as propriedades vistas em aula, incluir pelo menos dez propriedades adicionais para melhorar design, interatividade e responsividade, integrar o projeto a um repositório GitHub, melhorá-lo para ter mais de 300 linhas de HTML e mais de 200 linhas de CSS, comentar o código e documentar com código, repositório e prints.

## Resolução

A pasta `exemplos/aula-06/` contém uma página de portfólio acadêmico e uma folha de estilos externa. O projeto aplica as propriedades listadas e acrescenta, entre outras, `max-width`, `min-height`, `line-height`, `letter-spacing`, `border-radius`, `box-shadow`, `transition`, `transform`, `opacity`, `gap`, `flex-wrap` e media queries.

### Por que manter o CSS externo?

O CSS externo mantém as regras visuais fora do HTML. Isso facilita reaproveitar estilos, reduzir duplicação e alterar o design sem mexer na estrutura do conteúdo.

### Conferência dos critérios

O exemplo é produzido com mais de 300 linhas em `index.html` e mais de 200 linhas em `style.css`. Os comentários explicam os blocos. A contagem de linhas atende ao requisito textual da atividade, mas não deve ser confundida com uma medida de qualidade: clareza, semântica e manutenção continuam sendo critérios mais importantes.

## Resultado esperado

Página de portfólio estilizada, com CSS externo, classes reutilizáveis e adaptação básica a telas menores.

## Conceitos-chave

Seletores, classes, IDs, cascata, cores, tipografia, espaçamento, dimensões, posicionamento, display e responsividade.
