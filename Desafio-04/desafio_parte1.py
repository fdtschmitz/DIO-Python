"""
    Desafio de código do curso da DIO - Formação Python Developer:
    O objetivo deste código é integrar o código Python com SQLite
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select


Base = declarative_base()


class Cliente(Base):
    """
        Esta classe implementa a tabela Cliente do esquema.
    """
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cpf = Column(String, unique=True, nullable=False)
    address = Column(String)


class Conta(Base):
    """
        Esta classe implementa a tabela Conta do esquema.
    """
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False)


# Criando conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Inspecionando o esquema do banco de dados
inspection = inspect(engine)

print(inspection.get_table_names())

# Populando o banco de dados

with Session(engine) as session:
    joao = Cliente(
        name='Joao da Silva',
        cpf='123456789',
        address='R da casa de cima, 75, Bairro - Cidade/UF'
    )

    jose = Cliente(
        name='José da Costa',
        cpf='987654321',
        address='Av do bairro, 45, Bairro - Cidade/UF'
    )

    maria = Cliente(
        name='Maria de Jesus',
        cpf='987321654',
        address='R do morro, 80, Bairro - Cidade/UF'
    )

    # Enviando para o banco de dados
    session.add_all([joao, jose, maria])
    session.commit()

# Visualizando dados persistidos
stmt = select(Cliente).where(Cliente.name.in_(['Joao da Silva']))
for cliente in session.scalars(stmt):
    print(cliente)

