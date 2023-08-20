from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades_RESTful import *

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
        'nome': 'Kayque',
        'habilidades': ['Python', 'Flask', ]
     },
     {'id': 1,
        'nome': 'Morgan',
        'habilidades': ['Django', 'JavaScript']}
]

# Não precisa mais do jsonify, o RESTful manda convertido
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 
                        'mensagem': 'Desenvolvedor da ID não existe'}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = response = {'status': 'erro', 
                        'mensagem': mensagem}
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
        
    
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/<int:id>/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == "__main__":
    app.run()

