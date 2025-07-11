# retorna funcao

def calculadora(operador):
    def soma(a,b):
        return a + b
    
    def sub(a,b):
        return a - b
    
    def mult(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    match operador:
        case "+":
            return soma
        
        case "-":
            return sub
        
        case "*":
            return mult
        case "/":
            return div
        
print(calculadora("+")(10,2))
print(calculadora("-")(10,2))
print(calculadora("*")(10,2))
print(calculadora("/")(10,2))