# Ficha de Cadastro de Cliente para Impressão

## Descrição do Projeto

Este projeto consiste em uma aplicação web que permite aos usuários da empresa preencherem uma ficha de cadastro de clientes com campos pré-definidos e gerar um arquivo para impressão em formato A4. A aplicação possui um sistema básico de controle de acesso via usuário e senha. Os dados preenchidos na ficha não são armazenados no sistema; o foco principal é a criação de uma ficha para impressão.

## Funcionalidades Principais

* **Página de Login:** Sistema de controle de acesso com nome de usuário e senha para usuários da empresa.
* **Ficha de Cadastro:**
    * Campos para dados pessoais: Nome, CPF, CNH (com campo de data de vencimento na mesma linha), Data de Nascimento, E-mail.
    * Campos para endereço: Endereço, CEP, Bairro, Cidade, Estado.
    * Seleção de Modalidade do Seguro através de um dropdown: Auto, Vida, Residência, Empresa, Equipamento portátil.
    * Campos dinâmicos específicos para cada modalidade de seguro (ex: Marca do Veículo, Modelo, Placa para Auto; Beneficiário para Vida, etc.) que aparecem ao selecionar a modalidade.
    * Seleção do Tipo do Seguro através de um dropdown: Seguro Novo, Renovação.
    * Campo para registrar quem indicou o cliente.
    * Data de preenchimento automática no dia do preenchimento.
* **Geração de PDF para Impressão:** Funcionalidade para gerar um arquivo PDF formatado para impressão em tamanho A4 com os dados preenchidos na ficha.
* **Botão de Sair:** Permite ao usuário deslogar do sistema e retornar à página de login.
* **Rodapé:** Exibe a mensagem de "Todos os direitos reservados" com o ano atualizado automaticamente.

## Tecnologias Utilizadas

**Front-end:**

* HTML5: Estrutura da página web.
* CSS3: Estilização da interface do usuário (arquivos `style.css` para estilos gerais e `login.css` para a página de login).
* JavaScript: Interatividade da página (mostrar/esconder campos dinâmicos, preenchimento automático da data, atualização do ano no rodapé, redirecionamento).

**Back-end:**

* Python: Linguagem de programação do lado do servidor (a lógica de autenticação e geração de PDF será implementada em Python com um framework como Flask ou Django - *ainda não implementado neste estágio*).

## Estrutura de Pastas
ficha-cadastro-web/
├── backend/
│   ├── init.py
│   └── ... (arquivos Python do backend - a serem implementados)
├── frontend/
│   ├── css/
│   │   ├── login.css
│   │   └── style.css
│   ├── images/
│   │   └── logo_empresa.png (coloque o logo da sua empresa aqui)
│   ├── js/
│   │   ├── login.js
│   │   └── script.js
│   ├── index.html
│   └── login.html
└── README.md


## Como Executar (Desenvolvimento Front-end)

1.  **Certifique-se de ter um navegador web instalado.**
2.  **Para visualizar as páginas:**
    * Abra o arquivo `frontend/index.html` ou `frontend/login.html` diretamente no seu navegador (dê um duplo clique no arquivo).
    * **Recomendado:** Utilize a extensão Live Server no Visual Studio Code (ou outro editor de código) para um desenvolvimento mais ágil com atualização automática do navegador. Basta abrir o arquivo HTML no VS Code e clicar com o botão direito, selecionando "Open with Live Server".

## Instruções de Uso (Front-end)

1.  **Acessar a Página de Login:** Abra o arquivo `login.html` no seu navegador.
2.  **Inserir Credenciais:** Digite o nome de usuário e a senha nos campos fornecidos (a autenticação real será implementada no backend).
3.  **Entrar no Sistema:** Clique no botão "Entrar". Você será redirecionado para a ficha de cadastro (`index.html`).
4.  **Preencher a Ficha de Cadastro:**
    * Preencha os campos de dados pessoais e endereço.
    * Selecione a "Modalidade do Seguro" no dropdown. Os campos específicos para a modalidade escolhida aparecerão.
    * Selecione o "Tipo do Seguro".
    * Preencha o campo "Quem indicou?".
    * A "Data de Preenchimento" será preenchida automaticamente.
5.  **Sair do Sistema:** Clique no botão "Sair" fixo no rodapé direito da página da ficha para retornar à página de login.
6.  **Gerar PDF:** Clique no botão "Gerar PDF para Impressão" para (futuramente) gerar o arquivo PDF com os dados preenchidos.

## Próximos Passos (Back-end - A Ser Implementado)

* **Implementação do Backend (Python):**
    * Configurar um framework web (Flask ou Django).
    * Criar rotas para `/login` e para servir a página da ficha.
    * Implementar a lógica de autenticação de usuários (verificação de credenciais).
    * Implementar a lógica para receber os dados da ficha e gerar o arquivo PDF para impressão (usando bibliotecas como `reportlab`).
* **Persistência de Usuários (Opcional):** Se necessário, configurar um banco de dados para armazenar as informações dos usuários da empresa.

## Considerações

* Este projeto foca na interface do usuário (front-end) e na estrutura básica para a funcionalidade de login e da ficha de cadastro. A lógica completa do back-end para autenticação e geração de PDF ainda precisa ser implementada.
* A estilização é básica e pode ser aprimorada para uma melhor experiência do usuário.
* A validação dos campos do formulário para garantir que os dados inseridos sejam válidos