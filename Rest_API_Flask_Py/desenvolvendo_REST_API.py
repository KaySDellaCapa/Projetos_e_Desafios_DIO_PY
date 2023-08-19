from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0,
        'nome': 'Kayque',
        'habilidades': ['Python', 'Flask', ]
     },
     {'id': 1,
        'nome': 'Morgan',
        'habilidades': ['Django', 'JavaScript']}
]

# Devolve um dev pela ID. Também altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 
                        'mensagem': 'Desenvolvedor da ID não existe'}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = response = {'status': 'erro', 
                        'mensagem': mensagem}
        
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)

# Lista dos dev e inlui novo dev. Permite registrar
@app.route('/dev/', methods=('GET', 'POST'))
def lista_desenvolvedores(dados):
    if request.method == 'POST':
        dados == json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({desenvolvedores[posicao]})


if __name__ == '__main__':
    app.run(debug=True)