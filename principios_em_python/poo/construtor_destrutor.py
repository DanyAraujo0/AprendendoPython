class Cachorro: # definindo uma classe para cachorro 
    def __init__(self, nome, cor, acordado = True): # constutor dos objetos
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        print("Incializando a classe...")

    def __del__(self):
        print("Removendo a instancia da classe")

    def latir(self): 
        print("Aiiiih")

    def dormir(self): 
        self.acordado = False
        print("Ohhnzzzzz")

cao_1 = Cachorro("Domênica","caramelo",True)

cao_1.latir()
cao_1.dormir()

del cao_1

cao_2 = Cachorro("Zenitsu","Amarelo",False)

cao_2.latir()