from flask import Flask, request, render_template, redirect, jsonify, session
import mysql.connector

# A chave secreta é usada para assinar os cookies de sessão, garantindo que não possam ser falsificados ou manipulados por terceiros
app = Flask(__name__)

#
'''app.secret_key = 'teste'

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="dsa",
    database="meu_site"
)
cursor = conn.cursor()'''

# Rota para a página de login
@app.route('/')
def pagina_login():
    return render_template('formulario.html')

# Rota para verificar as credenciais de login e redirecionar para a página de formulário
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    data = request.json
    login = data['login']
    senha = data['senha']

    # Consulta SQL para verificar o login no banco de dados
    cursor.execute("SELECT * FROM usuarios WHERE login = %s AND senha = %s", (login, senha))
    usuario = cursor.fetchone()

    print(usuario)

    if usuario:
        usuario_id = usuario[0] 
        # Session o objeto é usado para armazenar dados de sessão do usuário entre solicitações
        session['usuario_id'] = usuario_id 
        return redirect(f'/formulario?usuario_id={usuario_id}')
    else:
        return jsonify({'mensagem': 'Login inválido'}), 401

# Rota para a página de formulário
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    data = request.json
    nome = data.get('nome')
    idade = data.get('idade')
    uf = data.get('uf')
    time_preferido = data.get('time_preferido')
    usuario_id = session['usuario_id']

    dados = (nome, idade, uf, time_preferido, usuario_id)
    print(dados)

    # Consulta SQL para inserir os dados no banco de dados
    cursor.execute("INSERT INTO formulario (id_usuario, nome, idade, uf, time_preferido) VALUES (%s, %s, %s, %s, %s)", (usuario_id, nome, idade, uf, time_preferido))
    conn.commit()

    # Redirecionar para a próxima página
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)    
