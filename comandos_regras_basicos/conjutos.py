# declarando um conjunto

numeros = set([1,2,3,2,3,4])
print(numeros)

letras = set("abacaxi")
print(letras)

linguagens = {"python","java","c","python","java"}
print(linguagens) # não pode confiar na ordem pois pode ser alterada

# para acessar os valores do conjunto é necessário criar uma lista

numeros = list(numeros)
print(numeros[0])

# usando o for

for linguagem in linguagens:
    print(linguagem)

# enumerate

for numero, numeros in enumerate (numeros):
    print(f"{numero}: {numeros}")

# Union - uni dois conjuntos

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

# intersection - compara pega os valores repitidos 

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

# difference - compara e pega os valores diferentes 

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# issubset - compara e retorna true se os valores pertencerem ao conjunto ou false se não

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b)) # os valores do conjunto a existem todos no conjunto b
print(conjunto_b.issubset(conjunto_a)) # porem os do b não existem todos no a

# isdisjoint - verifica se os conjuntos não se tocam ou seja se não a valores iguais nos dois conjuntos

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b)) # não possuem valores iguais
print(conjunto_a.isdisjoint(conjunto_c)) # 1 se repete nos dois conjuntos logo false

# add - adiciona valores no conjunto e ignora os repetidos
 
sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
print(sorteio)
sorteio.add(25) # sera ignorado pois ja existe no conjunto
print(sorteio)

# clear - limpa o conjunto

sorteio.clear()
print(sorteio)

# copy - gera uma copia

sorteio.add(25)
sorteio.add(42)
s2 = sorteio.copy()
print(sorteio)
print(s2)

# discard - discarta um valor do conjunto

sorteio.discard(42)
print(sorteio)

# pop - remove o primeiro valor adicionado no conjunto

numeros = {1,2,3,4,5,8,9,6}
print(numeros)
print(numeros.pop())

# remove - mesma coisa do discard porem quando o elemento não existe ele retorna error

numeros.remove(3)

# len - tamanho do conjunto

print(len(numeros))

# in - verifica se esta no conjunto

1 in numeros