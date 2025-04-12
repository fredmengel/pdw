from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def carregar_profissionais():
    with open('profissionais.json', encoding='utf-8') as f:
        return json.load(f)['profissionais']

@app.route('/profissionais', methods=['GET'])
def get_profissionais():
    profissionais = carregar_profissionais()
    especialidade = request.args.get('especialidade', '').lower()
    nome = request.args.get('nome', '').lower()

    resultado = [
        prof for prof in profissionais
        if (especialidade in prof['especialidade'].lower() or not especialidade)
        and (nome in prof['nome'].lower() or not nome)
    ]

    # Resposta com header CORS explícito
    response = make_response(jsonify(resultado), 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)



