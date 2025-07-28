# clear - limpa né
contatos = {
    "dany": {"nome": "Danyelle", "telefone": "3334-9999"},
    "teo": {"nome": "Teodoro", "telefone": "4444-9999"},
    "gabi": {"nome": "Gabriela", "telefone": "5555-9999"},
    "jao": {"nome": "João", "telefone": "6611-9999", "extra": {"a": 1}},
}

contatos.clear()
print(contatos)

# copy - copia né fi

contatos = {
    "dany": {"nome": "Danyelle", "telefone": "3334-9999"},
    "teo": {"nome": "Teodoro", "telefone": "4444-9999"},
    "gabi": {"nome": "Gabriela", "telefone": "5555-9999"},
    "jao": {"nome": "João", "telefone": "6611-9999", "extra": {"a": 1}},
}

copia = contatos.copy()
print(copia)

# fromkey - cria as chaves do dicionario

dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

# get - usado para acessar chaves do dicionario

# print(contatos("leo")) # a chave não existe logo retorna error
print(
    contatos.get("leo", {})
)  # a chave não existe e é ignorada , mas foi passado retorno de {}
print(contatos.get("dany"))

# keys - retorna apenas as chaves do dicionario

print(contatos.keys())

# pop - usado para remover caso não tenha certeza se o valor esta no dicionario pois nao retorna error

print(contatos.pop("leo", {}))

# popitem - retira os itens em sequencia o ultimo adicionado

print(contatos.popitem())

# setdefault - adiciona campos chaves caso não existentes

contatos.setdefault("idade", 19)
print(contatos)

# update - atualiza e adiciona campos chaves não existentes

contatos.update({"jao": {"nome": "João", "telefone": "6611-9999"}})
print(contatos)

# values - retorna todos os valores existentes no dicionario

print(contatos.values())

# in - verifica se valor existe no dicionario

result = "dany" in contatos
print(result)
result = "leo" in contatos
print(result)
result = "idade" in contatos["gabi"]
print(result)

# del - remove valores do dicionario

del contatos["gabi"]
print(contatos)
