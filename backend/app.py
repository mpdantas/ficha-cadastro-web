from flask import Flask, request, redirect, url_for, render_template, send_file
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__,
            static_folder=os.path.join('..', 'frontend'),
            static_url_path='/',
            template_folder=os.path.join('..', 'frontend'))
app.secret_key = 'chave_secreta_para_sessao' # Substitua por uma chave segura

users = {
    'empresa': 'senha123'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return redirect(url_for('ficha'))
        else:
            error = 'Nome de usuário ou senha incorretos'
    return render_template('login.html', error=error)

@app.route('/ficha', methods=['GET', 'POST']) # Adicionar 'POST' para receber dados do formulário
def ficha():
    if request.method == 'POST':
        # Coletar dados do formulário
        dados_ficha = {
            'nome': request.form.get('nome'),
            'cpf': request.form.get('cpf'),
            'cnh': request.form.get('cnh'),
            'vencimentoCNH': request.form.get('vencimentoCNH'), # Se você o manteve no HTML
            'dataNascimento': request.form.get('dataNascimento'),
            'email': request.form.get('email'),
            'endereco': request.form.get('endereco'),
            'cep': request.form.get('cep'),
            'bairro': request.form.get('bairro'),
            'cidade': request.form.get('cidade'),
            'estado': request.form.get('estado'),
            'modalidadeSeguro': request.form.get('modalidadeSeguro'),
            'tipoSeguro': request.form.get('tipoSeguro'),
            'indicacao': request.form.get('indicacao'),
            'dataPreenchimento': request.form.get('dataPreenchimento'),
            # Adicione aqui os campos específicos de cada modalidade de seguro
            # Exemplo para Auto:
            'marcaAuto': request.form.get('marcaAuto'),
            'modeloAuto': request.form.get('modeloAuto'),
            'anoFabricacaoAuto': request.form.get('anoFabricacaoAuto'),
            'anoModeloAuto': request.form.get('anoModeloAuto'),
            'placaAuto': request.form.get('placaAuto'),
            'chassiAuto': request.form.get('chassiAuto'),
            'renavamAuto': request.form.get('renavamAuto'),
            # ... outros campos ...
        }

        # Criar o PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # Definir uma fonte e tamanho para o título
        p.setFont("Helvetica-Bold", 18)
        p.drawString(50, height - 50, "FICHA DE CADASTRO DE CLIENTE")

        # Definir fonte e tamanho para o conteúdo
        p.setFont("Helvetica", 12)
        y_pos = height - 100 # Posição Y inicial para o conteúdo

        # Adicionar dados ao PDF
        for key, value in dados_ficha.items():
            if value: # Apenas adicione se o valor não for vazio
                p.drawString(50, y_pos, f"{key.replace('_', ' ').title()}: {value}")
                y_pos -= 15 # Mover para a próxima linha

        p.showPage() # Finaliza a página
        p.save() # Salva o conteúdo no buffer

        buffer.seek(0) # Retorna ao início do buffer
        return send_file(buffer, as_attachment=True, download_name='ficha_cadastro.pdf', mimetype='application/pdf')

    # Se a requisição for GET, apenas renderiza o formulário (como antes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)