email = input("Digite o email: ").strip()

regras = ["gmail.com", "outlook.com"]
arroba = "@"

if email[0] == "@":
    print("E-mail inválido")
elif arroba not in email:
    print("E-mail inválido")
elif " " in email:
    print("E-mail inválido")
else:
    for dominio in regras:
        if dominio in email:
            verifica = True
            break
        else:
            verifica = False
    if verifica:
        print("E-mail válido")
    else:
        print("E-mail inválido")
