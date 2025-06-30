texto = input("Informe o texto: ")
vogais = "AEIOU"

#usando o for
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print("\n")

#range(stop) -> range object SERVE PARA LISTAR
# range(start, stop[, step]) -> range object
for numero in range(0, 11):
    print(numero, end=" ")

print("\n")

for numero in range(5, 51, 5):
    print(numero, end=" ")

print("\n")

#while
opcao = 10 
while opcao != 0:
    opcao = int(input("Informe a opcao(0-sair, 1-sacar, 2-depositar)"))
    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Depositando")
    elif opcao >2 or opcao<0:
        print("Opcao invalida")

print("\n")

#diferente de c++ e java aqui não tem do while
# mas tem o while true
while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break
    print(numero)

print("\n")

# podemos usar o continue que serve para pular, o break corta a execução do laço
for numero in range(50):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
