# tupla - é uma lista porem imutavel ou seja os valores não se alteram

frutas = (
    "laranja",
    "maca",
    "uva",
)  # definida com () e , no fim

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

print(frutas[0])
print(frutas[::])
print(frutas[:-1])

# matriz
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

print(matriz)

for indice, matriz in enumerate(matriz):
    print(f"{indice}: {matriz}")
