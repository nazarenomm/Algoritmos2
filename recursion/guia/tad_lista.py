from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

    def __str__(self):
        return str(self.dato)
    
    def __repr__(self) -> str:
        return f"Nodo({str(self.dato)})"

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None
    
    def __len__(self) -> int:
        if self.es_vacia():
            return 0
        else:
            return 1 + len(self._head.sig)
    
    def __str__(self) -> str:
        def str_interna(self) -> str:
            if self.es_vacia():
                return ''
            else:
                return str(self._head) + ', ' + str_interna(self._head.sig)
        return '[' + str_interna(self)[:-2] + ']'

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato

    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig
                else:
                    _eliminar_interna(actual._head.sig, actual, valor)

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head
            else:
                _eliminar_interna(self._head.sig, self, valor)

    def ultimo(self) -> T:
        pass

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        pass
        
    def join(self, separador: str = '') -> str:
        pass
        
    def index(self, valor: T) -> int:
        pass
        
    def existe(self, valor: T) -> bool:
        pass

    def __repr__(self) -> str:
        def interna(self):
            if self.es_vacia():
                return ''
            else:
                return repr(self._head) + ', ' + interna(self._head.sig)
        if self.es_vacia():
            return ''
        else:
            return f"Lista({interna(self)[:-2]})"

        
    def __eq__(self, otra: ListaGenerica) -> bool:
        pass
    # if len distintas return false
    #ir comparando heads y disminuyendo las listas return head1 == head2 and recursion
    

if __name__ == '__main__':
    xs: Lista[int] = Lista()
    
    print(f'xs es vacia? {xs.es_vacia()}')	# True
    
    # Operaciones basicas
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)
    
    print(xs)
    