from typing import Generic, TypeVar
from tad_lista import Lista

T = TypeVar('T')

class Conjunto(Generic[T]):
    def __init__(self):
        self._elementos = Lista()
    
    def __repr__(self) -> str:
        def repr_interna(elementos: Lista[T]) -> str:
            if elementos.es_vacia():
                return ''
            else:
                return str(elementos._head) + ', ' + repr_interna(elementos._head.sig)
        return 'Conjunto(' + repr_interna(self._elementos)[:-2] + ')'
    
    def __str__(self) -> str:
        def str_interna(elementos) -> str:
            if elementos.es_vacia():
                return ''
            else:
                return str(elementos._head) + ', ' + str_interna(elementos._head.sig)
        return '{' + str_interna(self._elementos)[:-2] + '}'
    
    def agregar(self, elemento: T):
        if not self._elementos.existe(elemento):
            self._elementos.insertar(elemento)

    def eliminar(self, elemento: T):
        if self._elementos.existe(elemento):
            self._elementos.eliminar(elemento)

    def pertenece(self, elemento: T) -> bool:
        if self._elementos.existe(elemento):
            return True
        else:
            return False
        
    def a_lista(self) -> Lista[T]:
        return self._elementos.copy()

if __name__ == '__main__':
    conjunto = Conjunto()
    conjunto.agregar(6)
    conjunto.agregar(3)
    conjunto.agregar(5)
    conjunto.agregar(5)
    conjunto.eliminar(5)
    lista = conjunto.a_lista()

    print(f'conjunto: {conjunto}')
    print(f'repr(conjunto): {repr(conjunto)}')
    print(f'lista: {lista}')
    