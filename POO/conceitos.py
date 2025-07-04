class Cachorro: # definindo uma classe para cachorro 
    def __init__(self, nome, cor, acordado = True): # constutor dos objetos
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def latir(self): # função da classe
        print("Aiiiih")

    def dormir(self): 
        self.acordado = False
        print("Ohhnzzzzz")

cao_1 = Cachorro("Domênica","caramelo",True) # definindo objetos

cao_1.latir() # chamando a função da classe
cao_1.dormir()
