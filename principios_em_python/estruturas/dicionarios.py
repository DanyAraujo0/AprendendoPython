# declarando dicionario - no dicionario a chave é imultavel

pessoa = {"nome": "Dany", "idade": 19}

pessoa = dict(nome="Dany", idade=19)

pessoa["telefone"] = "123456-9999"

# acessando os valores do dicionario

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

# sobreescrevendo o dicionario - é possivel alterar os valores do dicionario

pessoa["nome"] = "Danyelle"
print(pessoa["nome"])

# dicionario alinhado -

contatos = {
    "dany": {"nome": "Danyelle", "telefone": "3334-9999"},
    "teo": {"nome": "Teodoro", "telefone": "4444-9999"},
    "gabi": {"nome": "Gabriela", "telefone": "5555-9999"},
    "jao": {"nome": "João", "telefone": "6611-9999", "extra": {"a": 1}},
}

telefone = contatos["teo"]["telefone"]
print(telefone)

extra = contatos["jao"]["extra"]["a"]
print(extra)

# interar - mostrando todo o dicionario

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():  # lista de tuplas mais legivel
    print(chave, valor)
