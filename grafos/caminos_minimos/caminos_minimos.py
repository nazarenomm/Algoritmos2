from typing import Generic, TypeVar

T = TypeVar("T")

class Arista(Generic[T]):
    def __init__(self, origen: T , destino: T, peso: int = 1, direccionada: bool = False) -> None:
        self.origen: T = origen
        self.destino: T = destino
        self.peso: int = peso
        self.direccionada = direccionada

    def __contains__(self, nodo: T):
        return nodo == self.origen or nodo == self.destino
    
    def __eq__(self, otro: "Arista[T]") -> bool:
        return isinstance(otro, Arista) and self.origen == otro.origen and self.destino == otro.destino and self.valor == otro.valor and self.direccionada == otro.direccionada 

    def __str__(self) -> str:
        return f"({self.origen},{self.destino})" if not self.direccionada else f"{self.origen}->{self.destino}"

class Grafo(Generic[T]):
    def __init__(self) -> None:    
        self.vertices: list[T] = []
        self.aristas: list[Arista[T]] = []

    def __contains__(self, x: T | Arista):
        if isinstance(x, Arista):
            return x in self.aristas
        else:
            return x in self.vertices
    
    def agregar_nodo(self, nodo: T) -> None:
        if nodo in self:
            raise ValueError("Nodo ya pertenece al grafo")
        self.vertices.append(nodo)

    def agregar_arista(self, origen: T, destino: T, valor: int = 1): # grafo simple, entonces las aristas no son direccionas
        arista = Arista(origen, destino, valor)
        if arista in self:
            raise ValueError("Arista ya pertenece al grafo")
        self.aristas.append(arista)

    def eliminar_nodo(self, nodo: T) -> None:
        self.vertices.remove(nodo)
        aristas_a_eliminar = [] # para no alterar la estructura por la que estoy iterando
        for arista in self.aristas:
            if nodo in arista:
                aristas_a_eliminar.append(arista)
        for a in aristas_a_eliminar:
            self.aristas.remove(a)

    def eliminar_arista(self, origen: T, destino: T) -> None:
        temp = Arista(origen, destino)
        self.aristas.remove(temp)

    def es_vecino_de(self, nodo1: T, nodo2: T) -> bool:
        retorno = False
        for arista in self.aristas:
            if nodo1 in arista:
                retorno = nodo2 in arista
        return retorno
    
    def vecinos_de(self, nodo):
        vecinos = []
        for arista in self.aristas:
            if nodo in arista:
                vecino = arista.origen if arista.origen != nodo else arista.destino
                vecinos.append(vecino)
        return vecinos
    
    def dfs(self, inicio: T):
        recorrido = []
        def _recorrer(nodo):
            if nodo not in recorrido:
                recorrido.append(nodo)
                for vecino in self.vecinos_de(nodo):
                    _recorrer(vecino)
        _recorrer(inicio)
        return recorrido
    
    def bfs(self, inicio: T):
        recorrido = []
        def _recorrer(cola: list[T]):
            if cola:
                nodo = cola.pop(0)
                if nodo not in recorrido:
                    recorrido.append(nodo)
                    for vecino in self.vecinos_de(nodo):
                        cola.append(vecino)
                _recorrer(cola)
                
        _recorrer([inicio])
        return recorrido
    
    def existe_conexion(self, nodo1: T, nodo2: T) -> bool:
        bfs1 = self.bfs(nodo1)
        return nodo2 in bfs1
    
    def dijkstra(self, origen: T, destino: T) -> list[T]:
        
    

if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_nodo("a")
    grafo.agregar_nodo("b")
    grafo.agregar_nodo("c")
    grafo.agregar_nodo("d")
    grafo.agregar_nodo("e")
    grafo.agregar_nodo("f")

    grafo.agregar_arista("a", "b", 5)
    grafo.agregar_arista("a", "c", 2)
    grafo.agregar_arista("a", "d", 3)
    grafo.agregar_arista("c", "b", 1)
    grafo.agregar_arista("b", "e", 1)
    grafo.agregar_arista("b", "f", 3)
    grafo.agregar_arista("e", "f", 1)
    grafo.agregar_arista("d", "e", 2)

    print(grafo.dijkstra("a", "f"))
    