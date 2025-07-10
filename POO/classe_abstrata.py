from abc import ABC, abstractclassmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractclassmethod
    def ligar(self):
        pass
    
    @abstractclassmethod
    def desligar(self):
        pass

    @property
    @abstractproperty # para passar property
    def marca(self):
        pass

class ControleTV(ControleRemoto): 
    def ligar(self): # por a classe ser abstrada é necessario implementar os medotos dela
        print("Ligando")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando")
        print("TV desligada")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)