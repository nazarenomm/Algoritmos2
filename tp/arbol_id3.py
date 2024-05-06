from typing import Optional
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from copy import deepcopy

class Nodo:
    def __init__(self, data: pd.DataFrame, target: pd.Series) -> None: #data : data de entrenamiento
        self.atributo: Optional[str] = None # se setea cuando se haga un split
        self.categoria: Optional[str] = None # lo mismo
        self.data: pd.DataFrame = data
        self.target: pd.Series = target
        self.clase: Optional[str] = None # cuando sea hoja deberia tener la clase predicha
        self.si: Optional[ArbolID3] = None
        self.sd: Optional[ArbolID3] = None

    def split(self, atributo: str, categoria: str) -> None:
        nueva_data_si = self.data[self.data[atributo] == categoria]
        nueva_data_sd = self.data[self.data[atributo] != categoria]
        nueva_target_si = self.target[self.data[atributo] == categoria]
        nueva_target_sd = self.target[self.data[atributo] != categoria]
        nodo_izq = Nodo(nueva_data_si, nueva_target_si)
        nodo_der = Nodo(nueva_data_sd, nueva_target_sd)
        self.sd = ArbolID3(nodo_der)
        self.si = ArbolID3(nodo_izq)
        self.atributo = atributo
        self.categoria = categoria
    
    def entropia(self) -> float:
        entropia = 0
        proporciones = self.target.value_counts(normalize= True)
        target_categorias = self.target.unique()
        for c in target_categorias:
            proporcion = proporciones.get(c, 0)
            entropia += proporcion * np.log2(proporcion)
        return -entropia
    
class ArbolID3:
    def __init__(self, nodo: Nodo) -> None:
        self.raiz: Nodo = nodo

    @staticmethod
    def crear_arbol(df: pd.DataFrame, target: pd.Series):
        nodo = Nodo(df, target)
        return ArbolID3(nodo)
    
    def _mejor_split(self) -> tuple[str, str]:
        mejor_ig = -1
        mejor_atributo = None
        mejor_categoria = None
        atributos = self.raiz.data.columns

        for atributo in atributos:
            for categoria in self.raiz.data[atributo].unique():
                ig = self.information_gain(atributo, categoria)
                if ig > mejor_ig:
                    mejor_ig = ig
                    mejor_atributo = atributo
                    mejor_categoria = categoria
        
        return mejor_atributo, mejor_categoria

    def fit(self) -> None:
        if len(self.raiz.target.unique()) == 1:
            self.raiz.clase = self.raiz.target.value_counts().idxmax()
        else:
            mejor_atributo, mejor_categoria = self._mejor_split()
            self.raiz.split(mejor_atributo, mejor_categoria)
            self.raiz.si.fit()
            self.raiz.sd.fit()
        
    def information_gain(self, atributo: str, categoria: str) -> float:
        # recopilo informacion necesaria para el calculo
        entropia_actual = self.raiz.entropia()
        len_actual = len(self.raiz.data)

        information_gain = entropia_actual
        
        # hago el split:  "atributo = categoria ?"
        nuevo = deepcopy(self)
        nuevo.raiz.split(atributo, categoria)

        # calculo IG
        entropia_izq = nuevo.raiz.si.raiz.entropia()
        len_izq = len(nuevo.raiz.si.raiz.data)
        entropia_der = nuevo.raiz.sd.raiz.entropia()
        len_der = len(nuevo.raiz.sd.raiz.data)

        return information_gain - ((len_izq/len_actual)*entropia_izq + (len_der/len_actual)*entropia_der)
    
    def imprimir(self, prefijo: str = '  ', es_ultimo: bool = True, es_raiz: bool = True) -> None:
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

    # TODO
    def predict(self, X: pd.DataFrame):
        pass


if __name__ == "__main__":
    df = pd.read_csv("tp/play_tennis.csv", index_col=0)

    X = df.drop('play', axis=1)
    y = df['play'] 
    
    arbol = ArbolID3.crear_arbol(X, y)

    arbol.fit()

    arbol.imprimir()



