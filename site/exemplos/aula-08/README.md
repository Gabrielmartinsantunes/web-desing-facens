# Aula 08 — Painel interativo com JavaScript

Este projeto resolve a atividade de JavaScript: sintaxe, variáveis e estruturas.

## Arquivos

- `index.html`: estrutura dos componentes e campos de entrada.
- `style.css`: apresentação visual e adaptação para telas menores.
- `script.js`: lógica, eventos e manipulação do DOM.

## Como executar

1. Abra a pasta no Visual Studio Code.
2. Abra `index.html` no navegador ou use uma extensão de servidor local.
3. Abra as ferramentas do desenvolvedor do navegador para visualizar o console.
4. Teste cada seção do painel.

## Funcionalidades implementadas

### 1. Saudação personalizada

O usuário digita o nome e pressiona o botão.
O JavaScript lê o valor do campo com `value`.
O método `trim` remove espaços externos.
A condicional `if` impede uma resposta vazia.
A saudação é exibida com `textContent`.

### 2. Contador

A variável `contador` utiliza `let` porque seu valor muda.
O botão de incremento soma uma unidade.
O botão de decremento subtrai uma unidade quando o valor é maior que zero.
O botão zerar restaura o valor inicial.
A função de atualização altera o elemento `output`.

### 3. Calculadora de média

Os campos de nota são lidos e convertidos com `Number`.
As notas ficam armazenadas em um array.
A função valida se cada nota está no intervalo entre zero e dez.
O método `forEach` percorre as notas e soma os valores.
A média é calculada dividindo a soma pelo tamanho do array.
As estruturas `if`, `else if` e `else` produzem uma mensagem didática de situação.
A classificação exibida é um exemplo e não substitui as regras oficiais de avaliação da instituição.

### 4. Lista de tarefas

O formulário escuta o evento `submit`.
`preventDefault` evita que o navegador recarregue a página.
`createElement` cria os elementos `li`, `span` e `button`.
`textContent` insere o texto digitado com segurança.
`appendChild` adiciona os nós à lista.
O botão Remover possui seu próprio evento de clique.

### 5. Filtro de conteúdos

Um array de objetos guarda título, categoria e descrição.
O elemento `select` fornece a categoria escolhida.
`filter` cria um novo array com a categoria selecionada.
`forEach` percorre os resultados.
Os cartões são criados dinamicamente e adicionados ao DOM.
Escolher Todos exibe a lista completa.

### 6. Alternância de tema

O botão chama `classList.toggle` no elemento `body`.
O CSS muda as variáveis de cor quando a classe `tema-escuro` está presente.
Essa solução separa comportamento e apresentação.

## Conceitos do material da aula

- `const` e `let` para declarar variáveis.
- Strings, números e booleanos como tipos básicos.
- Operadores aritméticos e comparação.
- Condicionais `if`, `else if` e `else`.
- Laço `for` e método `forEach`.
- Funções tradicionais e funções de seta.
- Arrays e objetos.
- Propriedades e métodos de objetos.
- `querySelector`, `textContent`, `value` e `classList`.
- `createElement` e `appendChild`.
- `addEventListener` para eventos de clique, mudança e submissão.

## Testes manuais recomendados

1. Tente gerar uma saudação com o campo vazio.
2. Digite um nome com espaços antes e depois.
3. Clique várias vezes em aumentar e diminuir o contador.
4. Tente diminuir o contador quando ele estiver em zero.
5. Calcule a média com notas válidas.
6. Informe uma nota abaixo de zero ou acima de dez.
7. Adicione uma tarefa com texto e remova-a.
8. Tente submeter uma tarefa vazia.
9. Troque as categorias do filtro.
10. Alterne o tema claro e escuro.
11. Reduza a largura da janela para conferir a responsividade.
12. Confira mensagens e erros no console do navegador.

## Observações técnicas

O projeto não usa frameworks nem bibliotecas externas.
O arquivo JavaScript é carregado com `defer`.
Os textos inseridos pelo usuário são exibidos com `textContent`.
A lista de tarefas existe apenas em memória e será perdida ao recarregar a página.
Não há backend, autenticação ou armazenamento persistente.
As notas são usadas somente para demonstrar operadores, arrays e condicionais.

## Versionamento

Inicialize um repositório Git na pasta do projeto.
Registre o estado inicial com um commit descritivo.
Implemente uma funcionalidade por vez e salve novos commits.
Crie uma tag quando considerar uma versão estável.
Publique o repositório no GitHub e inclua o endereço verdadeiro na entrega.

## Evidências para a atividade

- Captura de tela da saudação.
- Captura de tela do contador.
- Captura de tela do resultado da média.
- Captura de tela da lista de tarefas.
- Captura de tela do filtro de conteúdos.
- Captura de tela da alternância de tema.
- Captura de tela do repositório remoto e do histórico de commits.

## Critérios de linha solicitados no PDF

O enunciado pede mais de 500 linhas em HTML, mais de 400 em CSS e mais de 300 em JavaScript.
Os arquivos desta pasta foram organizados para ultrapassar esses limites com comentários e demonstrações didáticas.
Quantidade de linhas não garante, por si só, qualidade, clareza ou desempenho.
O código deve continuar legível, coerente e fácil de testar.

## Limite da solução

Esta é uma implementação de referência para estudo.
Compare-a com os exemplos vistos na aula e adapte o conteúdo às orientações do professor.
Não apresente os exemplos como se fossem códigos fornecidos oficialmente pelo docente.
Antes de enviar, confira o prazo e os critérios atualizados no Canvas.
