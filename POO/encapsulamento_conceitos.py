class Conta:
    def __init__(self,nro_agencia,saldo=0):
        self.nro_agencia = nro_agencia        
        self._saldo = saldo # o _ é usado para referenciar que aquele objeto é privado em python
    # um recurso privado só deveria ser acessado no escopo do metodo
    def depositar(self,valor): # metodo sacar publico por padrão
        pass

    def sacar(self,valor): 
        pass

    def mostrar_saldo(self): # por convenção é necessário passar um metodo para acessar a variavel privada
        return self._saldo
 
conta = Conta("0001", 100) # funciona mas não deveria pois é um recurso privado
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())