# Dicionário com os valores de desconto
descontos = {"DESCONTO10": 0.10, "DESCONTO20": 0.20, "SEM_DESCONTO": 0.00}

# Entrada do usuário
preco = float(input("Digite o preço do produto: ").strip())
cupom = input("Digite o cupom para desconto: ").strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom in descontos:
    if cupom == "DESCONTO10":
        preco_final = preco - preco * 0.10
    elif cupom == "DESCONTO20":
        preco_final = preco - preco * 0.20
    elif cupom == "SEM_DESCONTO":
        preco_final = preco
else:
    print("Não foi possivel identificar o cupom")

print(f"O preco final é {preco_final:.2f}")
