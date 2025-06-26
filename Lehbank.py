##### Iniciando com as variaveis definidas ######
opcao = -1
limite = 500
saldo = 0
LIMITE_SAQUE = 3
valor_digitado = 0
deposito = 0

##### Listas criadas para guardar ações de saques e depositos ######
historico_saque = []
historico_deposito = []

###### Inicio do loop #######
while True:
    print("\n############### Lehbank ###############")
    print("[1] Deposito\n[2] Saque\n[3] Extrato\n[0] Sair\n")

    opcao = int(input())

    if opcao == 1:
        print("Insira um valor para deposito:")
        deposito = float(input("R$: "))

        if deposito > 0:
            saldo += deposito
            historico_deposito.append(deposito) #### Função para adicionar dados na lista criada anteriormente ####
            print("Deposito realizado com sucesso!\n")

        else:
            print("Informe um valor valido!")

#### Define regras e limites de saques #####
    elif opcao == 2:
        print("Digite o valor:")

        if len(historico_saque) >= LIMITE_SAQUE:
            print("Quantidade de saques diarios atingidos")

        else:
            valor_digitado = float(input("R$: "))

            if valor_digitado > saldo:
                print("Saldo insuficiente")

            elif valor_digitado > limite:
                print(f"Valor inserido excede ao limite diario de R${limite:.2f}")

            elif valor_digitado <= 0:
                print("Valor invalido!")
                
            else:
                saldo -= valor_digitado
                historico_saque.append(valor_digitado) #### Função para adicionar na lista criada anteriormente ####
                print("Saque realizado com sucesso!")

##### Exibe movimentações e saldo atual ######
    elif opcao == 3:
        print("############## EXTRATO ##############")
        print(f"Valor atual R$ {saldo:.2f}\n")
        print("############## Historico de Movimentações ##############\nDepositos realizados")
        print(historico_deposito)
        print("Valores sacados\n")
        print(historico_saque)

#### Opção que encerra o loop ####
    elif opcao == 0:
        print("Sessão finalizada com sucesso")
        break
    else:
        print("Opção invalida! Tente novamente.")