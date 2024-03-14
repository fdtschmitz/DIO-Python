from models import Pessoas, db_session


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


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta()
