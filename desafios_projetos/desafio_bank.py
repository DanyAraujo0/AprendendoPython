menu = """
------------------------
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para o depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Operação bem sucedida!")
        else:
            print("Valor informado é inválido!")
    elif opcao == "s":
        if saldo <= 0:
            print("Não é possível realizar saques sem saldo!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedido! Não será possível realizar mais saques!")
        else:
            valor = float(input("Informe o valor para o saque: "))
            if valor > saldo:
                print("Saldo insuficiente! Não é possível realizar o saque")
            elif valor > limite:
                print(
                    "O limite por saque é de R$ {limite}}! Não é possível realizar o saque"
                )
            elif valor <= 0:
                print("Valor inválido! Não é possível realizar o saque")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Operação bem sucedida!")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
