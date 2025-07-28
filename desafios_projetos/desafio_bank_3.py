from abc import ABC, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo or 0

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self._saldo:
            print("Não é possível realizar saques sem saldo!")
            return False
        elif valor <= 0:
            ("Número de saques excedido! Não será possível realizar mais saques!")
            return False
        else:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Deposito realizado com sucesso! ===")
            return True
        else:
            print("Valor informado é inválido!")
            return False


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print(
                "\n Número de saques excedido! Não será possível realizar mais saques!"
            )
            return False

        if valor > self.limite:
            print(
                f"\nO limite por saque é de R$ {self.limite:.2f}! Não é possível realizar a operação."
            )
            return False

        saque_bem_sucedido = super().sacar(valor)

        if saque_bem_sucedido:
            self.numero_saques += 1

        return saque_bem_sucedido

    def __str__(self):
        return f"""\
            Agencia: {self.agencia}
            Conta: {self.numero}
            Titular: {self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionarTransacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class InterfaceTransacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    def registrar(self, conta):
        pass


class Deposito(InterfaceTransacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionarTransacao(self)


class Saque(InterfaceTransacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionarTransacao(self)


def exibir_menu():
    menu = """
    ------------------------
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [a] Adicionar cliente
        [c] Criar conta
        [l] Listar contas
        [q] Sair
    ------------------------
    """
    print(menu)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return None

    return cliente.contas[0]


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    conta = recuperar_conta_cliente(cliente)

    if cliente:
        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    conta = recuperar_conta_cliente(cliente)

    if cliente:
        valor = float(input("Informe o valor do deposito: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nO Cliente não foi encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\t\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("============================================")


def criar_cliente(clientes):
    cpf = input("Entre com o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(f"Existe um cliente com o cpf {cpf} ja cadastrado!")
        return
    else:
        nome = input("Informe o nome do novo cliente: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
        endereco = input("Informe o endereco: ")

        cliente = PessoaFisica(
            nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
        )

        clientes.append(cliente)

        print("Usuário criado com sucesso!!")


def criar_conta(clientes, numero_conta, contas):
    cpf = input("Entre com o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.adicionar_conta(conta)
        print("Conta criada com sucesso!!")

    else:
        print("Cliente não cadastrado faça o cadastro primeiro!!")


def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return

    for conta in contas:
        print("*" * 40)
        print(str(conta))
        print("*" * 40)


def main():
    clientes = []
    contas = []

    while True:
        exibir_menu()
        opcao = input("    =>")
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "q":
            break
        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(clientes, numero_conta, contas)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "a":
            criar_cliente(clientes)
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
