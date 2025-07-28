# funcao interna
def funcao():
    print("Executando a funcao principal")

    def funcao_interna():
        print("Executando a funcao interna")

    def funcao2():
        print("Executando a funcao 2")

    funcao_interna()
    funcao2()


funcao()
# não é possivel chamar as funcoes internas de uma funcao principal fora de seu escopo
# funcao_interna()
