from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    nome = "Você sabe..."
    dadosDic = {"chave":"valor","chave2":"valor2",}
    return render_template('index.html', nome = nome, dados = dadosDic)

@app.route('/contato')
def contato():
    return render_template('contato.html')
