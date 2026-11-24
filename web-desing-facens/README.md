# Apostila Acadêmica de Web Design — FACENS

Material de apoio acadêmico organizado a partir dos oito arquivos de aula enviados nesta conversa e do Plano de Aprendizagem de Web Design (CATIN1).

> **Escopo:** esta versão acompanha os arquivos nomeados de Aula 01 a Aula 08. O número da aula aqui segue o nome dos PDFs fornecidos, não a numeração do cronograma do Plano de Aprendizagem.

## Objetivo

Reunir os conteúdos das aulas, explicar os conceitos em linguagem didática e apresentar resoluções completas das atividades práticas localizadas nos materiais. Cada resolução inclui o enunciado, a proposta de solução, os arquivos de código, explicações e observações sobre o que precisa ser comprovado na entrega acadêmica.

## Organização

```text
web-desing-facens/
├── README.md
├── requirements.txt
├── build_site.py
├── .github/workflows/pages.yml
├── docs/
│   ├── index.md
│   ├── aulas/
│   │   ├── aula-01.md
│   │   ├── aula-02.md
│   │   ├── aula-03.md
│   │   ├── aula-04.md
│   │   ├── aula-05.md
│   │   ├── aula-06.md
│   │   ├── aula-07.md
│   │   └── aula-08.md
│   └── projetos/pastelaria-da-sogra.md
├── exemplos/
│   ├── aula-02/
│   ├── aula-03/
│   ├── aula-04/
│   ├── aula-05/
│   ├── aula-06/
│   ├── aula-07/
│   └── aula-08/
└── site/                 # site estático gerado por build_site.py
```

## Como visualizar localmente

Requer Python 3.10 ou superior.

```bash
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000 --directory site
```

Abra `http://localhost:8000` no navegador.

## Publicação no GitHub Pages

O arquivo `.github/workflows/pages.yml` prepara a publicação automática a cada atualização na branch `main`.

1. Na conta `Gabrielmartinsantunes`, crie um repositório público chamado `web-desing-facens`. Deixe o repositório vazio (não gere outro README, `.gitignore` ou licença).
2. Extraia este pacote, abra um terminal na pasta `web-desing-facens` e execute:

   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "feat: cria apostila acadêmica de Web Design"
   git remote add origin https://github.com/Gabrielmartinsantunes/web-desing-facens.git
   git push -u origin main
   ```

3. No GitHub, abra **Settings → Pages → Build and deployment → Source** e selecione **GitHub Actions**.
4. Abra a aba **Actions** e acompanhe o workflow `Publicar apostila no GitHub Pages`.
5. Quando a execução terminar com sucesso, confira o endereço que o GitHub exibir em **Settings → Pages**. O endereço esperado para este repositório é `https://gabrielmartinsantunes.github.io/web-desing-facens/`.

O pacote contém a configuração do deploy, mas a publicação online só passa a existir depois que o repositório remoto for criado, os arquivos forem enviados e o GitHub Pages estiver habilitado.

## Fontes e fidelidade ao material

- As explicações e os enunciados são fundamentados nos PDFs Aula 01 a Aula 08 e no Plano de Aprendizagem enviados.
- Quando o PDF menciona um código fornecido em aula que não aparece no arquivo recebido, a lacuna é explicitada. Um exemplo mínimo elaborado para completar o exercício é identificado como solução de referência, não como código oficial do professor.
- A Aula 01 contém uma atividade de organização de grupo, não um exercício de programação.
- A Aula 02 descreve a criação do projeto e o fluxo de versionamento, mas faz referência a códigos fornecidos que não constam no PDF recebido.
- As atividades que dependem de arquivos de mídia externos (vídeo e áudio) indicam os caminhos que devem ser preenchidos pelos estudantes; os arquivos binários não vieram com os materiais.

## Projeto acadêmico em grupo

O projeto **Pastelaria da Sogra** é citado como experiência prática coletiva, sem atribuir o desenvolvimento a uma única pessoa. Repositório: <https://github.com/vitorhugo-santos/projeto-web-pastelaria-da-sogra>.

## Referências de apoio indicadas nas aulas

- Repositório de materiais do docente: <https://github.com/deivisontakatu/aula-web-design>
- Perfil GitHub do docente: <https://github.com/deivisontakatu>
- Material complementar de CSS: <https://github.com/deivisontakatu/aula-css>
- Material complementar de JavaScript: <https://github.com/deivisontakatu/aula-javascript>

## Aviso acadêmico

Este repositório é um material independente de estudo. Não é publicação oficial da FACENS nem substitui as orientações do docente, o Canvas ou os critérios de avaliação vigentes. Antes de enviar qualquer atividade, confira as instruções e os prazos na plataforma da disciplina.
