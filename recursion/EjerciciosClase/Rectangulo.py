class Rectangulo:
    def __init__(self, base:float, altura:float):
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
        return self.base * self.altura
    
    def calcular_perimetro(self) -> float:
        return (2*self.base)+(2*self.altura)

prueba = Rectangulo(5,3)
print(prueba.calcular_area())
print(prueba.calcular_perimetro())