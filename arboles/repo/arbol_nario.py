from functools import reduce
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []

    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> list["ArbolN[T]"]:
        return self._subarboles

    @subarboles.setter
    def subarboles(self, subarboles: list["ArbolN[T]"]):
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: "ArbolN[T]"):
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + max([subarbol.altura() for subarbol in self.subarboles])
        
    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])
        
    def __str__(self) -> str:
        string = []
        def _interna(arbol, prefijo: str = "", es_ultimo: bool = True, es_raiz: bool= True):
            simbolo_rama = '+---> '
            if es_raiz:
                string.append(str(arbol.dato))
                for i, sub in enumerate(arbol.subarboles, start=1):
                    es_ultimo = i == len(arbol.subarboles)
                    _interna(sub, prefijo, es_ultimo, es_raiz=False)
            elif arbol.es_hoja():
                string.append(prefijo + "|")
                string.append(prefijo + simbolo_rama + str(arbol.dato))
            else:
                string.append(prefijo + "|")
                string.append(prefijo + simbolo_rama + str(arbol.dato))
                prefijo += ' '*6 if es_ultimo else '|' + ' '*4
                for i, sub in enumerate(arbol.subarboles, start=1):
                    es_ultimo = i == len(arbol.subarboles)
                    _interna(sub, prefijo, es_ultimo, es_raiz=False)

        _interna(self)
        return "\n".join(string)
    
    def __eq__(self, otro) -> bool:
        if self.dato != otro.dato or len(self.subarboles) != len(otro.subarboles):
            return False
        else:
            for sub1,sub2 in zip(self.subarboles, otro.subarboles):
                if sub1 != sub2:
                    return False
        return True
    
    def preorder(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder()
        return recorrido
    
    def postorden(self) -> list[T]:
        recorrido = []
        for subarbol in self.subarboles:
            recorrido += subarbol.postorden()
        recorrido.append(self.dato)
        return recorrido
    
    def bfs(self):
        bfs = []
        def _recorrer(cola: list[ArbolN[T]]) -> None:
            if cola:
                arbol = cola.pop(0)
                bfs.append(arbol.dato)
                for subarbol in arbol.subarboles:
                    cola.append(subarbol)
                _recorrer(cola)
                
        _recorrer([self])
        return bfs
    
    def copy(self) -> "ArbolN[T]":
        nuevo = ArbolN(self.dato)
        for subarbol in self.subarboles:
            nuevo.insertar_subarbol(subarbol.copy())
        return nuevo
    
    def recorrido_guiado(self, recorrido: list[int]) -> T:
        if not recorrido:
            return self.dato
        else:
            direccion = recorrido.pop(0)
            return self.subarboles[direccion].recorrido_guiado(recorrido)


if __name__ == "__main__":
    arbol = ArbolN(1)
    s2 = ArbolN(2)
    s3 = ArbolN(3)
    s4 = ArbolN(4)
    s5 = ArbolN(5)
    s6 = ArbolN(6)
    s7 = ArbolN(7)
    s8 = ArbolN(8)
    s9 = ArbolN(9)

    arbol.insertar_subarbol(s2)
    arbol.insertar_subarbol(s3)
    arbol.insertar_subarbol(s4)
    s2.insertar_subarbol(s5)
    s4.insertar_subarbol(s6)
    s2.insertar_subarbol(s7)
    s4.insertar_subarbol(s8)
    s4.insertar_subarbol(s9)

    print(arbol)
    print(arbol.preorder())
    print(arbol.postorden())
    print(arbol.bfs())
    print(arbol.recorrido_guiado([2,0]))