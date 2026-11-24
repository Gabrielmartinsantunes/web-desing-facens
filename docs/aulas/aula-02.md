# Aula 02 — Introdução ao Web Design e Controle de Versões

## Objetivo da aula

Compreender a função do Web Design, distinguir HTML, CSS e JavaScript e iniciar o controle de versões com Git e GitHub.

## Conteúdo abordado

- Web Design como combinação de design visual, funcionalidade, usabilidade e acessibilidade.
- HTML para estrutura, CSS para apresentação e JavaScript para interatividade.
- Controle de versões e histórico de alterações.
- Git, repositórios locais e repositórios remotos.
- Commits, branches e tags.
- Deploy como publicação da aplicação em ambiente acessível aos usuários.
- Vercel como alternativa de hospedagem integrada ao Git.

## Atividade indicada no PDF

O enunciado pede instalar o Visual Studio Code, criar `index.html`, `style.css` e `script.js` com os códigos fornecidos, salvar tudo na mesma pasta, configurar Git no VS Code, inicializar o versionamento, publicar no GitHub, alterar o projeto, registrar as mudanças com commits e tags, documentar o processo e enviar o arquivo pelo Canvas.

## Lacuna identificada no material

O enunciado fala em “copiar os códigos fornecidos”, mas o PDF recebido não contém esses códigos iniciais. Para permitir o treino, a pasta `exemplos/aula-02/` traz um projeto inicial simples criado para esta apostila. Ele é uma solução de referência própria, não uma reprodução de um código oficial ausente.

## Resolução passo a passo

1. Instalar o Git a partir de [git-scm.com](https://git-scm.com/downloads) e o Visual Studio Code.
2. Conferir a instalação com `git --version` no terminal.
3. Configurar nome e e-mail que serão gravados nos commits.
4. Abrir a pasta do exemplo no VS Code.
5. Inicializar o repositório local.
6. Registrar o primeiro commit.
7. Criar um repositório remoto no GitHub e associá-lo ao diretório local.
8. Fazer o primeiro `push`.
9. Alterar algum conteúdo, registrar outro commit e criar uma tag.
10. Enviar a tag ao remoto e documentar os passos.

## Comandos equivalentes no terminal

```bash
git --version
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"

cd caminho/para/aula-02
git init
git add .
git commit -m "chore: estrutura inicial do projeto"
git branch -M main

git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main

# Depois de realizar uma alteração:
git add .
git commit -m "feat: adiciona mensagem de boas-vindas"
git tag -a v1.0.0 -m "Primeira versão estável"
git push origin main
git push origin v1.0.0
```

Substitua `SEU-USUARIO`, `SEU-REPOSITORIO` e o e-mail pelos seus dados. Não publique credenciais, tokens ou senhas em arquivos versionados.

## O que é uma tag?

Uma tag marca um ponto específico do histórico. Os slides apresentam a tag leve e a tag anotada. O exemplo acima usa tag anotada (`git tag -a`) para guardar uma mensagem descritiva. `git tag` lista as tags existentes.

## Resultado esperado

Um repositório remoto com os arquivos, histórico de commits e uma tag criada; mais um documento com descrição das etapas e capturas de tela, enviado no Canvas.

## Evidências recomendadas

- Terminal mostrando `git --version`.
- Repositório local inicializado no VS Code.
- Histórico com pelo menos dois commits.
- Repositório remoto com os três arquivos.
- Tag visível no GitHub.

## Conceitos-chave

Git, GitHub, repositório, commit, branch, tag, push, histórico, deploy.
