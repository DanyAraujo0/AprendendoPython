class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Prim,prim")
    
    def parar(self):
        print("Parando a Biscreta.....")
        print("Biscreta parada!!")

    def correr(self):
        print("Vrummmm")

b1 = Bicicleta("preta", "caloi",2022,650)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)