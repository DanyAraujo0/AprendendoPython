# decorador com argumentos

def meu_decorador(funcao):
    def envolope(*args,**kwargs):
        print("faz algo antes de executar")
        funcao(*args,**kwargs)
        print("faz algo depois de executar")

    return envolope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! {nome}")

ola_mundo("uai")