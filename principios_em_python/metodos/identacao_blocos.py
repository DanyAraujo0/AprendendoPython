def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa")

    print("Obrigado ")


def depositar(valor):
    saldo = 500
    saldo += valor

    print("O valor foi depositado")


sacar(500)

depositar(100)
