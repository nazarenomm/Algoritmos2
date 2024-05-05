from typing import Optional
import pandas as pd
import numpy as np
from copy import deepcopy

class Nodo:
    def __init__(self, data: pd.DataFrame, target: str) -> None: #data : data de entrenamiento
        self.atributo: Optional[str] = None # se setea cuando se haga un split
        self.categoria: Optional[str] = None # lo mismo
        self.data: pd.DataFrame = data
        self.target: str = target
        self.clase: Optional[str] = None # cuando sea hoja deberia tener la clase predicha
        self.si: Optional[ArbolID3] = None
        self.sd: Optional[ArbolID3] = None

    def split(self, atributo: str, categoria: str) -> None:
        # nuevo = deepcopy(self) # TODO: copy propio
        nueva_data_si = self.data[self.data[atributo] == categoria]
        nueva_data_sd = self.data[self.data[atributo] != categoria]
        nodo_izq = Nodo(nueva_data_si, self.target)
        nodo_der = Nodo(nueva_data_sd, self.target)
        self.sd = ArbolID3(nodo_der)
        self.si = ArbolID3(nodo_izq)
        self.atributo = atributo
        self.categoria = categoria
    
    def entropia(self) -> float:
        entropia = 0
        proporciones = self.data[self.target].value_counts(normalize= True)
        target_categorias = self.data[self.target].unique()
        for c in target_categorias:
            proporcion = proporciones.get(c, 0)
            entropia += proporcion * np.log2(proporcion)
        return -entropia
    
class ArbolID3:
    def __init__(self, nodo: Nodo) -> None:
        self.raiz: Nodo = nodo

    # solo para probar metodos
    @staticmethod
    def crear_arbol(df: pd.DataFrame, target: str):
        nodo = Nodo(df, target)
        return ArbolID3(nodo)

    def fit(self, df: pd.DataFrame, target: str) -> "ArbolID3": # construye el arbol (?)
        pass
        # decido cual va a ser atributo y su valor por el que splitear y guardo el atributo como raiz
        # hago el split con ese atributo y valor (categoria)
        # repito recursivamente

    # podria ser helper de fit o split
    def information_gain(self, atributo: str, categoria: str) -> float:
        # recopilo informacion necesaria para el calculo
        entropia_actual = self.raiz.entropia()
        len_actual = len(self.raiz.data)

        information_gain = entropia_actual
        
        # hago el split:  "atributo = categoria ?"
        nuevo = deepcopy(self)
        nuevo.raiz.split(atributo, categoria)

        # calculo IG (horrible)
        entropia_izq = nuevo.raiz.si.raiz.entropia()
        len_izq = len(nuevo.raiz.si.raiz.data)
        entropia_der = nuevo.raiz.sd.raiz.entropia()
        len_der = len(nuevo.raiz.sd.raiz.data)

        return information_gain - ((len_izq/len_actual)*entropia_izq + (len_der/len_actual)*entropia_der)
    
    def es_vacio(self) -> bool:
        return self.raiz is None
    
    def insertar_si(self,si:"ArbolID3") -> None:
        if self.es_vacio():
            raise TypeError("Arbol vacio")
        self.raiz.si = si
    
    def insertar_sd(self,sd:"ArbolID3") -> None:
        if self.es_vacio():
            raise TypeError("Arbol vacio")
        self.raiz.sd = sd

    def imprimir(self, prefijo='  ', es_ultimo=True, es_raiz= True):
        nodo = self.raiz
        simbolo_rama = '└─no── ' if es_ultimo else '├─si── '
        if es_raiz:
            print(str(nodo.atributo) + " = " + str(nodo.categoria) + "?")
            nodo.si.imprimir(prefijo, False, False)
            nodo.sd.imprimir(prefijo, True, False)
        elif nodo.atributo is not None:
            print(prefijo + simbolo_rama + str(nodo.atributo) + " = " + str(nodo.categoria) + "?")
            prefijo += ' '*10 if es_ultimo else '│' + ' '*9
            nodo.si.imprimir(prefijo, False, False)
            nodo.sd.imprimir(prefijo, True, False)
        else:
            print(prefijo + simbolo_rama + 'Clase:', str(nodo.clase))


if __name__ == "__main__":
    df = pd.read_csv("tp/play_tennis.csv")
    print(df.head())
    print("\n")

    arbol = ArbolID3.crear_arbol(df, target= "play")

    print(f"entropia inicial: {arbol.raiz.entropia()}")
    print("\n")

    print(f"information gain de splitear por {"wind = Weak ?"} : {arbol.information_gain("wind", "Weak")}")
    print("\n")

    arbol.raiz.split("wind", "Weak")

    print(f"data del subarbol izquierdo luego del split (casos positivos):\n {arbol.raiz.si.raiz.data}")
    
    
    print(f"\ndata del subarbol derecho (casos negativos):\n {arbol.raiz.sd.raiz.data}")
    print("\n")

    arbol.raiz.si.raiz.split("outlook", "Sunny")
    arbol.raiz.sd.raiz.split("temp", "Mild")

    arbol.imprimir()
