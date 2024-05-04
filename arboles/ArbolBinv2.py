from typing import Generic, Optional, TypeVar, Callable, Any 
from functools import wraps
T = TypeVar("T")

class Nodo:
    def __init__(self, dato :T) -> None:
        self.valor = dato
        self.si: ArbolBinario[T] = ArbolBinario()
        self.sd: ArbolBinario[T] = ArbolBinario()
            
class ArbolBinario(Generic[T]):
    class Decoradores:
        @classmethod
        def valida_no_es_vacio(cls, f:Callable[..., Any]) ->Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args, **kwargs)-> Any:
                if self.es_vacio():
                    raise TypeError("Arbol vacio")
                return f(self, *args, **kwargs)
            return wrapper
            
    
    def __init__(self) -> None:
        self.raiz: Optional[Nodo] = None
    
    @staticmethod
    def crear_nodo(dato:T) -> "ArbolBinario[T]":
        nuevo = ArbolBinario()
        nuevo.raiz = Nodo(dato)
        return nuevo
    
    def es_vacio(self) -> bool:
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
    def insertar_si(self,si:"ArbolBinario[T]") -> None:
        self.raiz.si = si
    
    @Decoradores.valida_no_es_vacio
    def insertar_sd(self,sd:"ArbolBinario[T]") -> None:
        self.raiz.sd = sd
        
    def es_hoja(self):
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()
        
    def set_raiz(self,dato: T) -> None:
        self.raiz = Nodo(dato)
        
    def copy(self) ->"ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato())
            nuevo.insertar_si(self.si().copy())
            nuevo.insertar_sd(self.sd().copy())
            return nuevo 
    
    #TODO: arbol espejo
        
        
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return [self.dato()] + self.si().preorder() + self.sd().preorder()
        
    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] +  self.sd().inorder()
        
    def posorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().posorder() +  self.sd().posorder() + [self.dato()]
        
    def preorder_tail(self) -> list[T]:
        def recorrido(p: list[ArbolBinario[T]], camino: list[T])-> list[T]:                
            if not p:
                return camino
            else:
                actual = p.pop()
                if not actual.es_vacio(): 
                    camino.append(actual.dato())
                    p.append(actual.sd())
                    p.append(actual.si())                
                return recorrido(p,camino)   
        return recorrido([self], [])
        
    def preorder_iter(self) -> list[T]:
        p = [self]
        camino = []
        while p:
            actual = p.pop()
            if not actual.es_vacio(): 
                camino.append(actual.dato())
                p.append(actual.sd())
                p.append(actual.si())                
        return camino   

    def bfs(self) -> list[T]:
        def recorrido(q: list[ArbolBinario[T]], camino: list[T])-> list[T]:                
            if not q:
                return camino
            else:
                actual = q.pop(0)
                if not actual.es_vacio(): 
                    camino.append(actual.dato())
                    q.append(actual.si())
                    q.append(actual.sd())                
                return recorrido(q,camino)   
        return recorrido([self], [])
    
    def bfs_inversa(self) -> list[T]:
        def recorrido(q: list[ArbolBinario[T]], camino: list[T])-> list[T]:                
            if not q:
                return camino
            else:
                actual = q.pop(0)
                if not actual.es_vacio(): 
                    camino.insert(0,actual.dato())
                    q.append(actual.si())
                    q.append(actual.sd())                
                return recorrido(q,camino)   
        return recorrido([self], [])
        
    
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else: 
            return 1 + len(self.si()) + self.sd().__len__()                
        
    def __str__(self):
        def recorrer(t: ArbolBinario[T],nivel:int)->str:
            tab = "." * 4 * nivel
            if t.es_vacio():
             return tab + "AV"+ "\n"
            else:
                tab += str(t.dato()) + "\n"
                tab += recorrer(t.si(), nivel + 1)
                tab += recorrer(t.sd(), nivel + 1)
                return tab
        return recorrer(self, 0)
        
                
    def hojas(self):
        if self.es_vacio():
            return []
        elif self.es_hoja():           #TODO
            return self.si().hojas() + self.sd().hojas()
        
        
    def sin_hojas(self) ->"ArbolBinario[T]":
        if self.es_vacio() or self.es_hoja():
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato())
            nuevo.insertar_si(self.si().sin_hojas())
            nuevo.insertar_sd(self.sd().sin_hojas())
            return nuevo 
    
    def podar(self, dato:T) ->"ArbolBinario[T]":
        if self.es_vacio() or self.dato() == dato:
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato())
            nuevo.insertar_si(self.si().podar(dato))
            nuevo.insertar_sd(self.sd().podar(dato))
            return nuevo 
        


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
    print(t.preorder())
    print(t.inorder())
    print(t.posorder())
    print(t.altura())
    print(len(t))
    
    r = t.copy()
    print(r.bfs())
    print(r.bfs_inversa())
    