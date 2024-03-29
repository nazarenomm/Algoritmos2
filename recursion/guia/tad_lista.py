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
    
    def __eq__(self, otro):
        return self.dato == otro.dato

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
    
    def __getitem__(self, index: int) -> T:
        if index >= len(self) or index < (-1*len(self)) :
            raise IndexError()

        if index == 0:
            return self._head
        elif index == -1:
            return self.ultimo()
        elif index > 0:
            return self._head.sig[index - 1]
        else:
            copia_self = self.copy()
            copia_self.eliminar(copia_self.ultimo())
            return copia_self[index + 1]

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

    def insertar_ultimo(self, dato: T):
        if self.es_vacia():
            self._head = Nodo(dato, Lista())
        else:
            self._head.sig.insertar_ultimo(dato)

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
        if len(self) == 1:
            return self.head()
        else:
            return self._head.sig.ultimo()

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        concatenada = self.copy()
        if ys.es_vacia():
            return concatenada
        else:
            concatenada.insertar_ultimo(ys._head)
            return concatenada.concat(ys._head.sig)
        
    def join(self, separador: str = '') -> str:
        def join_interna(self, separador) -> str:
            if self.es_vacia():
                return ''
            else:
                return str(self._head) + separador + join_interna(self._head.sig, separador)
        return join_interna(self, separador)[:-len(separador)]
        
    def index(self, valor: T) -> int | None:
        def index_interna(self, valor, index = 0):
            if self._head.dato == valor:
                return index
            else:
                return index_interna(self._head.sig, valor, index + 1)
        if self.existe(valor):
            return index_interna(self, valor)
        else:
            return None
            
    def existe(self, valor: T) -> bool:
        if self.es_vacia():
            return False
        else:
            return self._head.dato == valor or self._head.sig.existe(valor)

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
        if len(self) != len(otra):
            return False
        if len(self) == 1:
            return self._head == otra._head
        else:
            return self._head == otra._head and self._head.sig == otra._head.sig

    def reversa(self) -> ListaGenerica:
        if self.es_vacia():
            return self
        else:
            nodo = Lista()
            nodo.insertar(self._head)
            return self._head.sig.reversa().concat(nodo)
        
    def primeros(self, n:int) -> ListaGenerica:
        def interna(self, n: int, primeros: ListaGenerica = Lista()) -> ListaGenerica:
            if len(primeros) == n:
                return primeros
            else:
                primeros.insertar_ultimo(self._head)
                return interna(self._head.sig, n, primeros)
        return interna(self, n)

    def cantidad(self, n: T) -> int:
        if not isinstance(n, Nodo):
            nodo = Nodo(n)
        def cant_interna(self: ListaGenerica, nodo: Nodo, acc: int = 0) -> int:
            if not self.existe(nodo.dato):
                return acc
            else:
                if self._head == nodo:
                    acc += 1
                return cant_interna(self._head.sig, nodo, acc)
        return cant_interna(self,nodo)

    def intercalar(self, otra: ListaGenerica) -> ListaGenerica:
        if len(self) == 1 and len(otra) == 1:
            return self.concat(otra)
        else:
            lista_temp = Lista()
            lista_temp.insertar_ultimo(self._head)
            lista_temp.insertar_ultimo(otra._head)
            return lista_temp.concat(self._head.sig.intercalar(otra._head.sig))

    def sublista(self, n: int, l: int) -> ListaGenerica:
        def interna(self: ListaGenerica, n: int, l: int) -> ListaGenerica:
            if len(self) < 1:
                raise IndexError()
            if n == 0:
                return self
            else:
                return interna(self._head.sig, n - 1, l)
        return interna(self, n, l).primeros(l)

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
    
    print(f'xs: {xs}')
    print(f'ys: {ys}')
    print(f'zs: {zs}')

    print(f'xs igual a xs?: {xs == xs}')
    print(f'xs igual a ys?: {xs == ys}')

    print(f'ultimo de xs: {xs.ultimo()}')
    print(f'ultimo de xs: {ys.ultimo()}')

    print(f'join de xs: {xs.join(" separador ")}')

    print(f'4 en xs?: {xs.existe(4)}')
    print(f'5 en xs?: {xs.existe(5)}')

    print(f'index de 100 en xs: {xs.index(100)}')
    print(f'index de 10 en xs: {xs.index(10)}')

    print(f'xs e ys concatenadas: {xs.concat(ys)}')

    print(f'xs[1]: {xs[1]}')
    print(f'xs[-1]: {xs[-1]}')				

    # Consumiendo como iterable
    for x in xs:
        print(x)	# 20 -> 10 -> 4

    print(f'reversa de xs: {xs.reversa()}')

    print(f'primeros 2 elementos de xs: {xs.primeros(2)}')

    print(f'veces de 10 en xs: {xs.cantidad(10)}')

    intercaladas = xs.intercalar(ys)
    print(f'xs e ys intercaladas: {intercaladas}')

    print(intercaladas.sublista(1,3))
    