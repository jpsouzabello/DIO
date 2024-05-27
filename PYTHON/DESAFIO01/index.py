menu = '''

Escolha uma operação bancária para realizar:

1.Depositar
2.Sacar
3.Extrato
4.Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque_total = 0

while True:

    operacao = input(menu)
    print('\n')
    operacao_escolhida = operacao.title()

    if operacao_escolhida == "Depositar":
        deposito = float(input("Insira uma quantidade para depósito: "))
        print('\n')
        if deposito > 0:
            saldo += deposito
            print(f"Operação bem sucedida! Depósito de R${deposito} realizado.")
            extrato += f"Depósito de R${deposito}.\n"
            print(f"Agora sua conta tem R${saldo}")
        else:
            print("Não é possível depositar esse valor.")
    
    elif operacao_escolhida == "Sacar" and numero_saques < LIMITE_SAQUES and saque_total <= limite:
        saque = float(input("Informe o valor do saque: "))
        print('\n')
        if saque > limite or saque_total == limite:
            print("Não é permitido a realização de saques acima de R$ 500.00 diariamente.")
         
        elif saldo >= saque:    
            numero_saques +=1
            saque_total += saque
            saldo -= saque
            print(f"Operação bem sucedida! Saque de R${saque} realizado.")
            extrato += f"Saque de R${saque}.\n"
            print(f"Agora sua conta tem R${saldo}")
        
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    elif operacao_escolhida == "Extrato":
        print("Confira o extrato de sua conta:", end='\n')
        print(extrato, end='\n')
        print(f"Seu saldo atual é de {saldo}")
    
    elif operacao_escolhida == "Sair":
        break

    else:
        print("Operação inválida ou número máximo de saques já atendido.")

print("Volte sempre!")