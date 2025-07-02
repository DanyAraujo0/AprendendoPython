# tipos de declaração de listas em python
frutas = ["laranja","maca","uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 42000000, 2020, 2900, "São Paulo", True]

# acessando os valores da lista

print(carro[0])
print(carro[-1]) #ultimo elemento da lista

# matriz
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[0])
print(matriz[0][1])
print(matriz[-1][-1]) #ultimo elemento da matriz

# fatiamento em listas
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

# usando o enumerate
for indice, carro in enumerate(carro):
    print(f"{indice}: {carro}")

# compressão de listas (criando uma lista a partir de outra)
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# pares = [numero in numeros if numero % 2 == 0] # funciona usando fltro em um linha
print(pares[::])

quadrado = []

for numero in numeros:
        quadrado.append(numero ** 2)

quadrado = [numero ** 2 for numero in numeros]

print(quadrado[::])

