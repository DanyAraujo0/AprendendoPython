# passagem parametros
def mensagem(nome):
    print("execultando a mensagem")
    return f"Olá {nome}"

def mensagem_longa(nome):
    print("execultando a mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao):
    print("excutando excutar")
    return funcao("Dany")

print(executar(mensagem))
print(executar(mensagem_longa))