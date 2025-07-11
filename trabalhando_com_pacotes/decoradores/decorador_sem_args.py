# decorador
def meu_decorador(funcao):
    def envolope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envolope

def ola_mundo():
    print("Olá mundo! ")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

# açucar sintatico - mesma coisa de antes porem usamos o @ e diminuimos as linhas
@meu_decorador
def ola_mundo():
    print("Olá mundo!")
