class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        ano_atual = 2025
        return ano_atual - self._ano_nascimento

    def get_nome(self): # o property seria uma substituição apropriada para o get
        return self._nome
    
    def get_idade(self): # atraves do property é possivel acessar a variavel privada
        ano_atual = 2025
        return ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Dany",2005)
print(f"Nome: {pessoa.nome} \nIdade:{pessoa.idade}") 
print(f"Nome: {pessoa.get_nome} \nIdade:{pessoa.get_idade}") # como nas outras linguagens possuem o get e set
        