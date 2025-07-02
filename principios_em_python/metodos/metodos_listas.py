lista = []

# append - atribui valores para  a lista existente

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

# copy - copia os valores de uma lista para outra sem alterar nenhum valor 

l2 = lista.copy()
print(lista)
print(l2)
l2[0] = 5
print(l2)

# extend - adiciona um lista com novos valores no fim na lista juntando

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java","csharp", "python", "c"])

print(linguagens)

# index - mostra o indice da variavel na lista

print(linguagens.index("java")) #so mostra a primeira ocorrencia mesmo com valores repetidos
print(linguagens.index("python"))

# pop - tira o ultimo elemento adicionado

linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(0) # pode passar o indice para retirada tbm
print(linguagens)

# remove - remove o objeto da lista

linguagens.remove("js") # é passado o valor que deseja retirar ao inves do indice
print(linguagens) # remove apenas a primeira ocorrencia

# reverse - inverte a lista ao contrario

linguagens.reverse()
print(linguagens)

# sort - ordena a lista se string em ordem alfabetica

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True) # ordena em decrescente em ordem alfabetica
print(linguagens)

linguagens.sort(key=lambda x:len(x)) # ordena por tamanho da palavra (quantidade de letras)
print(linguagens)

linguagens.sort(key=lambda x:len(x), reverse=True) # ordena decrescente ao tamanho da palavra
print(linguagens)

# len - mostra a quantidade de elementos na lista

print(len(linguagens))

# sorted - mesma coisa que o sort porem é uma função e deve ser usada dentro de um print

print(sorted(linguagens, key=lambda x:len(x), reverse=True))

num = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 

print(num)