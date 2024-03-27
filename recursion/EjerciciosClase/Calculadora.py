class Calculadora:
    
    def __init__(self, a:int, b:int):  
        self.b = b
        self.a = a
    
    def suma(self) -> int:
        return a+b   
        
    def resta(self) -> int:
        return a-b   
    
    def multiplicacion(self) -> int:
        return a*b   
        
    def division(self) -> float:
        return a/b #TODO: hacer validacion   
            
if __name__ == "__main__":
    a = int(input("Ingrese el primer numero"))
    b = int(input("ingrese el sdo numero"))
    calc = Calculadora(a,b)
    print(calc.suma())
    print(calc.resta())        
    print(calc.multiplicacion())        
    print(calc.division())        
            
