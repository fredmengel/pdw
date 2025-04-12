from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir requisições do frontend

# Função para carregar os dados dos profissionais
def carregar_profissionais():
    with open('profissionais.json', encoding='utf-8') as f:
        return json.load(f)['profissionais']

@app.route('/profissionais', methods=['GET'])
def get_profissionais():
    profissionais = carregar_profissionais()
    especialidade = request.args.get('especialidade', '').lower()
    nome = request.args.get('nome', '').lower()

    resultado = [
        profissional for profissional in profissionais
        if (especialidade in profissional['especialidade'].lower() or not especialidade)
        and (nome in profissional['nome'].lower() or not nome)
    ]

    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True)


