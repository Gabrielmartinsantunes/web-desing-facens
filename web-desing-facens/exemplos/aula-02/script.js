// JavaScript externo: comportamento do botão de demonstração.
const botaoMensagem = document.querySelector("#botao-mensagem");
const mensagem = document.querySelector("#mensagem");

botaoMensagem.addEventListener("click", () => {
    mensagem.textContent = "A alteração foi registrada? Agora salve um commit no Git.";
});
