from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)

from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    relationship
)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    contas = relationship("Conta", back_populates="cliente")


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float, nullable=True)
    cliente = relationship("Cliente", back_populates="contas")


estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
estados_sudeste = ['ES', 'MG', 'RJ', 'SP']
estados_centro_oeste = ['DF', 'GO', 'MT', 'MS']
estados_sul = ['PR', 'SC', 'RS']
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']

engine = create_engine('sqlite:///cliente.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

cpf_input = input("CPF: ")
cliente = session.query(Cliente).filter_by(cpf=cpf_input).first()

if cliente:
    print("Cliente já cadastrado.")
else:
    nome = input("Nome: ")
    estado = input("Estado: ").upper()
    if estado not in estados_nordeste + estados_sudeste + estados_centro_oeste + estados_sul + estados_norte:
        print("Estado inexistente.")
    else:
        cliente = Cliente(nome=nome, cpf=cpf_input, estado=estado)
        session.add(cliente)
        session.commit()
        print(f"ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereco: {cliente.estado}.\n")

        while True:
            tipo = input("Tipo da conta (CORRENTE/POUPANÇA): ").upper()
            if tipo in ["CORRENTE", "POUPANÇA"]:
                break
            else:
                print("Escolha uma conta corrente ou poupança.")

        agencia = ""
        if estado in estados_nordeste:
            agencia = "12345"
        elif estado in estados_sul:
            agencia = "12346"
        elif estado in estados_norte:
            agencia = "12347"
        elif estado in estados_centro_oeste:
            agencia = "12348"
        elif estado in estados_sudeste:
            agencia = "12349"

        saldo = float(input("Saldo na conta:\n"))
        conta = Conta(tipo=tipo, agencia=agencia, id_cliente=cliente.id, saldo=saldo)
        session.add(conta)
        session.commit()

cliente = session.query(Cliente).filter_by(cpf=cpf_input).first()
contas = session.query(Conta).filter_by(id_cliente=cliente.id).all()

print(f"Cliente ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Estado: {cliente.estado}")
for conta in contas:
    print(f"Conta ID: {conta.id}, Tipo: {conta.tipo}, Agência: {conta.agencia}, Saldo: {conta.saldo}\n")

clientes = session.query(Cliente).all()
contas = session.query(Conta).all()
print("lista de clientes:")
for cliente in clientes:
    print(f"Cliente ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Estado: {cliente.estado}")
