# tupla - é uma lista porem imutavel ou seja os valores não se alteram

frutas = ("laranja","maca","uva",) # definida com () e , no fim

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

print(frutas[0])
print(frutas[::])
print(frutas[:-1])

# matriz
matriz = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
)

print(matriz)

for indice, matriz in enumerate (matriz):
    print(f"{indice}: {matriz}")

# count - contando os elementos da tupla

cores = ("azul","amarelo","roxo","azul",)
print(cores.count("azul"))
print(cores.count("roxo"))

# index - mostra o indice da variavel na lista

linguagens = ("python", "js", "c","java","java",)
print(linguagens.index("java")) #so mostra a primeira ocorrencia mesmo com valores repetidos

# len - mostra a quantidade de elementos na lista

print(len(linguagens))

carros = ("gol")
print(isinstance(carros, tuple))