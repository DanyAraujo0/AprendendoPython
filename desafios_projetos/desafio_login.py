# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:
if usuario in usuarios:
    if senha in usuarios[usuario]:
        print("Acesso permitido")
    else:
        print("Usuário ou senha incorretos")
else:
    print("Usuário ou senha incorretos")
