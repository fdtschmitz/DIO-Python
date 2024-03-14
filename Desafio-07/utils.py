from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Adam', idade=25)
    print(pessoa)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Adam').first()
    #print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Adam').first()
    pessoa.idade = 34
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Adam').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('fdts', '123')
    insere_usuario('adam', '321')
    insere_usuario('tmt', '456')
    consulta_todos_usuarios()