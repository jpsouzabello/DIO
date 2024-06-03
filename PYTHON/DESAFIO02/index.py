menu = """
1. Depositar
2. Sacar
3. Extrato
4. Cadastrar usuário
5. Criar conta corrente
6. Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas_correntes = []

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    cpf = int(input("Informe seu CPF: "))
    bairro, cidade = input("Digite seu bairro e cidade: ").split()
    moradia = f"Bairro: {bairro} | Cidade: {cidade}"
    
    if any(usuario['CPF'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado.")
        return usuarios
    
    usuario = {"Nome": nome, "Data de nascimento": data_nascimento, "CPF": cpf, "Moradia": moradia}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuarios

def criar_conta_corrente(contas_correntes, usuarios):    
    cpf = int(input("Informe seu CPF: "))
    
    usuario = next((usuario for usuario in usuarios if usuario['CPF'] == cpf), None)
    
    if usuario is None:
        print("Usuário não existente.")
        return contas_correntes
    
    numero_conta = len(contas_correntes) + 1
    conta_e_agencia = f"{numero_conta:04d}-0001"
    conta_corrente = {"Número da conta": conta_e_agencia, "Usuário": usuario}
    contas_correntes.append(conta_corrente)
    print(f"Conta corrente {conta_e_agencia} criada com sucesso!, usuário: {usuario}")
    return contas_correntes

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite=limite, 
            numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES
        )
    
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "5":
        contas_correntes = criar_conta_corrente(contas_correntes, usuarios)

    elif opcao == "6":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
