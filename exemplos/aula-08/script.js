/* ==========================================================
   AULA 08 — JAVASCRIPT DO PAINEL INTERATIVO
   Conceitos usados: const, let, operadores, condicionais,
   funções, arrays, objetos, DOM e addEventListener.
   ========================================================== */

// Seleciona elementos uma vez para reutilizar nas funções.
const botaoTema = document.querySelector("#alternar-tema");
const campoNome = document.querySelector("#nome-usuario");
const botaoSaudacao = document.querySelector("#gerar-saudacao");
const resultadoSaudacao = document.querySelector("#resultado-saudacao");
const valorContador = document.querySelector("#valor-contador");
const botaoAumentar = document.querySelector("#aumentar-contador");
const botaoDiminuir = document.querySelector("#diminuir-contador");
const botaoZerar = document.querySelector("#zerar-contador");
const botaoMedia = document.querySelector("#calcular-media");
const resultadoMedia = document.querySelector("#resultado-media");
const formularioTarefa = document.querySelector("#form-tarefa");
const campoTarefa = document.querySelector("#texto-tarefa");
const listaTarefas = document.querySelector("#lista-tarefas");
const seletorCategoria = document.querySelector("#categoria-filtro");
const resultadosFiltro = document.querySelector("#resultados-filtro");
const resumoObjeto = document.querySelector("#resumo-objeto");

// Variável mutável porque seu valor muda a cada interação do contador.
let contador = 0;

// Array de objetos usado pela funcionalidade de filtro.
const conteudos = [
    { titulo: "Estrutura HTML5", categoria: "html", descricao: "Organize títulos e seções." },
    { titulo: "Links e imagens", categoria: "html", descricao: "Use href, src e alt." },
    { titulo: "Tabelas e formulários", categoria: "html", descricao: "Estruture dados e campos." },
    { titulo: "Seletores CSS", categoria: "css", descricao: "Escolha os elementos por tag, classe ou ID." },
    { titulo: "Tipografia e cores", categoria: "css", descricao: "Defina fontes e contraste." },
    { titulo: "Box Model", categoria: "css", descricao: "Observe content, padding, border e margin." },
    { titulo: "Variáveis JavaScript", categoria: "javascript", descricao: "Pratique let e const." },
    { titulo: "Funções e arrays", categoria: "javascript", descricao: "Agrupe lógica e listas de valores." },
    { titulo: "DOM e eventos", categoria: "javascript", descricao: "Reaja a ações do usuário." }
];

// Objeto para demonstrar propriedades e um método com this.
const estudante = {
    nome: "Estudante",
    disciplina: "Web Design",
    descrever() {
        return `${this.nome} está estudando ${this.disciplina}.`;
    }
};

// Confere se um elemento foi localizado antes de continuar.
function elementoExiste(elemento) {
    return elemento !== null;
}

// Atualiza o texto do contador no DOM.
function atualizarContador() {
    valorContador.textContent = String(contador);
}

// Aumenta o valor da variável e atualiza a apresentação.
function aumentarContador() {
    contador = contador + 1;
    atualizarContador();
}

// Diminui o valor atual sem permitir que fique negativo.
function diminuirContador() {
    if (contador > 0) {
        contador = contador - 1;
    } else {
        contador = 0;
    }
    atualizarContador();
}

// Restaura o valor inicial do exemplo.
function zerarContador() {
    contador = 0;
    atualizarContador();
}

// Gera uma saudação usando uma entrada do usuário.
function gerarSaudacao() {
    const nomeDigitado = campoNome.value.trim();

    if (nomeDigitado === "") {
        resultadoSaudacao.textContent = "Digite seu nome antes de continuar.";
        campoNome.focus();
        return;
    }

    resultadoSaudacao.textContent = `Olá, ${nomeDigitado}! Bons estudos de JavaScript.`;
}

// Converte os valores digitados e valida o intervalo de cada nota.
function lerNotas() {
    const campoNota1 = document.querySelector("#nota-1");
    const campoNota2 = document.querySelector("#nota-2");
    const campoNota3 = document.querySelector("#nota-3");
    const notas = [
        Number(campoNota1.value),
        Number(campoNota2.value),
        Number(campoNota3.value)
    ];

    for (let indice = 0; indice < notas.length; indice++) {
        if (Number.isNaN(notas[indice]) || notas[indice] < 0 || notas[indice] > 10) {
            return null;
        }
    }

    return notas;
}

// Calcula a média com um laço para praticar repetição e acumulador.
function calcularMedia() {
    const notas = lerNotas();

    if (notas === null) {
        resultadoMedia.textContent = "Informe três notas entre 0 e 10.";
        return;
    }

    let soma = 0;
    notas.forEach((nota) => {
        soma = soma + nota;
    });

    const media = soma / notas.length;
    let situacao;

    if (media >= 7) {
        situacao = "Aprovado no exemplo";
    } else if (media >= 5) {
        situacao = "Em recuperação no exemplo";
    } else {
        situacao = "Reprovado no exemplo";
    }

    resultadoMedia.textContent = `Média: ${media.toFixed(2)} — ${situacao}.`;
}

// Cria uma tarefa como nó de texto e um botão de remoção.
function criarTarefa(texto) {
    const item = document.createElement("li");
    const textoItem = document.createElement("span");
    const botaoRemover = document.createElement("button");

    textoItem.textContent = texto;
    botaoRemover.type = "button";
    botaoRemover.textContent = "Remover";
    botaoRemover.setAttribute("aria-label", `Remover tarefa: ${texto}`);

    botaoRemover.addEventListener("click", () => {
        item.remove();
    });

    item.appendChild(textoItem);
    item.appendChild(botaoRemover);
    listaTarefas.appendChild(item);
}

// Trata o envio do formulário sem recarregar a página.
function adicionarTarefa(evento) {
    evento.preventDefault();
    const texto = campoTarefa.value.trim();

    if (texto === "") {
        campoTarefa.focus();
        return;
    }

    criarTarefa(texto);
    campoTarefa.value = "";
    campoTarefa.focus();
}

// Cria os cartões dos conteúdos filtrados.
function mostrarConteudos(lista) {
    resultadosFiltro.textContent = "";

    if (lista.length === 0) {
        const aviso = document.createElement("p");
        aviso.textContent = "Nenhum conteúdo encontrado para esta categoria.";
        resultadosFiltro.appendChild(aviso);
        return;
    }

    lista.forEach((conteudo) => {
        const cartao = document.createElement("article");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const categoria = document.createElement("small");

        cartao.classList.add("conteudo-card");
        titulo.textContent = conteudo.titulo;
        descricao.textContent = conteudo.descricao;
        categoria.textContent = conteudo.categoria;

        cartao.appendChild(categoria);
        cartao.appendChild(titulo);
        cartao.appendChild(descricao);
        resultadosFiltro.appendChild(cartao);
    });
}

// Seleciona os conteúdos que correspondem à categoria escolhida.
function filtrarConteudos() {
    const categoriaSelecionada = seletorCategoria.value;
    let conteudosFiltrados;

    if (categoriaSelecionada === "todos") {
        conteudosFiltrados = conteudos;
    } else {
        conteudosFiltrados = conteudos.filter((conteudo) => {
            return conteudo.categoria === categoriaSelecionada;
        });
    }

    mostrarConteudos(conteudosFiltrados);
}

// Alterna uma classe no body para trocar as variáveis de cor do CSS.
function alternarTema() {
    document.body.classList.toggle("tema-escuro");
}

// Registra os eventos de clique dos controles do contador.
botaoAumentar.addEventListener("click", aumentarContador);
botaoDiminuir.addEventListener("click", diminuirContador);
botaoZerar.addEventListener("click", zerarContador);

// Registra o evento do botão de saudação.
botaoSaudacao.addEventListener("click", gerarSaudacao);

// Registra o evento para calcular a média das notas.
botaoMedia.addEventListener("click", calcularMedia);

// O evento submit é usado no formulário de tarefas.
formularioTarefa.addEventListener("submit", adicionarTarefa);

// Atualiza os cartões quando uma opção do select é escolhida.
seletorCategoria.addEventListener("change", filtrarConteudos);

// Registra o evento do botão de troca de tema.
botaoTema.addEventListener("click", alternarTema);

// Inicializa os elementos dinâmicos quando o script é carregado.
function inicializarPainel() {
    atualizarContador();
    filtrarConteudos();
    resumoObjeto.textContent = estudante.descrever();
}

// O script está incluído com defer, então o HTML já foi interpretado.
inicializarPainel();

// Pequenos exemplos de operações podem ser vistos no console do navegador.
console.log("Disciplina:", estudante.disciplina);
console.log("Total de conteúdos disponíveis:", conteudos.length);
console.log("Categorias cadastradas:", conteudos.map((item) => item.categoria));

// Nota de revisão 01: Leia o valor de um campo usando a propriedade value.
// Nota de revisão 02: Use trim para remover espaços no início e no fim de uma entrada.
// Nota de revisão 03: Number converte uma string numérica para um valor do tipo number.
// Nota de revisão 04: Number.isNaN ajuda a identificar valores que não representam números.
// Nota de revisão 05: Uma condicional evita processar dados inválidos.
// Nota de revisão 06: O retorno null indica que a leitura das notas falhou.
// Nota de revisão 07: Um array agrupa dados que pertencem à mesma operação.
// Nota de revisão 08: O índice de um array começa em zero.
// Nota de revisão 09: A propriedade length informa o total de itens.
// Nota de revisão 10: forEach executa uma função uma vez para cada item.
// Nota de revisão 11: filter devolve um novo array sem modificar a lista original.
// Nota de revisão 12: Um objeto agrupa informações com nomes de propriedade.
// Nota de revisão 13: Um método é uma função armazenada dentro de um objeto.
// Nota de revisão 14: this referencia o objeto associado à chamada do método.
// Nota de revisão 15: querySelector utiliza a mesma sintaxe de seletores do CSS.
// Nota de revisão 16: textContent altera texto sem interpretar marcação HTML.
// Nota de revisão 17: createElement cria um nó que ainda não está ligado à página.
// Nota de revisão 18: appendChild conecta um nó ao elemento pai.
// Nota de revisão 19: addEventListener registra a função que será executada no evento.
// Nota de revisão 20: preventDefault impede o comportamento padrão de submissão do formulário.
// Nota de revisão 21: classList.toggle alterna a presença de uma classe.
// Nota de revisão 22: Uma função pequena e nomeada facilita a leitura do código.
// Nota de revisão 23: Evite usar variáveis globais quando um escopo menor é suficiente.
// Nota de revisão 24: Use const para referências que não precisam ser reatribuídas.
// Nota de revisão 25: Use let quando a variável receberá novos valores durante a execução.
// Nota de revisão 26: Template strings permitem inserir valores com ${expressao}.
// Nota de revisão 27: toFixed formata um número para uma quantidade definida de casas decimais.
// Nota de revisão 28: focus ajuda o usuário a retornar ao campo que precisa de correção.
// Nota de revisão 29: aria-live comunica atualizações de conteúdo para tecnologias assistivas.
// Nota de revisão 30: Mensagens de erro devem explicar como corrigir o problema.
// Nota de revisão 31: Não confie apenas na validação visual: valide os dados antes de processá-los.
// Nota de revisão 32: O console do navegador é útil para localizar valores inesperados.
// Nota de revisão 33: Teste valores de borda, como zero, campo vazio e nota dez.
// Nota de revisão 34: Teste cada botão separadamente antes de verificar a página inteira.
// Nota de revisão 35: Verifique se os IDs usados no JavaScript existem no HTML.
// Nota de revisão 36: O atributo defer permite carregar o script sem bloquear a análise inicial do HTML.
// Nota de revisão 37: Separe o comportamento no JavaScript e a aparência no CSS.
// Nota de revisão 38: Evite inserir strings de usuário com innerHTML; prefira textContent.
// Nota de revisão 39: Faça alterações pequenas e valide cada uma antes de continuar.
