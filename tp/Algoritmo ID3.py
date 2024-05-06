'''
Definiciones:

Índice de Gini:
El índice de Gini es una medida de impureza utilizada en la construcción de árboles de decisión. 
Se calcula midiendo la probabilidad de que un elemento elegido al azar sea clasificado incorrectamente 
si se clasifica al azar de acuerdo con la distribución de las clases en un nodo. En otras palabras, 
cuanto menor sea el índice de Gini, mayor será la pureza del nodo, lo que significa que hay una predominancia 
de una sola clase en ese nodo. El índice de Gini varía entre 0 y 1, donde 0 indica que el nodo es completamente 
puro (todos los elementos pertenecen a la misma clase) y 1 indica que el nodo es completamente impuro 
(los elementos están distribuidos uniformemente entre las clases).

Entropía:
La entropía es otra medida de impureza utilizada en árboles de decisión. Se basa en la teoría de la 
información y mide la incertidumbre de una distribución de clases en un nodo. 
Cuanto mayor sea la entropía, mayor será la incertidumbre. En la práctica, se calcula la entropía 
como la suma de la probabilidad de cada clase multiplicada por el logaritmo de esa probabilidad. 
Un nodo con una entropía baja significa que está más ordenado en términos de clases, mientras que 
un nodo con una entropía alta significa que está más desordenado.

Ganancia de Información:
La ganancia de información se refiere a cuánta información se gana al dividir un conjunto de datos 
en base a una característica específica. En el contexto de la construcción de árboles de decisión, 
la ganancia de información se utiliza para seleccionar la mejor característica para dividir los 
datos en cada nodo del árbol. Se calcula como la diferencia entre la entropía (o el índice de Gini)
del nodo antes de la división y la ponderación promedio de la entropía (o el índice de Gini) de 
los nodos hijos después de la división. En pocas palabras, una mayor ganancia de información 
significa que la división de los datos en esa característica específica es más efectiva para 
reducir la incertidumbre en la clasificación de los datos.

En resumen, el índice de Gini, la entropía y la ganancia de información son medidas utilizadas en la 
construcción de árboles de decisión para evaluar la pureza de los nodos y seleccionar las mejores 
características para dividir los datos.

#----------------------

El algoritmo ID3

ID3 (Iterative Dichotomiser 3) es un algoritmo clásico para la construcción de árboles de decisión.

Inicio:
ID3 comienza con el conjunto de datos de entrenamiento y la lista de características disponibles.
Selección de la característica: El algoritmo selecciona la mejor característica para dividir los 
datos en el nodo actual del árbol. Utiliza la ganancia de información (o en ocasiones la ganancia 
normalizada de información) como medida para evaluar la importancia de cada característica. 
La característica con la mayor ganancia de información se selecciona como la mejor característica 
para dividir los datos.

División del conjunto de datos:

Se divide el conjunto de datos en subconjuntos basados en los valores posibles de la característica 
seleccionada en el paso anterior.

Recursión:
Se repiten los pasos 2 y 3 recursivamente en cada subconjunto de datos generado por la división 
hasta que se cumpla alguna condición de parada. Estas condiciones pueden incluir:

-Todos los elementos en el subconjunto pertenecen a la misma clase.
-No quedan características para dividir.
-El árbol alcanza una profundidad máxima predefinida.

Creación del árbol:
Se construye el árbol de decisión recursivamente mientras se realizan las divisiones basadas en 
la mejor característica en cada nodo.

Podado del árbol (opcional):
Después de que se construye el árbol, en algunos casos se puede realizar un proceso de poda para 
reducir el sobreajuste. Esto implica eliminar las ramas del árbol que no proporcionan una mejora 
significativa en la precisión de la clasificación.

Fin:
Se obtiene el árbol de decisión final que se puede utilizar para clasificar nuevos datos.
ID3 es un algoritmo simple y efectivo para la construcción de árboles de decisión, pero tiene 
algunas limitaciones. Por ejemplo, tiende a crear árboles demasiado profundos, lo que puede 
llevar al sobreajuste. Además, no maneja adecuadamente los atributos continuos y puede ser 
sensible al ruido en los datos. Sin embargo, sirve como una base sólida para algoritmos 
posteriores de árboles de decisión más avanzados, como C4.5 y CART.

# Implementacion ------------

Este código implementa un árbol de decisión usando el algoritmo ID3 para clasificación

Clase Node:
Esta clase representa un nodo en el árbol de decisión. Cada nodo puede tener una característica 
asociada (feature), un umbral de división (threshold) para características continuas, un valor 
de clase (value) si es una hoja, y referencias a sus subárboles izquierdo (left) y derecho (right).

Clase ID3DecisionTree:
Esta clase implementa el árbol de decisión utilizando el algoritmo ID3.

El método fit(X, y) toma los datos de entrada X y las etiquetas de clase y 
y construye el árbol de decisión utilizando la función _build_tree.
El método _build_tree(X, y) es una función recursiva que construye el árbol 
dividiendo recursivamente los datos en subconjuntos basados en las características 
y los valores de umbral.

El método _find_best_split(X, y) encuentra la mejor característica y umbral para 
dividir los datos en un nodo dado, maximizando la ganancia de información.

El método _information_gain(feature_column, y, threshold) calcula la ganancia de 
información al dividir los datos en dos conjuntos basados en un umbral específico 
para una característica.

El método _entropy(y) calcula la entropía de un conjunto de etiquetas de clase.

El método predict(X) toma datos de entrada X y devuelve las predicciones para cada 
instancia utilizando el árbol de decisión construido.

El método _traverse_tree(x, node) es una función recursiva que recorre el árbol de 
decisión para realizar predicciones en nuevas instancias.

Ejemplo de uso:

En el ejemplo de uso, se crean datos de entrenamiento X_train y etiquetas de clase y_train.
Se crea un objeto ID3DecisionTree llamado tree y se ajusta a los datos de entrenamiento.
Se crean datos de prueba X_test y se utilizan para hacer predicciones utilizando el método predict.
Las predicciones se imprimen en la pantalla.
'''

import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, value=None, left=None, right=None):
        self.feature = feature  # Índice de la característica utilizada para la división
        self.threshold = threshold  # Umbral para la división (solo para características continuas)
        self.value = value  # Valor de clase si el nodo es una hoja
        self.left = left  # Subárbol izquierdo
        self.right = right  # Subárbol derecho

class ID3DecisionTree:
    def __init__(self):
        self.root = None

    def fit(self, X, y):
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y):
        if len(set(y)) == 1:
            return Node(value=y[0])

        best_feature, best_threshold = self._find_best_split(X, y)
        left_indices = X[:, best_feature] < best_threshold
        right_indices = ~left_indices

        left_subtree = self._build_tree(X[left_indices], y[left_indices])
        right_subtree = self._build_tree(X[right_indices], y[right_indices])

        return Node(feature=best_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)

    def _find_best_split(self, X, y):
        best_gain = -1
        best_feature = None
        best_threshold = None

        for feature in range(X.shape[1]):
            values = sorted(set(X[:, feature]))
            thresholds = [(values[i] + values[i + 1]) / 2 for i in range(len(values) - 1)]

            for threshold in thresholds:
                gain = self._information_gain(X[:, feature], y, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _information_gain(self, feature_column, y, threshold):
        parent_entropy = self._entropy(y)

        left_indices = feature_column < threshold
        right_indices = ~left_indices

        if len(y[left_indices]) == 0 or len(y[right_indices]) == 0:
            return 0

        left_entropy = self._entropy(y[left_indices])
        right_entropy = self._entropy(y[right_indices])

        left_weight = len(y[left_indices]) / len(y)
        right_weight = len(y[right_indices]) / len(y)

        child_entropy = left_weight * left_entropy + right_weight * right_entropy

        return parent_entropy - child_entropy

    def _entropy(self, y):
        class_counts = Counter(y)
        probabilities = [class_count / len(y) for class_count in class_counts.values()]
        entropy = -sum(prob * np.log2(prob) for prob in probabilities)
        return entropy

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature] < node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)

# Ejemplo de uso
X_train = np.array([[2, 10], [3, 5], [5, 8], [6, 3], [7, 9]])
y_train = np.array([0, 1, 1, 0, 1])

tree = ID3DecisionTree()
tree.fit(X_train, y_train)

X_test = np.array([[4, 6], [1, 9]])
print("Predicciones:", tree.predict(X_test))
#------------------------------------------------------------------------

