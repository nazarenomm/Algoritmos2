from typing import Generic, Optional, TypeVar
T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor
        self.izquierda: Optional[T] = None
        self.derecha: Optional[T]= None

    def __str__(self):
        return str(self.valor)
    
    def __repr__(self):
        return f"Nodo({self.valor}, izquierda: {self.izquierda}, derecha: {self.derecha})"
    
    def obtener_valor(self) -> T:
        return self.valor

class ArbolBinario(Generic[T]):
    def __init__(self, raiz: Optional[Nodo[T]]= None) -> None:
        self.raiz:Optional[Nodo[T]] = raiz
        
    def es_vacio(self) -> bool:
        return self.raiz is None
    
    def insertar(self, valor: T) -> None:
        def _insertar_recursivo(nodo: Optional[Nodo], valor: T) -> Nodo:
            if nodo is None:
                return Nodo(valor)
            elif nodo.izquierda is None:
                nodo.izquierda =_insertar_recursivo(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar_recursivo(nodo.derecha, valor)
            return nodo
        if self.es_vacio():
            self.raiz = Nodo(valor)
        else:
            self.raiz = _insertar_recursivo(self.raiz, valor)
            
    def eliminar(self, valor: T)-> None:
        def _eliminar_recursivo(nodo: Optional[Nodo], valor: T)->Optional[Nodo]:
            if nodo and nodo.valor != valor:
                nodo.izquierda = _eliminar_recursivo(nodo.izquierda, valor)
                nodo.derecha = _eliminar_recursivo(nodo.derecha, valor)
            return nodo
        if not self.es_vacio():
            self.raiz = _eliminar_recursivo(self.raiz, valor)
            
        
    def cantidad(self) -> int:
        def _cantidad_recursivo(nodo: Optional[Nodo], acc: int) -> int:
            if nodo is None:
                return acc
            else:
                acc += 1
                acc = _cantidad_recursivo(nodo.izquierda, acc)
                acc = _cantidad_recursivo(nodo.derecha, acc)
            return acc
        
        if not self.es_vacio():
            return _cantidad_recursivo(self.raiz, 0)
        else:
            return 0


    def altura(self) -> int:
        def _altura_recursiva(nodo: Optional[Nodo]) -> int:
            if nodo is None:
                return 0
            else:
                altura_izquierda = _altura_recursiva(nodo.izquierda)
                altura_derecha = _altura_recursiva(nodo.derecha)
                return 1 + max(altura_izquierda, altura_derecha)   

        if not self.es_vacio():
            return _altura_recursiva(self.raiz)
        else:
            return 0

    def altura_valor(self, valor: T)->int:
        def _av_recursiva(nodo: Optional[Nodo], valor: T, altura_actual = 1):
            if nodo is None:
                return self.altura()+1
            elif nodo.obtener_valor() == valor:
                return altura_actual
            else: 
                altura_izquierda =_av_recursiva(nodo.izquierda,valor, altura_actual + 1)
                altura_derecha = _av_recursiva(nodo.derecha,valor, altura_actual + 1)
                return min(altura_izquierda, altura_derecha)
        return _av_recursiva(self.raiz,valor)
    
    def subarbol(self, buscado: Nodo[T], izq = True):
        def _subarbol_recursivo(nodo: Optional[Nodo],izq = True):
            if nodo:
                if nodo.obtener_valor()==buscado.obtener_valor():
                    if izq:
                        return ArbolBinario(nodo.izquierda)
                    else:
                        return ArbolBinario(nodo.derecha)
                else:
                    arbolIzq =_subarbol_recursivo(nodo.izquierda, izq)
                    arbolDer =_subarbol_recursivo(nodo.derecha, izq)
                    if not arbolIzq.raiz is None:
                        return arbolIzq
                    elif not arbolDer.raiz is None:
                        return arbolDer
                    else:
                        return ArbolBinario()
        return _subarbol_recursivo(self.raiz, izq = True)
                    
    def preorden(self):
        def _preorden_recursivo(nodo: Optional[Nodo]):
            if not nodo:
                return []
            else:
                return _preorden_recursivo(nodo.izquierda) + _preorden_recursivo(nodo.derecha)
        return _preorden_recursivo(self.raiz)
            
        
        
if __name__ == "__main__":
    root = Nodo("A")
    nodob = Nodo("B")
    nodoc = Nodo("C")
    nodod = Nodo("D")
    nodoe = Nodo("E")
    nodof = Nodo("F")
    nodog = Nodo("G")
    nodoh = Nodo("H")
    
    arbol_vacio = ArbolBinario()
    arbol_deh1 = ArbolBinario(root)
    arbol = ArbolBinario()
    arbol.insertar(root)
    arbol.insertar(nodob)
    arbol.insertar(nodoc)
    arbol.insertar(nodod)
    arbol.insertar(nodoe)    
    arbol.insertar(nodof)
    arbol.insertar(nodog)
    arbol.insertar(nodoh)
    
    print(arbol)
    print(arbol.cantidad())
    print(arbol.altura())
    print(arbol.altura_valor(nodoh))