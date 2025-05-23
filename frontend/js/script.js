// Função para obter a data atual no formato DD/MM/AAAA
// Função para obter a data atual no formato DD/MM/AAAA
function obterDataAtual() {
    const hoje = new Date();
    const dia = String(hoje.getDate()).padStart(2, '0');
    const mes = String(hoje.getMonth() + 1).padStart(2, '0');
    const ano = hoje.getFullYear();
    return `${dia}/${mes}/${ano}`;
}

// Função para preencher automaticamente o campo de data de preenchimento ao carregar a página
function preencherDataPreenchimento() {
    const dataPreenchimentoInput = document.getElementById('dataPreenchimento');
    if (dataPreenchimentoInput) {
        dataPreenchimentoInput.value = obterDataAtual();
    }
}

// Função para mostrar ou esconder os campos específicos da modalidade de seguro e tipo de seguro
function mostrarCamposModalidade() {
    const modalidadeSeguroSelect = document.getElementById('modalidadeSeguro');
    const tipoSeguroSelect = document.getElementById('tipoSeguro'); // Obtém o dropdown de tipo de seguro
    const camposAuto = document.getElementById('camposAuto');
    const camposVida = document.getElementById('camposVida');
    const camposResidencia = document.getElementById('camposResidencia');
    const camposEmpresa = document.getElementById('camposEmpresa');
    const camposPortatil = document.getElementById('camposPortatil');
    const campoClasseBonus = document.getElementById('campoClasseBonus'); // Obtém o campo Classe de Bônus

    // Esconde todos os campos de modalidade e a classe de bônus inicialmente
    camposAuto.style.display = 'none';
    camposVida.style.display = 'none';
    camposResidencia.style.display = 'none';
    camposEmpresa.style.display = 'none';
    camposPortatil.style.display = 'none';
    campoClasseBonus.style.display = 'none'; // Garante que a Classe de Bônus esteja oculta por padrão

    const modalidadeSelecionada = modalidadeSeguroSelect.value;
    const tipoSeguroSelecionado = tipoSeguroSelect.value; // Valor selecionado do tipo de seguro

    // Mostra os campos correspondentes à modalidade selecionada
    if (modalidadeSelecionada === 'auto') {
        camposAuto.style.display = 'block';
        // Lógica para mostrar Classe de Bônus se for Auto E Renovação
        if (tipoSeguroSelecionado === 'renovacao') {
            campoClasseBonus.style.display = 'block';
        }
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

// Função para atualizar o ano no rodapé
function atualizarAnoRodape() {
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        const anoAtual = new Date().getFullYear();
        currentYearSpan.textContent = anoAtual;
    } else {
        console.log("Elemento currentYear não encontrado no rodapé.");
    }
}

// Adiciona um ouvinte de evento para executar funções quando a página for carregada
window.onload = function() {
    preencherDataPreenchimento();
    atualizarAnoRodape();
    // Chamar mostrarCamposModalidade aqui para garantir que o estado inicial esteja correto
    // (útil se o navegador memorizar a seleção do dropdown ao recarregar)
    mostrarCamposModalidade();

    // Inicialização da máscara de CPF com Cleave.js
    const cpfInput = document.getElementById('cpf');
    if (cpfInput) {
        new Cleave(cpfInput, {
            blocks: [3, 3, 3, 2],
            delimiters: ['.', '.', '-'],
            numericOnly: true
        });
    }
};

// Adiciona um ouvinte de evento para o dropdown de modalidade (muda a seção principal)
const modalidadeSeguroSelect = document.getElementById('modalidadeSeguro');
if (modalidadeSeguroSelect) {
    modalidadeSeguroSelect.addEventListener('change', mostrarCamposModalidade);
}

// Adiciona um ouvinte de evento para o dropdown de tipo de seguro (pode afetar campos dentro da modalidade)
const tipoSeguroSelect = document.getElementById('tipoSeguro');
if (tipoSeguroSelect) {
    tipoSeguroSelect.addEventListener('change', mostrarCamposModalidade);
}

// Função placeholder para a geração do PDF (a lógica real está no backend em Python)
function gerarPDF() {
    alert('Funcionalidade de gerar PDF é controlada pelo backend agora.');
}

// ... (seu código existente: obterDataAtual, preencherDataPreenchimento, mostrarCamposModalidade, atualizarAnoRodape, window.onload, event listeners) ...

// Função para buscar endereço por CEP usando a API ViaCEP
function buscarEnderecoPorCep() {
    const cepInput = document.getElementById('cep');
    const enderecoInput = document.getElementById('endereco');
    const bairroInput = document.getElementById('bairro');
    const cidadeInput = document.getElementById('cidade');
    const estadoInput = document.getElementById('estado');

    // Limpa os campos de endereço enquanto a busca é realizada
    enderecoInput.value = '';
    bairroInput.value = '';
    cidadeInput.value = '';
    estadoInput.value = '';

    let cep = cepInput.value.replace(/\D/g, ''); // Remove caracteres não numéricos do CEP

    // Verifica se o CEP tem 8 dígitos
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`) // Faz a requisição à API ViaCEP
            .then(response => response.json()) // Converte a resposta para JSON
            .then(data => {
                if (!data.erro) { // Verifica se a API retornou um erro
                    enderecoInput.value = data.logradouro;
                    bairroInput.value = data.bairro;
                    cidadeInput.value = data.localidade;
                    estadoInput.value = data.uf;
                } else {
                    alert('CEP não encontrado.');
                }
            })
            .catch(error => {
                console.error('Erro ao buscar CEP:', error);
                alert('Erro ao buscar CEP. Verifique sua conexão ou tente novamente.');
            });
    } else if (cep.length > 0) {
        alert('CEP inválido. Digite 8 dígitos.');
    }
}