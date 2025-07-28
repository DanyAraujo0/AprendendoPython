# em python usa def para referenciar uma função


def exibir_mensagem():
    print("Hello World!")


exibir_mensagem()


def exibir_nome(nome):  # passando uma variavel
    print(f"Olá sou {nome}")


exibir_nome("Dany")  # passando um parametro para a variavel

# funções podem retornar valores


def calcular_total(numeros):
    return sum(numeros)


print(f"O total é: {calcular_total([150,31,559,10])}")

# passando varias variaveis


def exibir_pessoa(nome, idade, estado, altura):
    print("====== Dados do atleta ======")
    print(f"Nome: {nome}\n Idade:{idade}\n Estado:{estado}\n Altura:{altura}")
    print("=============================")


exibir_pessoa("Teo", 20, "MG", 1.82)
# mais legivel pois não corre o risco de passar argumentos para variaveis erradas
exibir_pessoa(nome="Paulo", altura=1.88, idade=22, estado="SP")

# * args - passa valores para uma tupla, ** kwargs - passa os valores para um dicionario
exibir_pessoa(*{"nome": "Paulo", "altura": 1.88, "idade": 22, "estado": "SP"})
exibir_pessoa(**{"nome": "Paulo", "altura": 1.88, "idade": 22, "estado": "SP"})


# passando a parametros por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(
    "Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina"
)
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# passando por nome
def criar_carro(modelo, ano, placa, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
criar_carro(
    modelo="Palio",
    ano=1999,
    placa="ABC-1234",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina",
)  # inválido


# hibrido
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# variaveis globais
salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(150))
