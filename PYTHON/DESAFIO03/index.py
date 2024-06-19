from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo = float(saldo)
        self.numero = int(numero)
        self.agencia = int(agencia)
        self.cliente = cliente
        self.historico = Historico()
        
    def saldo_conta(self):
        return self.saldo 

    def nova_conta(self, novo_cliente, novo_numero):
        self.cliente = novo_cliente
        self.numero = novo_numero 
        return novo_cliente, novo_numero 

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            print("Saldo insuficiente para saque.")
            return False
        elif valor_saque <= 0:
            print("Operação inválida.")
        else:
            self.saldo -= valor_saque
            saque = Saque(valor_saque)
            saque.registrar_transacao(self)
            return True
    
    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        deposito = Deposito(valor_deposito)
        deposito.registrar_transacao(self)
        return True
    
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite_valor_saque, limite_saques):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite_valor_saque = limite_valor_saque
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor_saque):
        if self.saques_realizados >= self.limite_saques:
            print("Número máximo de saques excedido.")
            return False
        if valor_saque > self.limite_valor_saque:
            print(f"Valor do saque excede o limite de R$ {self.limite_valor_saque:.2f}.")
            return False
        if super().sacar(valor_saque):
            self.saques_realizados += 1
            return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar_transacao(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar_transacao(self, conta):
        conta.historico.adicionar_transacao(f"Depósito de R$ {self.valor:.2f}")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar_transacao(self, conta):
        conta.historico.adicionar_transacao(f"Saque de R$ {self.valor:.2f}")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        if isinstance(transacao, Deposito):
            conta.depositar(transacao.valor)
        elif isinstance(transacao, Saque):
            conta.sacar(transacao.valor)
        else:
            print("Tipo de transação inválido.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

menu = """\n
    ================ MENU ================
    [t]\tTransação
    [h]\tHistórico
    [nc]\tNova conta
    [lc]\tListar contas
    [u]\tUsuário
    [q]\tSair
    => """

menu_transacao = """\n
    ================ MENU ================
    [s]\tSaque
    [d]\tDepósito
    [q]\tSair
    => """

menu_cadastro = """\n
    ================ MENU ================
    [s]\tSim
    [n]\tNão
    => """

def filtrar_usuario(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def main():
    clientes = []
    while True:
        print("Escolha uma operação:")
        operacao = input(menu)

        if operacao == "t":
            cpf = input("Digite seu CPF:")
            usuario = filtrar_usuario(cpf, clientes)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            numero_conta = int(input("Digite o número da conta:"))
            conta = next((conta for conta in usuario.contas if conta.numero == numero_conta), None)
            if not conta:
                print("Conta não encontrada.")
                continue

            print("Escolha uma operação:")
            operacao_transacao = input(menu_transacao)    
            if operacao_transacao == "s":
                valor = float(input("Digite um valor de saque:"))
                if conta.sacar(valor):
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {conta.saldo:.2f}.")
                else:
                    print("Saque não realizado.")

            elif operacao_transacao == "d":
                valor = float(input("Digite um valor de depósito:"))
                if valor > 0:
                    conta.depositar(valor)
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {conta.saldo:.2f}.")
                else:
                    print("Valor de depósito inválido.")
                
            elif operacao_transacao == "q":
                continue
                
            else:
                print("Operação inválida.")

        elif operacao == "h":
            cpf = input("Digite seu CPF:")
            usuario = filtrar_usuario(cpf, clientes)
            if usuario:
                numero_conta = int(input("Digite o número da conta:"))
                conta = next((conta for conta in usuario.contas if conta.numero == numero_conta), None)
                if conta:
                    print("Histórico de transações:")
                    for transacao in conta.historico.transacoes:
                        print(transacao)
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")

        elif operacao == "nc":
            cpf = input("Digite seu CPF:")
            usuario = filtrar_usuario(cpf, clientes)
            if usuario:
                numero_conta = max((conta.numero for conta in usuario.contas), default=0) + 1
                nova_conta = ContaCorrente(0.0, numero_conta, 123, usuario, 500.0, 3)
                usuario.adicionar_conta(nova_conta)
                print(f"Nova conta criada com sucesso! Número da conta {numero_conta}.")
            else:
                print("Usuário não encontrado. Favor criar um novo usuário.")

        elif operacao == "lc":
            cpf = input("Digite seu CPF:")
            usuario = filtrar_usuario(cpf, clientes)
            if usuario:
                print(f"Contas do cliente {usuario.nome} (CPF: {usuario.cpf})")
                for conta in usuario.contas:
                    print(f"Número da conta: {conta.numero}, Agência: {conta.agencia}, Saldo: R$ {conta.saldo:.2f}")
            else:
                print("Cliente não encontrado.")
            
        elif operacao == "u":
            cpf = input("Digite seu CPF:")
            usuario = filtrar_usuario(cpf, clientes)
            if usuario:
                print(f"Nome: {usuario.nome}")
                print(f"CPF: {usuario.cpf}")
            else: 
                print("Usuário não encontrado. Deseja realizar seu cadastro?")
                cadastro = input(menu_cadastro)
                if cadastro == "s":
                    nome = input("Digite seu nome:")
                    cpf = input("Digite seu CPF:")
                    nova_pessoa = PessoaFisica(nome, cpf)
                    clientes.append(nova_pessoa)
                    print("Cadastro realizado com sucesso!")
                elif cadastro == "n":
                    print("Operação cancelada.")
                else:
                    print("Valor inválido.")
            
        elif operacao == "q":
            break

        else:
            print("Operação inválida.")

main()
