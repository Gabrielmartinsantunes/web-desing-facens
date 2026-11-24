# Aula 04 — Mídias em HTML

## Objetivo da aula

Adicionar conteúdo multimídia e componentes comuns de interface a uma página HTML.

## Conteúdo abordado

A sequência da atividade trabalha imagens, vídeo, áudio, formulários, links, listas, tabelas, IDs, classes e `div` como contêiner. Os elementos são agrupados dentro da estrutura HTML5 com `header`, `main` e `footer`.

## Atividade indicada no PDF

Criar `index.html` com estrutura HTML5; adicionar três imagens com `src`, `alt`, `width` e `height` e testar uma imagem sem dimensões; inserir um vídeo com `controls`, `width` e `poster`; inserir áudio com fontes MP3 e OGG e texto alternativo; montar formulário com nome, e-mail, mensagem e botão; criar três tipos de links; criar listas ordenada e não ordenada; montar tabela de três colunas e três linhas com `thead` e `tbody`; criar um parágrafo com ID e dois parágrafos com classe `destaque` com fundo amarelo-claro; agrupar um subtítulo e dois parágrafos em uma `div`; comentar e documentar o código.

## Resolução

A solução está em `exemplos/aula-04/index.html`, com estilos em `style.css` e imagens SVG didáticas na pasta `assets/images/`.

### Mídias que precisam ser fornecidas

O PDF menciona `video.mp4`, `musica.mp3` e `musica.ogg`, mas esses arquivos não vieram entre os anexos. A solução mantém os caminhos `assets/video/video.mp4`, `assets/audio/musica.mp3` e `assets/audio/musica.ogg`. Para reproduzir vídeo e áudio, coloque arquivos reais nesses caminhos. O elemento HTML e as alternativas de formato já estão configurados.

### Como testar

1. Abra `index.html` no navegador.
2. Confira as três imagens de exemplo.
3. Teste os links de navegação e o link externo em nova aba.
4. Verifique se os campos `required` impedem o envio do formulário vazio.
5. Confirme a estrutura da tabela e das listas.
6. Depois de adicionar mídia real, teste `controls` no vídeo e no áudio.

## Resultado esperado

Página com blocos de mídia, formulário, links, listas e tabela. O vídeo e o áudio só funcionarão após a inclusão dos arquivos binários indicados.

## Conceitos-chave

`img`, `alt`, dimensões, `video`, `audio`, `source`, `form`, `label`, `input`, `textarea`, `a`, `target`, `ol`, `ul`, `table`, `thead`, `tbody`, `id`, `class` e `div`.
