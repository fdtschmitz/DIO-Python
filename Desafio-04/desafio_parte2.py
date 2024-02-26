"""
    Desafio de código do curso da DIO - Formação Python Developer:
    O objetivo deste código é integrar o código Python com MongoDB
"""
import pprint
import pymongo as pym
import datetime

secret = ".secrets.txt"

with open(secret, 'r') as file:
    secrets = file.read()

client = pym.MongoClient(secrets)

db = client.test

collections = db.new_collection
print((db.list_collection_names()))

# Definindo o formado do cadastro de cliente

clientes = [
    {
        "name": "Joao da Silva",
        "cpf": "123456789",
        "address": "Rua de cima, 12, Bairro, Cidade-UF",
        "agencia": "001",
        "conta": "000010",
        "tipo": "corrente",
        "date": datetime.datetime.utcnow()
    },
    {
        "name": "Joao da Silva",
        "cpf": "123456987",
        "address": "Rua do meio, 45, Bairro, Cidade-UF",
        "agencia": "001",
        "conta": "000020",
        "tipo": "corrente",
        "date": datetime.datetime.utcnow()
    },
    {
        "name": "Joao da Silva",
        "cpf": "321456789",
        "address": "Rua de baixo, 78, Bairro, Cidade-UF",
        "agencia": "001",
        "conta": "000030",
        "tipo": "corrente",
        "date": datetime.datetime.utcnow()
    }
]

result = collections.insert_many(clientes)
print(result.inserted_ids)

print("Recuperação geral de dados")
for post in collections.find():
    pprint.pprint(post)
