# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))


# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordem_pacientes(pacientes):
    ordenada = []

    for i, (nome, idade, status) in enumerate(pacientes):
        if status.strip().lower() == "urgente":
            prioridade = 0
        elif idade > 60:
            prioridade = 1
        else:
            prioridade = 2

        ordenada.append((prioridade, -idade, i, nome))

    ordenada.sort()
    return [item[3] for item in ordenada]


# TODO: Exiba a ordem de atendimento com título e vírgulas:

print("Ordem de Atendimento: " + ", ".join(ordem_pacientes(pacientes)))
