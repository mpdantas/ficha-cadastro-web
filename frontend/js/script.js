// Função para obter a data atual no formato DD/MM/AAAA
function obterDataAtual() {
    const hoje = new Date(); // Cria um novo objeto Date com a data e hora atuais
    const dia = String(hoje.getDate()).padStart(2, '0'); // Obtém o dia e adiciona um zero à esquerda se for menor que 10
    const mes = String(hoje.getMonth() + 1).padStart(2, '0'); // Obtém o mês (0-11), adiciona 1 e formata com zero à esquerda
    const ano = hoje.getFullYear(); // Obtém o ano com quatro dígitos
    return `${dia}/${mes}/${ano}`; // Retorna a data no formato DD/MM/AAAA
}

// Função para preencher automaticamente o campo de data de preenchimento ao carregar a página
function preencherDataPreenchimento() {
    const dataPreenchimentoInput = document.getElementById('dataPreenchimento'); // Obtém o elemento input da data de preenchimento pelo seu ID
    if (dataPreenchimentoInput) { // Verifica se o elemento foi encontrado no DOM
        dataPreenchimentoInput.value = obterDataAtual(); // Define o valor do campo com a data atual formatada
    }
}

// Função para mostrar ou esconder os campos específicos da modalidade de seguro selecionada
function mostrarCamposModalidade() {
    const modalidadeSeguroSelect = document.getElementById('modalidadeSeguro'); // Obtém o elemento select da modalidade do seguro pelo seu ID
    const camposAuto = document.getElementById('camposAuto'); // Obtém a div dos campos de seguro Auto
    const camposVida = document.getElementById('camposVida'); // Obtém a div dos campos de seguro Vida
    const camposResidencia = document.getElementById('camposResidencia'); // Obtém a div dos campos de seguro Residência
    const camposEmpresa = document.getElementById('camposEmpresa'); // Obtém a div dos campos de seguro Empresa
    const camposPortatil = document.getElementById('camposPortatil'); // Obtém a div dos campos de seguro Equipamento portátil

    // Esconde todos os campos de modalidade inicialmente
    camposAuto.style.display = 'none';
    camposVida.style.display = 'none';
    camposResidencia.style.display = 'none';
    camposEmpresa.style.display = 'none';
    camposPortatil.style.display = 'none';

    // Obtém o valor selecionado no dropdown de modalidade
    const modalidadeSelecionada = modalidadeSeguroSelect.value;

    // Mostra os campos correspondentes à modalidade selecionada
    if (modalidadeSelecionada === 'auto') {
        camposAuto.style.display = 'block';
    } else if (modalidadeSelecionada === 'vida') {
        camposVida.style.display = 'block';
    } else if (modalidadeSelecionada === 'residencia') {
        camposResidencia.style.display = 'block';
    } else if (modalidadeSelecionada === 'empresa') {
        camposEmpresa.style.display = 'block';
    } else if (modalidadeSelecionada === 'portatil') {
        camposPortatil.style.display = 'block';
    }
}

// Adiciona um ouvinte de evento para executar a função preencherDataPreenchimento quando a página for carregada
// Adiciona um ouvinte de evento para executar funções quando a página for carregada
window.onload = function() {
    preencherDataPreenchimento(); // Preenche a data de preenchimento
    atualizarAnoRodape(); // Atualiza o ano no rodapé

    const cpfInput = document.getElementById('cpf');
    if (cpfInput) {
        new Cleave(cpfInput, {
            blocks: [3, 3, 3, 2],
            delimiters: ['.', '.', '-'],
            numericOnly: true
        });
    }
};

// Adiciona um ouvinte de evento para executar a função mostrarCamposModalidade sempre que o valor do dropdown de modalidade mudar
const modalidadeSeguroSelect = document.getElementById('modalidadeSeguro');
if (modalidadeSeguroSelect) { // Verifica se o elemento foi encontrado
    modalidadeSeguroSelect.addEventListener('change', mostrarCamposModalidade);
}

// Função placeholder para a geração do PDF (a lógica real será no backend em Python)
//function gerarPDF() {
    //alert('Funcionalidade de gerar PDF será implementada no backend.');
    // Aqui, em um cenário real, você faria uma requisição para o seu backend Python
    // enviando os dados do formulário para que ele gere o PDF.
//}

// Função para atualizar o ano no rodapé
function atualizarAnoRodape() {
    const currentYearSpan = document.getElementById('currentYear'); // Obtém o elemento span pelo seu ID
    if (currentYearSpan) { // Verifica se o elemento foi encontrado
        const anoAtual = new Date().getFullYear(); // Obtém o ano atual com quatro dígitos
        currentYearSpan.textContent = anoAtual; // Define o conteúdo do span com o ano atual
    } else {
        console.log("Elemento currentYear não encontrado no rodapé.");
    }
}