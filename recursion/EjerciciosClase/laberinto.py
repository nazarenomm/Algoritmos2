import numpy as np
from copy import deepcopy
import random

class Laberinto:
    def __init__(self, size):
        self.forma = np.ones((size,size))
        self.posicion = 0,0
        self.forma[0,0] = 0
        self.size = size

    def __str__(self):
        return str(self.forma)
    
    def __repr__(self) -> str:
        i = self.forma.size - np.count_nonzero(self.forma)
        return str(self)
    
    def hay_camino(self, direccion: str) -> bool:
        if direccion == "N":
            if self.posicion[0] == 0:
                return False
            else:
                return self.forma[self.posicion[0] - 1, self.posicion[1]] == 1
        elif direccion == "S":
            if self.posicion[0] == self.size - 1:
                return False
            else:
                return self.forma[self.posicion[0] + 1, self.posicion[1]] == 1
        elif direccion == "O": 
            if self.posicion[1] == 0:
                return False
            else:
                return self.forma[self.posicion[0], self.posicion[1] - 1] == 1
        elif direccion == "E":
            if self.posicion[1] == self.size - 1:
                return False
            else:
                return self.forma[self.posicion[0], self.posicion[1] + 1] == 1
        else:
            raise ValueError("Dirección inválida")
    
    def avanzar(self, direccion: str):
        if direccion == "N":
            self.posicion = (self.posicion[0] - 1, self.posicion[1])
        elif direccion == "S":
            self.posicion = (self.posicion[0] + 1, self.posicion[1])
        elif direccion == "E":
            self.posicion = (self.posicion[0], self.posicion[1] + 1)
        elif direccion == "O":
            self.posicion = (self.posicion[0], self.posicion[1] - 1)
        self.forma[self.posicion] = 0

    def trazar_camino(self) -> tuple["Laberinto", bool]:
        salida = (self.forma[self.size - 1, self.size - 1] == 0)
        if salida:
            return self, True
        else:
            salida_encontrada = False
            solucion = deepcopy(self)
            direcciones = ['N', 'S', 'O', 'E']
            while direcciones and not salida_encontrada:
                direccion = direcciones.pop(random.randint(0, len(direcciones) - 1))
                if self.hay_camino(direccion):
                    camino_actual = deepcopy(self)
                    camino_actual.avanzar(direccion)
                    solucion, salida_encontrada = camino_actual.trazar_camino()
                
            return solucion, salida_encontrada
                    
    def contar_caminos(self):
        pass
    

if __name__ == "__main__":
    lab = Laberinto(10)
    print(lab)
    print(lab.trazar_camino())