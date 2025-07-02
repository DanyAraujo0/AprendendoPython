preco = 10
print(preco)
#ao converter é necessario escrever o tipo para conversao ex: int/float 
preco = float(preco)
print(preco)

preco = 11.20
print(preco)

preco = int(preco)
print(preco)

preco=10
print(preco/2)
#conversao por divisão
print(preco//2)

preco = 10.50
idade = 28
#numerico para string
print(str(preco))
print(str(idade))   

#concatenando usando uma variavel e {} 
texto = f"idade {idade} preco {preco}"
print(texto)

preco = "10.50"
idade = "28"
#numerico para string
print(float(preco))
print(int(idade))   

#erro na conversão
preco = "teste"
print(float(preco))