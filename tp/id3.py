import pandas as pd
import numpy as np
from copy import deepcopy

class Dataset(): # innecesario
    def __init__(self, df: pd.DataFrame, target: str):
        self.df: pd.DataFrame = df
        self.target: str = target
        self.target_categorias = df[target].unique()
    
    def entropy(self):
        entropia = 0
        proporciones = self.df[self.target].value_counts(normalize= True)
        for c in self.target_categorias:
            proporcion = proporciones.get(c, 0)
            entropia += proporcion * np.log2(proporcion)
        return -entropia
    
    @property
    def columnas(self):
        return self.df.columns
    
    def __len__(self):
        return len(self.df)
    
    def get_categorias(self, feature: str):
        return self.df[feature].unique()
    
    def filtrar(self, feature: str, valor: str) -> "Dataset":
        nuevo = Dataset(self.df[self.df[feature] == valor], self.target)
        return nuevo
    
class ArbolID3():
    def __init__(self, datos: Dataset):
        self._datos: Dataset = datos
        self._subarboles: list[ArbolID3] = []

    def split(self, feature: str) -> "ArbolID3":
        nuevo = deepcopy(self) # hacer copy propio
        categorias = self.datos.get_categorias(feature)
        for c in categorias:
            subset = nuevo.datos.filtrar(feature, c)
            subarbol = ArbolID3(subset)
            nuevo.insertar_subarbol(subarbol)
        return nuevo

    def information_gain(self, feature: str) -> float:
        # recopilo informacion necesaria para el calculo
        entropia_actual = self.datos.entropy()
        information_gain = entropia_actual
        len_actual = len(self.datos)

        # hago el split por el feature
        nuevo_arbol = self.split(feature)

        # calculo IG
        for subarbol in nuevo_arbol.subarboles:
            entropia_subset = subarbol.datos.entropy()
            len_subset = len(subarbol.datos)
            information_gain -= (len_subset/len_actual) * entropia_subset

        return information_gain

    # del repo de arbol n-ario:
    @property
    def datos(self) -> Dataset:
        return self._datos

    @datos.setter
    def dato(self, valor: Dataset):
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
    
    dataset = Dataset(df, "play")

    print(f"entropia inicial: {dataset.entropy()}")

    arbol = ArbolID3(dataset)

    print(f"information gain de splitear por wind: {arbol.information_gain("wind")}") 
