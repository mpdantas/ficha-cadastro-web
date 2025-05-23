from flask import Flask, request, redirect, url_for, render_template, send_file
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from datetime import datetime # Importar a biblioteca datetime

app = Flask(__name__,
            static_folder=os.path.join('..', 'frontend'),
            static_url_path='/',
            template_folder=os.path.join('..', 'frontend'))
app.secret_key = 'chave_secreta_para_sessao'

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

@app.route('/ficha', methods=['GET', 'POST'])
def ficha():
    if request.method == 'POST':
        # --- Coleta e Formatação da Data de Nascimento ---
        data_nascimento_raw = request.form.get('dataNascimento')
        data_nascimento_formatada = ""
        if data_nascimento_raw:
            try:
                # Converte de YYYY-MM-DD (formato do input date) para objeto datetime
                data_obj = datetime.strptime(data_nascimento_raw, '%Y-%m-%d')
                # Converte objeto datetime para DD/MM/AAAA
                data_nascimento_formatada = data_obj.strftime('%d/%m/%Y')
            except ValueError:
                data_nascimento_formatada = "Formato inválido" # Ou deixar em branco, ou logar erro

        # Data de Preenchimento (já vem do JS no formato certo)
        data_preenchimento_raw = request.form.get('dataPreenchimento')
        data_preenchimento_formatada = data_preenchimento_raw # Assume que já está DD/MM/AAAA


        # --- Coletar TODOS os dados do formulário e montar o dicionário dados_ficha ---
        dados_ficha = {
            # Dados Pessoais
            'Nome': request.form.get('nome'),
            'CPF': request.form.get('cpf'),
            'CNH': request.form.get('cnh'),
            # 'Vencimento CNH' REMOVIDO AQUI
            'Data de Nascimento': data_nascimento_formatada, # Usar a data formatada
            'E-mail': request.form.get('email'),

            # Endereço
            'Endereço': request.form.get('endereco'),
            'CEP': request.form.get('cep'),
            'Bairro': request.form.get('bairro'),
            'Cidade': request.form.get('cidade'),
            'Estado': request.form.get('estado'),

            # Informações do Seguro
            'Modalidade do Seguro': request.form.get('modalidadeSeguro'),
            'Tipo do Seguro': request.form.get('tipoSeguro'),

            # Campos Específicos para Auto
            'Marca do Veículo': request.form.get('marcaAuto'),
            'Modelo do Veículo': request.form.get('modeloVeiculoAuto'),
            'Ano Fabricação': request.form.get('anoFabricacaoAuto'),
            'Ano Modelo': request.form.get('anoModeloAuto'),
            'Placa': request.form.get('placaAuto'),
            'Chassi': request.form.get('chassiAuto'),
            'Renavam': request.form.get('renavamAuto'),
            'Classe de Bônus': request.form.get('classeBonus'),

            # Informações Adicionais
            'Quem Indicou': request.form.get('indicacao'),
            'Data de Preenchimento': data_preenchimento_formatada, # Usar a data formatada
        }

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # --- Caminho para o Logo ---
        logo_path = os.path.join(app.root_path, '..', 'frontend', 'imagens', 'logo.png')
        logo_width = 50 # Ajuste a largura conforme necessário
        logo_height = 40 # Ajuste a altura conforme necessário
        logo_x = 50     # Posição X do canto inferior esquerdo do logo
        logo_y = height - 10 - logo_height - 10 # Posição Y (calculada abaixo do título)

        try:
            p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
        except Exception as e:
            print(f"Erro ao carregar o logo: {e}")
            print(f"Caminho do logo: {logo_path}")
            # Em caso de erro, continua sem o logo


        # --- Título Principal ---
        p.setFont("Helvetica-Bold", 24)
        title_y = height - 50
        p.drawCentredString(width / 2.0, title_y, "FICHA CADASTRAL")

        # --- Linha separadora ---
        line_y = title_y - 20
        p.line(50, line_y, width - 50, line_y)

        y_position = line_y - 30

        # --- Função auxiliar para adicionar blocos de texto ---
        def add_text_block(title, data_dict, start_y):
            nonlocal y_position
            y_position = start_y
            p.setFont("Helvetica-Bold", 14)
            p.drawString(50, y_position, title)
            y_position -= 20

            p.setFont("Helvetica", 11)
            current_x = 60

            for label, value in data_dict.items():
                if value:
                    p.drawString(current_x, y_position, f"{label}: {value}")
                    y_position -= 15
            y_position -= 20

        # --- Chamadas para adicionar os blocos de texto ---
        dados_pessoais_pdf = {
            'Nome': dados_ficha.get('Nome'),
            'CPF': dados_ficha.get('CPF'),
            'CNH': dados_ficha.get('CNH'),
            # 'Vencimento CNH' REMOVIDO AQUI DO DICIONÁRIO
            'Data de Nascimento': dados_ficha.get('Data de Nascimento'),
            'E-mail': dados_ficha.get('E-mail')
        }
        add_text_block("Dados Pessoais:", dados_pessoais_pdf, y_position)

        dados_endereco_pdf = {
            'Endereço': dados_ficha.get('Endereço'),
            'CEP': dados_ficha.get('CEP'),
            'Bairro': dados_ficha.get('Bairro'),
            'Cidade': dados_ficha.get('Cidade'),
            'Estado': dados_ficha.get('Estado')
        }
        add_text_block("Endereço:", dados_endereco_pdf, y_position)

        dados_seguro_pdf = {
            'Modalidade do Seguro': dados_ficha.get('Modalidade do Seguro'),
            'Tipo do Seguro': dados_ficha.get('Tipo do Seguro')
        }
        add_text_block("Informações do Seguro:", dados_seguro_pdf, y_position)

        if dados_ficha.get('Modalidade do Seguro') == 'auto':
            dados_auto_pdf = {
                'Marca do Veículo': dados_ficha.get('Marca do Veículo'),
                'Modelo do Veículo': dados_ficha.get('Modelo do Veículo'),
                'Ano Fabricação': dados_ficha.get('Ano Fabricação'),
                'Ano Modelo': dados_ficha.get('Ano Modelo'),
                'Placa': dados_ficha.get('Placa'),
                'Chassi': dados_ficha.get('Chassi'),
                'Renavam': dados_ficha.get('Renavam'),
                'Classe de Bônus': dados_ficha.get('Classe de Bônus')
            }
            add_text_block("Detalhes do Seguro Auto:", dados_auto_pdf, y_position)

        dados_adicionais_pdf = {
            'Quem Indicou': dados_ficha.get('Quem Indicou'),
            'Data de Preenchimento': dados_ficha.get('Data de Preenchimento')
        }
        add_text_block("Informações Adicionais:", dados_adicionais_pdf, y_position)

        # Rodapé do PDF
        p.setFont("Helvetica-Oblique", 9)
        p.drawCentredString(width / 2.0, 30, f"Gerado em {dados_ficha.get('Data de Preenchimento')} - Todos os direitos reservados.")

        p.showPage()
        p.save()

        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name='ficha_cadastro.pdf', mimetype='application/pdf')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)