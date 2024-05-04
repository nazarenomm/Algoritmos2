import pandas as pd
import numpy as np
from copy import deepcopy

class ArbolID3():
    def __init__(self, datos: pd.DataFrame, target: str):
        self._datos: pd.DataFrame = datos
        self.target: str = target
        self._subarboles: list[ArbolID3] = []

    def entropy(self):
        entropia = 0
        proporciones = self.datos[self.target].value_counts(normalize= True)
        target_categorias = self.datos[self.target].unique()
        for c in target_categorias:
            proporcion = proporciones.get(c, 0)
            entropia += proporcion * np.log2(proporcion)
        return -entropia

    def split(self, feature: str) -> "ArbolID3":
        nuevo = deepcopy(self) # hacer copy propio
        categorias = self.datos[feature].unique()
        for c in categorias:
            subset = nuevo.datos[nuevo.datos[feature] == c]
            subarbol = ArbolID3(subset, nuevo.target)
            nuevo.insertar_subarbol(subarbol)
        return nuevo

    def information_gain(self, feature: str) -> float:
        # recopilo informacion necesaria para el calculo
        entropia_actual = self.entropy()
        information_gain = entropia_actual
        len_actual = len(self.datos)

        # hago el split por el feature
        nuevo_arbol = self.split(feature)

        # calculo IG
        for subarbol in nuevo_arbol.subarboles:
            entropia_subset = subarbol.entropy()
            len_subset = len(subarbol.datos)
            information_gain -= (len_subset/len_actual) * entropia_subset

        return information_gain

    # del repo de arbol n-ario:
    @property
    def datos(self) -> pd.DataFrame:
        return self._datos

    @datos.setter
    def dato(self, valor: pd.DataFrame):
        self._dato = valor

    @property
    def subarboles(self) -> list["ArbolID3"]:
        return self._subarboles

    @subarboles.setter
    def subarboles(self, subarboles: list["ArbolID3"]):
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: "ArbolID3"):
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        altura_actual = 0
        for subarbol in self.subarboles:
            altura_actual = max(altura_actual, subarbol.altura())
        return altura_actual + 1
        
    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])
    
if __name__ == "__main__":
    
    df = pd.read_csv("tp/play_tennis.csv", index_col= 0)
    
    arbol = ArbolID3(df, "play")

    print(f"entropia inicial: {arbol.entropy()}")

    print(f"information gain de splitear por wind: {arbol.information_gain("wind")}") 
