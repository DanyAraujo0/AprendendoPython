saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saque>=1000:
    print("O limite para o saque é de 1000")

elif saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")    

#if condição; elif(else if) senão condição; else; senão
# !deve ser identado e : pontos    

#if alinhado é quando adicionamos varios if dentro de uma condição
if saldo >= 500:
    credito=float(input("Deseja um credito ate 100 na sua conta? Digite o valor: "))
    if credito >100:
        print("Não é possivel esse valor!")
    else:
        print("Será adicionado a conta!")
else:
    print("Adione mais saldo para ter credito")

#if ternario composto de 3 partes ou seja nele se a condicao for verdadeira ele retorna o valor antes 
# da condição senão for o valor apos o else

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")    
