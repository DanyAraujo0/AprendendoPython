class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"   
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Maria",1)
aluno2 = Estudante("Joao",2)
mostrar_valores(aluno1,aluno2)

aluno1.matricula = 3
mostrar_valores(aluno1,aluno2)

Estudante.escola = "Unileste"
aluno3 = Estudante("Pedro", 5)
mostrar_valores(aluno1,aluno2,aluno3)



