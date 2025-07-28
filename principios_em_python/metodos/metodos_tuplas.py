# count - contando os elementos da tupla

cores = (
    "azul",
    "amarelo",
    "roxo",
    "azul",
)
print(cores.count("azul"))
print(cores.count("roxo"))

# index - mostra o indice da variavel na lista

linguagens = (
    "python",
    "js",
    "c",
    "java",
    "java",
)
print(
    linguagens.index("java")
)  # so mostra a primeira ocorrencia mesmo com valores repetidos

# len - mostra a quantidade de elementos na lista

print(len(linguagens))

carros = "gol"
print(isinstance(carros, tuple))
