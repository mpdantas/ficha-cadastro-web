from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__,
            static_folder=os.path.join('..', 'frontend'),  # Define a pasta para arquivos estáticos
            static_url_path='/',  # Define a URL para acessar os arquivos estáticos
            template_folder=os.path.join('..', 'frontend')) # Define a pasta para os templates HTML
app.secret_key = 'chave_secreta_para_sessao'  # Substitua por uma chave secreta forte em produção

# Usuários (simulação - para fins de teste apenas.  Use um banco de dados e hash de senha em produção)
users = {
    'empresa': 'senha123'
}

@app.route('/')
def index():
    """
    Rota para a página inicial.  Redireciona para a página de login.
    """
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Rota para a página de login.
    Se a requisição for GET, exibe o formulário de login.
    Se a requisição for POST, processa o login.
    """
    error = None  # Inicializa a variável de erro
    if request.method == 'POST':
        username = request.form.get('username')  # Obtém o nome de usuário do formulário
        password = request.form.get('password')  # Obtém a senha do formulário
        if username in users and users[username] == password:
            # Autenticação bem-sucedida - redireciona para a ficha de cadastro
            return redirect(url_for('ficha'))
        else:
            # Falha na autenticação - define a mensagem de erro
            error = 'Nome de usuário ou senha incorretos'
    return render_template('login.html', error=error)  # Renderiza o template de login, passando o erro (se houver)

@app.route('/ficha')
def ficha():
    """
    Rota para a página da ficha de cadastro.
    Renderiza o arquivo index.html.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask