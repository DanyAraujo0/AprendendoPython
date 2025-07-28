def exibir_menu():
    menu = """
    ------------------------
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Criar usuário
        [c] Criar conta
        [l] Listar dados
        [q] Sair
    ------------------------
    """
    print(menu)


def sacar(*, saldo, LIMITE_SAQUES, numero_saques, extrato, limite):
    if saldo <= 0:
        print("Não é possível realizar saques sem saldo!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número de saques excedido! Não será possível realizar mais saques!")
    else:
        valor = float(input("Informe o valor para o saque: "))
        if valor > saldo:
            print("Saldo insuficiente! Não é possível realizar o saque")
        elif valor > limite:
            print(
                "O limite por saque é de R$ {limite}}! Não é possível realizar o saque"
            )
        elif valor <= 0:
            print("Valor inválido! Não é possível realizar o saque")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação bem sucedida!")


def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor para o depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Operação bem sucedida!")
    else:
        print("Valor informado é inválido!")


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================================")


def criar_usuario(usuarios):
    cpf = int(input("Entre com o CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f"Existe um usuário com o cpf {cpf} ja cadastrado!")
        return
    else:
        nome = input("Informe o nome do novo usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
        endereco = input("Informe o endereco: ")

        usuarios.append(
            {
                "cpf": cpf,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco,
            }
        )

        print("Usuário criado com sucesso!!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(usuarios, numero_conta, AGENCIA, contas):
    cpf = int(input("Entre com o CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        contas.append(
            {
                "cpf": cpf,
                "agencia": AGENCIA,
                "numero_conta": numero_conta,
                "usuario": usuario,
            }
        )
        print("Conta criada com sucesso!!")
        return
    else:
        print("Usuário não cadastrado faça o cadastro primeiro!!")
        criar_usuario(usuarios)


def listar_dados(contas):
    for conta in contas:
        linha = f"""\
            ****************************************
            Agência: {conta['agencia']}
            Número conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            Data de Nascimento: {conta['usuario']['data_nascimento']}
            Endereço: {conta['usuario']['endereco']}
            ****************************************
        """
        print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        exibir_menu()
        opcao = input("    =>")
        if opcao == "d":
            depositar(saldo, extrato)
        elif opcao == "s":
            sacar(
                saldo=saldo,
                LIMITE_SAQUES=LIMITE_SAQUES,
                numero_saques=numero_saques,
                extrato=extrato,
                limite=limite,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break
        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(usuarios, numero_conta, AGENCIA, contas)
        elif opcao == "l":
            listar_dados(contas)
        elif opcao == "u":
            criar_usuario(usuarios)
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
