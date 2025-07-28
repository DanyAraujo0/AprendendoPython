texto = "PyThOn"
print(texto.upper())
print(texto.lower())
print(texto.title())
# upper = deixa tudo maiusculo
# lower = deixa tudo minusculo
# title = deixa a primeira letra maiuscula

texto = "   Olá Mundo!!!        "
print(texto)
print(texto.strip(), ".")
print(texto.lstrip(), ".")
print(texto.rstrip(), ".")
# strip = retira todos espaços em vazio
# lstrip =  retira o espaço em vazio no inicio
# rstrip = retira o espaço em vazio no fim

texto = "Danyelle"
print(texto.center(10, "#"))
print(".".join(texto))
print(texto.center(10, "#"))
# center = centraliza a palavra com numero de caracteres e o algorismo que vai substituir os espaços vazios
# join = apos cada letra é adicionado um o ponto
