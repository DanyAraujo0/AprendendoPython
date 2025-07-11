def meu_gerador(numeros: list[int]):
    # contador += 1
    # yield numeros[contador] * 2
    for numero in numeros:
        yield numero * 2 # A função armazena o estado atual e retorna um valor, pausando sua execução até a próxima chamada.

    # texto = "Python"
    # yield texto # é necessario passar yield para o gerador iterar

for i in meu_gerador(numeros=[1,5,9]):
    print(i)

# a diferença é que o gerador é usado passando item a item de forma simples