class Passaro:
    def voar(self):
        print("Voandoo")


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print(
            "Avestruz não voa"
        )  # aqui esta sobreescrevendo a função de voar da classe pai


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
