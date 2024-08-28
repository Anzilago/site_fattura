from flask import Flask, render_template, url_for
#render_temlate apenas retorna o arquivo HTML..
#URL_FOR posso usar dentro das rotas dizendo pra pegar o link da função "X"

app = Flask(__name__)

lista_usuarios = ['Lira', 'Amanda', 'Henrique', 'Ariane', 'Arthur']

@app.route('/')#somente a barra pois quero dizer que é homepage, se tivesse algo depois da barra seria pra lear a outra pagina
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)
#o parametro posso colocar qual nome, convem colocar o msm nome da variavel que quer pegar

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__': #só executa se estiver rodando o arquivo direto, importando não roda! testes coloca aqui abaixo
    app.run(debug=True) #app.run para rodar o site 
    # DEBUG=TRUE dizendo que vou debugar o site nao preciso ficar rodando para atuaizar minhas alterações