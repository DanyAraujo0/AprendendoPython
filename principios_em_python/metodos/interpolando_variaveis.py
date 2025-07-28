# old style %

nome = "Dany"
idade = 19
profissao = "Programadora"
linguagem = "Python"

pessoa = {
    "nome": "Dany",
    "idade": 19,
    "profissao": "Programadora",
    "linguagem": "Python",
}

print(
    "Olá me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s."
    % (nome, idade, profissao, linguagem)
)
# é necessário o uso de % e um prefixo para o tipo s-string d

# metodo format
print(
    "Olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format(
        nome, idade, profissao, linguagem
    )
)
# pode usar nomeando a ordem de cada variavel
print(
    "Olá me chamo {3}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculada no curso de {0}.".format(
        linguagem, idade, profissao, nome
    )
)
# passando variavel
print(
    "Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.".format(
        nome=nome, idade=idade, profissao=profissao, linguagem=linguagem
    )
)
# pode usar nomeando
print(
    "Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.".format(
        **pessoa
    )
)
# f string
print(
    f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}."
)

# formatando usando f-string
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")
