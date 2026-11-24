# Aula 02 — Projeto inicial para versionamento

Os slides solicitam que sejam criados `index.html`, `style.css` e `script.js` usando códigos fornecidos pelo professor. Esses trechos não aparecem no PDF recebido. Os três arquivos desta pasta formam uma base didática própria para demonstrar a separação entre HTML, CSS e JavaScript e permitir que o exercício de Git seja praticado.

## Como executar

Abra `index.html` no navegador. Clique no botão para alterar o parágrafo.

## Fluxo do Git

```bash
git init
git add .
git commit -m "chore: estrutura inicial"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

Altere uma frase ou cor e faça outro commit:

```bash
git add .
git commit -m "feat: altera mensagem de boas-vindas"
git tag -a v1.0.0 -m "Primeira versão"
git push origin main
git push origin v1.0.0
```

A URL do remoto é um exemplo. Troque pelos dados do repositório que você criar. A tag anotada guarda uma mensagem sobre a versão. Os comandos de configuração do usuário são globais e devem usar o nome e o e-mail reais que você deseja associar aos commits.
