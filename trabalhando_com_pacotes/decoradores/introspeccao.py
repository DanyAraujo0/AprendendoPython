import functools # usamos para fazer a introspeccao ser correta

def meu_decorador(funcao):
    @functools.wraps(funcao) # passando o metodo
    def envolope(*args,**kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args,**kwargs)
        print("faz algo depois de executar")
        return resultado
    return envolope

@meu_decorador
def ola_mundo(nome, outro_arg):
    print(f"Olá mundo! {nome}")
    return nome.upper()

resultado = ola_mundo("uai",2)
print(resultado)

print(ola_mundo.__name__) # para verificar
