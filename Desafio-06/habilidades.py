from flask_restful import Resource
from flask import request
import json

habilidades = [
    {'id': 0,
     'habilidade': 'Python'},
    {'id': 1,
     'habilidade': 'Java'},
    {'id': 2,
     'habilidade': 'Flask'},
    {'id': 3,
     'habilidade': 'PHP'}
]


class Habilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(habilidades)
        dados['id'] = posicao
        habilidades.append(dados)


class UpdateHabilidades(Resource):
    def get(self, id):
        return habilidades[id]

    def put(self, id):
        dados = json.loads(request.data)
        habilidades[id] = dados
        return dados

    def delete(self, id):
        habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}
