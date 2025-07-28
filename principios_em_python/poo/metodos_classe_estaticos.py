class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, dia, mes, ano, nome):  # função de fabrica
        idade = 2025 - ano
        return cls(nome, idade)

    # um metodo de classe recebe um primeiro parametro que aponta para a classe, enquanto o estatico não
    # ele pode acessar ou modificar o estado da classe, enquanto o estatico não pode nem acessar ou modificar
    # usado em metodos de fabrica

    @staticmethod
    def maior_idade(idade):
        return idade > 18


# um metodo estatico não recebe um primeiro argumento explicito ele é vinculado a classe não aos objetos dela
# usado em funções unitarias

p = Pessoa.criar_data_nascimento(8, 12, 2005, "Dany")
print(p.nome, p.idade)

print(Pessoa.maior_idade(15))
print(Pessoa.maior_idade(80))
