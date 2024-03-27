class Vehiculo():
    def __init__(self, color):
        self.color = color
    
    def info(self):
        print("Color: ", self.color)
        

class Coche(Vehiculo):
    def __init__(self, color, marca):
        super().__init__(color)
        self.marca = marca
    
    def info(self):
        super().info()
        print("Marca: ", self.marca)
    
    
vehiculo = Vehiculo("Amarillo")
vehiculo.info()
coche = Coche("Verde", "Volkswagen")
coche.info()
