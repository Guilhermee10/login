from flask import Flask
from flask import render_template, redirect, request
from flask import flash
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = "GuilhermeEBAC"


@app.route("/")
def home():
    return render_template("login.html")
@app.route("/login", methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuarios.json') as tempuser:
        users = json.load(tempuser)

        for user in users:
            if user['nome'] == nome and user['senha'] == senha:
                return render_template('usuarios.html')

    flash('Usuário inválido')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)