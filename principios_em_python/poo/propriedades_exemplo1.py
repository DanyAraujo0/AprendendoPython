# o property permite o acesso direto a variavel privada sem a necessidade de passar metodos para isso
# setter serve para setar o valor parecido com o set
class Foo:
    def __init__(self,x=None):
        self._x = x
    
    @property # sem o property não seria possivel setar o valor na variavel
    def x(self):
        return self._x or 0 # não seria possivel retornar sem o property
     
    @x.setter # seria uma substituição para o medoto set
    def x(self,value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0 # ao inves de deletar passar 0 para a variavel faz mais sentido
    
foo = Foo(10)
print(foo.x)
# não seria possivel setar novamente mas poderia passar o valor e setar na variavel
foo.x = 10
print(foo.x)
# não é possivel deletar sem passar o deleter
del foo.x
print(foo.x)
