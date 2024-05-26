from typing import Generic, Optional, TypeVar, Callable, Any 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.text import Annotation
from anytree import NodeMixin
class _MPLTreeExporter:
    def __init__(self, fontsize=None, x_step=0.5, y_step=0.3):
        self.fontsize = fontsize
        self.x_step = x_step  # Separación horizontal entre nodos
        self.y_step = y_step  # Separación vertical entre nodos
        self.characters = ["#", "[", "]", "<=", "\n", "", ""]
        self.bbox_args = dict()
        self.arrow_args = dict(arrowstyle="<-")

    def export(self, tree, ax=None):
        if ax is None:
            ax = plt.gca()
        ax.clear()
        ax.set_axis_off()
        self.recurse(tree.raiz, ax)

        anns = [ann for ann in ax.get_children() if isinstance(ann, Annotation)]

        if self.fontsize is None:
            renderer = ax.figure.canvas.get_renderer()
            for ann in anns:
                ann.update_bbox_position_size(renderer)
                size = ann.get_fontsize()
                ann.set_fontsize(size)

        return anns

    def recurse(self, node, ax, depth=0, y_pos=1.0, x_pos=0.5, sibling_count=1, sibling_index=0):
        kwargs = dict(
            bbox=self.bbox_args.copy(),
            ha="center",
            va="center",
            zorder=100 - 10 * depth,
            xycoords="axes fraction",
            arrowprops=self.arrow_args.copy(),
        )
        kwargs["arrowprops"]["edgecolor"] = plt.rcParams["text.color"]

        if self.fontsize is not None:
            kwargs["fontsize"] = self.fontsize

        xy = (x_pos + (sibling_index - (sibling_count - 1) / 2) * self.x_step, y_pos - depth * self.y_step)

        #if node.atributo is not None:
        rta = str(node.categoria) + "\n" if node.categoria else ""
        pregunta =  "\n" + str(node.atributo) + "?" if node.atributo else ""
        entropia = "Entropia: " + str(round(node.entropia(), 2)) + "\n"
        clase = "Clase: " + str(node.clase)
        texto = rta + entropia + clase + pregunta
        ax.annotate(texto, xy, **kwargs)
        for i, sub_node in enumerate(node.subs):
            self.recurse(
                sub_node.raiz,
                ax,
                depth=depth + 1,
                y_pos=y_pos,
                x_pos=x_pos,
                sibling_count=len(node.subs),
                sibling_index=i,
            )
    # elif node.clase is not None:
        #     ax.annotate("Clase: " + node.clase, xy, **kwargs)

class Nodo(NodeMixin):
    def __init__(self, data: pd.DataFrame, target: pd.Series) -> None:
        super().__init__()
        self.atributo: Optional[str] = None
        self.categoria: Optional[str] = None
        self.data: pd.DataFrame = data
        self.target: pd.Series = target
        self.clase: Optional[str] = None
        self.subs: list[ArbolID3] = []

    def split(self, atributo: str) -> None:
        self.atributo = atributo
        for categoria in self.data[atributo].unique():
            nueva_data = self.data[self.data[atributo] == categoria]
            nueva_data = nueva_data.drop(atributo, axis=1)
            nuevo_target = self.target[self.data[atributo] == categoria]
            nuevo = Nodo(nueva_data, nuevo_target)
            nuevo.categoria = categoria
            self.subs.append(ArbolID3(nuevo))

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
    

    def fit(self) -> None:
        if len(self.raiz.target.unique()) == 1 or len(self.raiz.data.columns) == 0:
            self.raiz.clase = self.raiz.target.value_counts().idxmax()
        else:
            mejor_atributo = self._mejor_split()
            self.raiz.split(mejor_atributo)
            [sub_arbol.fit() for sub_arbol in self.raiz.subs]

    def _mejor_split(self) -> str:
        mejor_ig = -1
        mejor_atributo = None
        atributos = self.raiz.data.columns

        for atributo in atributos:
            ig = self.information_gain(atributo)
            if ig > mejor_ig:
                mejor_ig = ig
                mejor_atributo = atributo
        
        return mejor_atributo

    def information_gain(self, atributo: str) -> float:
        entropia_actual = self.raiz.entropia()
        len_actual = len(self.raiz.data)

        nuevo = deepcopy(self)
        nuevo.raiz.split(atributo)

        entropias_subarboles = 0

        for subarbol in nuevo.raiz.subs:
            entropia = subarbol.raiz.entropia()
            len_subarbol = len(subarbol.raiz.data)
            entropias_subarboles += ((len_subarbol/len_actual)*entropia)

        information_gain = entropia_actual - entropias_subarboles
        return information_gain

    def imprimir(self, prefijo: str = '  ', es_ultimo: bool = True, es_raiz: bool = True) -> None:
        pass

    def predict(self, X: pd.DataFrame) -> list[str]:
        pass


# Uso:
df = pd.read_csv("tp/play_tennis.csv", index_col=0)  # tu conjunto de datos
target = df['play']  # columna objetivo
features = df.drop('play', axis=1)
arbol = ArbolID3.crear_arbol(features, target)
arbol.fit()

exportador = _MPLTreeExporter()
exportador.export(arbol)
plt.show()
