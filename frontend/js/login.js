// frontend/js/login.js
function atualizarAnoRodapeLogin() {
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        const anoAtual = new Date().getFullYear();
        console.log("Ano atual (login.js):", anoAtual); // Para depuração
        currentYearSpan.textContent = anoAtual;
    } else {
        console.log("Elemento currentYear não encontrado (login.js)."); // Para depuração
    }
}

// Chama a função para atualizar o ano do rodapé quando a página carregar
window.onload = atualizarAnoRodapeLogin;