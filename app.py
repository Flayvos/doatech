
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = 'database.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        entrada = {
            'nome': request.form['nome'],
            'email': request.form['email'],
            'tipo': request.form['tipo'],
            'mensagem': request.form['mensagem']
        }
        dados = load_data()
        dados.append(entrada)
        save_data(dados)
        return redirect('/lista')
    return render_template('cadastrar.html')

@app.route('/lista')
def lista():
    dados = load_data()
    return render_template('lista.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
