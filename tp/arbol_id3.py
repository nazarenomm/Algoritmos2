from typing import Optional
import pandas as pd
import numpy as np
from copy import deepcopy

class Data:
    def __init__(self, df: pd.DataFrame, target: str) -> None:
        self.df: pd.DataFrame = df
        self.target: str = target
    
    def filtrar(self, atributo: str, valor: str, igual: bool = True) -> "Data":
        if igual:
            nuevo_df = df[df[atributo] == valor]
        else:
            nuevo_df = df[df[atributo] != valor]
        return Data(nuevo_df, self.target)
        
    def entropia(self) -> float:
        entropia = 0
        proporciones = self.df[self.target].value_counts(normalize= True)
        target_categorias = self.df[self.target].unique()
        for c in target_categorias:
            proporcion = proporciones.get(c, 0)
            entropia += proporcion * np.log2(proporcion)
        return -entropia

class Nodo:
    def __init__(self, data: Data) -> None: #data : data de entrenamiento
        self.atributo: Optional[str] = None # se setea cuando se haga un split
        self.categoria: Optional[str] = None# lo mismo
        self.data: Data = data
        self.si: Optional[ArbolID3] = None
        self.sd: Optional[ArbolID3] = None

    def split(self, atributo: str, categoria: str) -> "Nodo":
        nuevo = deepcopy(self) # hacer copy propio
        nueva_data_si = self.data.filtrar(atributo, categoria)
        nueva_data_sd = self.data.filtrar(atributo, categoria, False)
        nodo_izq = Nodo(nueva_data_si)
        nodo_der = Nodo(nueva_data_sd)
        nuevo.sd = ArbolID3(nodo_der)
        nuevo.si = ArbolID3(nodo_izq)
        nuevo.atributo = atributo
        nuevo.categoria = categoria
        return nuevo
    
    
class ArbolID3:
    def __init__(self, nodo: Nodo) -> None:
        self.raiz: Nodo = nodo

    @staticmethod
    def crear_arbol(df: pd.DataFrame, target: str):
        data = Data(df, target)
        nodo = Nodo(data)
        return ArbolID3(nodo)

    def fit(self, df: pd.DataFrame, target: str) -> "ArbolID3": # construye el arbol (?)
        data = Data(df, target)
        pass
        # decido cual va a ser atributo y su valor por el que splitear y guardo el atributo como raiz
        # hago el split con ese atributo y valor (categoria)
        # repito recursivamente

    # podria ser helper de fit o split
    def information_gain(self, atributo: str, categoria: str) -> float:
        # recopilo informacion necesaria para el calculo
        entropia_actual = self.raiz.data.entropia()
        len_actual = len(self.raiz.data.df)

        information_gain = entropia_actual
        
        # hago el split por el atributo
        nodo = self.raiz.split(atributo, categoria)

        # calculo IG (horrible)
        entropia_izq = nodo.si.raiz.data.entropia()
        len_izq = len(nodo.si.raiz.data.df)
        entropia_der = nodo.sd.raiz.data.entropia()
        len_der = len(nodo.sd.raiz.data.df)

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

if __name__ == "__main__":
    df = pd.read_csv("tp/play_tennis.csv")
    print(df.head())

    arbol = ArbolID3.crear_arbol(df, "play")

    print(f"entropia inicial: {arbol.raiz.data.entropia()}")

    print(f"information gain de splitear por {"wind = Weak ?"} : {arbol.information_gain("wind", "Weak")}")
