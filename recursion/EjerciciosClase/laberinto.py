import numpy as np

class Laberinto:
    def __init__(self, size):
        self.forma = np.ones((size,size))
        self.posicion = 0,0
        self.forma[0,0] = 0

    def __str__(self):
        return str(self.forma)
    
    def avanzar(self, direccion: str):
        if direccion == "N":
            self.posicion = (self.posicion[0] - 1, self.posicion[1])
        elif direccion == "S":
            self.posicion = (self.posicion[0] + 1, self.posicion[1])
        elif direccion == "E":
            self.posicion = (self.posicion[0], self.posicion[1] - 1)
        elif direccion == "O":
            self.posicion = (self.posicion[0], self.posicion[1] + 1)
        self.forma[self.posicion] = 0

    
def trazar_camino(laberinto: Laberinto):
    pass
    #TODO: hacer copia, agregar checks en avanzar


if __name__ == "__main__":
    lab = Laberinto(10)
    print(lab)
    lab.avanzar("S")
    lab.avanzar("O")
    lab.avanzar("O")
    print(lab)