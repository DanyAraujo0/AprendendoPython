class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):  # sem o contrutor não iria iterar
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        # return StopIteration # parar o for


for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)

# para codigos mais complexos
