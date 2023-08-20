from flask_restful import Resource

habilidades = ['Python', 'Django', 'Java']
class Habilidades(Resource):
    def get(self):
        return habilidades