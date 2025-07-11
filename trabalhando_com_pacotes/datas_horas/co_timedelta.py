from datetime import date, datetime, timedelta

# o timedelta é usado para diferença entre horarios

tipo_carro = "P"
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now() # utc now serve pra qualquer localidade do usuario

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f"O carro chegou às {data_atual} e ficara pronto ás {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f"O carro chegou às {data_atual} e ficara pronto ás {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f"O carro chegou às {data_atual} e ficara pronto ás {data_estimada}")