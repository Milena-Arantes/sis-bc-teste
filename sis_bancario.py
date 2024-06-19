#deposito
#saque
#extrato
saque = []
deposito = []
saldo = 0
limite_saque = 3
acao = 1

while acao != 0:

    opcao = int(input(f'''      Seja Bem-Vindo(a)!
        O que deseja fazer?
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [0] - Sair
        Escolha uma opção: '''))

#DEPÓSITO
    if opcao == 1:
        print("Você escolheu: Depósito")
        while True:
            valor_dep = float(input("Insira o valor que você deseja depositar: "))
            deposito.append(valor_dep)
            saldo += valor_dep
            resp = input("Deseja fazer um novo depósito? Digite 's' para 'Sim' e 'n' para 'Não': ")
            if resp.lower() == 'n':
                break
    
#SAQUE
    elif opcao == 2:
        print("Você escolheu: Saque")
        if len(saque) >= limite_saque:
            print(f"Você excedeu o limite de {limite_saque} saques diários. Não é possível sacar.")
        else:
            while len(saque) < limite_saque:
                valor_saq = float(input("Insira o valor que deseja sacar: "))
                if valor_saq > saldo:
                    print("Valor excede o valor do saldo. Não é possível sacar.")
                elif valor_saq > 500:
                    print("Valor excede o limite de saque. Não é possível sacar.")
                else:
                    saque.append(valor_saq)
                    saldo -= valor_saq
                    print(f"Saque de R${valor_saq:.2f} realizado com sucesso.")
                if len(saque) >= limite_saque:
                    print(f"Você excedeu o limite de {limite_saque} saques diários. Não é possível sacar.")
                    break
                resp = input("Deseja fazer um novo saque? Digite 's' para 'Sim' e 'n' para 'Não': ")
                if resp.lower() == 'n':
                    break

#EXTRATO
    elif opcao == 3:
        print("Você escolheu: Extrato")
        resp = "0"
        print(f'''
        Depósitos: {deposito}
        Saques: {saque}
        Saldo atual: {saldo}''')
    
    elif opcao == 0:
        print("Saindo do sistema.")
        break

    else:
        print("Opção não existe, tente novamente")
        
