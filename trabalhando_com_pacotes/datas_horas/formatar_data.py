from datetime import datetime

data_atual = datetime.now()
mascara = '%d/%m/%Y %H:%M'

print(data_atual.strftime(mascara)) # usamos o strftime para formatar a string e passamos a mascara do padrao de exibicao
# print(data_atual.strftime('%d/%m/%Y')) # funciona tambem a aplicação direta

data = "2025-7-11 10:52"
data_convertida = datetime.strptime(data, '%Y-%m-%d %H:%M') # a mascara a ser passada deve estar no mesmo formato da variavel

print(data_convertida)
print(data_convertida.strftime(mascara)) # agora que virou data pode passar o strf
