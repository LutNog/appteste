from flask import Flask, request, redirect

app = Flask(__name__)

# Rota para a página de login
@app.route('/')
def pagina_login():
    return app.send_static_file('login.html')

# Rota para verificar as credenciais de login e redirecionar para a página de dados
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    # Verificar se o login e a senha estão corretos (simulação)
    if login == "1" and senha == "1":
        # Se o login for bem-sucedido, redirecionar para a próxima página
        return redirect('/formulario.html')
    else:
        # Se o login falhar, redirecionar de volta para a página de login
        return redirect('/')

# Rota para receber os dados via método GET e redirecionar para a próxima página
@app.route('/api/salvar-dados', methods=['GET'])
def salvar_dados():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    uf = request.args.get('uf')
    time_preferido = request.args.get('time_preferido')
    
    # Aqui você pode fazer o que quiser com os dados, como salvar em uma variável
    dados = {'nome': nome, 'idade': idade, 'uf': uf, 'time_preferido': time_preferido}
    print(dados)  # Exemplo de impressão dos dados
    
    # Redirecionar para a próxima página
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)   