import requests
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from habilidades import Habilidades, UpdateHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Fernando',
        'habilidades': ['Python', 'Flash']
    },
    {
        'id': 1,
        'nome': 'Joseph',
        'habilidades': ['Python', 'Django']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}


class Lista_Devs(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Devs, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(UpdateHabilidades, '/habilidades/<int:id>')


@app.route('/')
def index():
    response = requests.get('http://127.0.0.1:5000/habilidades/')
    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    else:
        return 'Failed to fetch data from the API', 500


if __name__ == '__main__':
    app.run(debug=True)


