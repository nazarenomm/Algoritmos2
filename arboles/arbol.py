from typing import Generic, Optional, TypeVar, Callable, Any
from functools import wraps

T = TypeVar("T") # se puede usar Any para que tome todo tipo de datos, lo ideal seria que NO
# nodo_num, nodo_cat, etc.

class Nodo(Generic[T]):
        def __init__(self, valor: T):
            self.valor = valor
            self.si: ArbolBinario[T] = ArbolBinario()
            self.sd: ArbolBinario[T] = ArbolBinario()

class ArbolBinario(Generic[T]):
    class Decoradores: #Completamente innecesario
        @classmethod
        def valida_no_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args, ** kwargs) -> Any:
                if self.es_vacio():
                    raise TypeError("Arbol Vacio")
                return f(self, *args, **kwargs)

            return wrapper
         
    def __init__(self):
        self.raiz: Optional[Nodo[T]] = None

    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinario[T]":
        nuevo_arbol = ArbolBinario()
        nuevo_arbol.raiz = Nodo(dato)
        return nuevo_arbol

    def es_vacio(self):
        return self.raiz is None
    
    @Decoradores.valida_no_es_vacio
    def si(self) -> "ArbolBinario[T]":
        return self.raiz.si
    
    @Decoradores.valida_no_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        return self.raiz.sd
    
    @Decoradores.valida_no_es_vacio
    def dato(self) -> T:
        return self.raiz.valor
    
    @Decoradores.valida_no_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        self.raiz.si = si

    @Decoradores.valida_no_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        self.raiz.sd = sd

    def set_raiz(self, dato: T):
        self.raiz = Nodo(dato)

    def altura(self) -> int:
        def _altura_recursiva(nodo: ArbolBinario[T]) -> int:
            if nodo.es_vacio():
                return 0
            else:
                return 1 + max(self.si().altura(), self.sd().altura())
        return _altura_recursiva(self)

    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            casos_previo = self.si().preorder() + self.sd().preorder()
            casos_previo.insert(0, self.dato())
            return casos_previo
        
    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            casos_previo = self.si().inorder()
            casos_previo.append(self.dato())
            return casos_previo + self.sd().inorder()
        
    def posorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().posorder() + self.sd().posorder() + [self.dato()]
        
    def bfs(self) -> list[T]:
        # si no arbol vacio
            # iterar hasta cola vacia, llamar bfs(cola)
            # desencolar
            # visito nodo actual, agregar a la lista/string
            # encolar si y sd
        def recorrido(q: list[ArbolBinario[T]], camino: list[T]) -> list[T]:
            if not q:
                return camino
            else:
                actual = q.pop(0) # desencolar
                if not actual.es_vacio():
                    camino.append(actual.dato()) # visito nodo actual, agregar a la lista/string
                    q.append(actual.si()) # encolar si
                    q.append(actual.sd()) # encolar sd
                return recorrido(q, camino)
            
        return recorrido([self], [])
            
    def __str__(self) -> str:
        def recorrer(t: ArbolBinario[T], nivel: int) -> str:
            tab = "." * 4 * nivel
            if t.es_vacio():
                return ""
            else:
                tab += str(t.dato()) + "\n"
                tab += recorrer(t.si(), nivel + 1)
                tab += recorrer(t.sd(), nivel + 1)
                return tab
            
        return recorrer(self, 0)
    
    def __len__(self) -> int:
        #return len(self.preorder())
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato()) #para profundo: self.dato().copy()
            nuevo.insertar_si(self.si().copy())
            nuevo.insertar_sd(self.sd().copy())
            return nuevo
        
    #TODO: armar arbol espejo, es un ejercicio de la guía

if __name__ == "__main__":
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n9 = ArbolBinario.crear_nodo(9)

    t.insertar_si(n2)
    t.insertar_sd(n3)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    n4.insertar_si(n8)
    n4.insertar_sd(n9)

    print(t)
    print("preorder: ", t.preorder())
    print("posorder: ", t.posorder())
    print("inorder: ", t.inorder())
    print("altura: ", t.altura())
    print("cantidad de nodos: ", len(t))

    t2 = t.copy()

    print("BFS: ", t.bfs())