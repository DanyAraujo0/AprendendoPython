# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    
    posicao_virgula = linha.rfind(",")
    funcao = (linha[posicao_virgula + 1:])    
    participante = linha[:posicao_virgula]

    eventos.update({funcao:participante})


# Exibe os grupos organizados

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")