from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self, dato: T) -> None:
        self._dato = dato
        self._si: ArbolBinario[T] = ArbolBinario()
        self._sd: ArbolBinario[T] = ArbolBinario()
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, nuevo_dato: T):
        self._dato = nuevo_dato

    @property
    def si(self):
        return self._si
    
    @si.setter
    def si(self, nuevo_si: "ArbolBinario[T]"):
        self._si = nuevo_si

    @property
    def sd(self):
        return self._sd
    
    @sd.setter
    def sd(self, nuevo_sd: "ArbolBinario[T]"):
        self._sd = nuevo_sd

    def __str__(self):
        return str(self.dato)
    
    def __repr__(self):
        return f"Nodo({self.dato})"
    
    def es_hoja(self):
        return self.si.es_vacio() and self.sd.es_vacio()
    
    def __eq__(self, otro: object) -> bool:
        return isinstance(otro, Nodo) and self.dato == otro.dato

class ArbolBinario(Generic[T]):
    def __init__(self) -> None:
        self._raiz: Optional[Nodo] = None

    @property
    def raiz(self):
        return self._raiz
    
    @raiz.setter
    def raiz(self, nuevo_dato: T):
        nueva_raiz = Nodo(nuevo_dato)
        self._raiz = nueva_raiz

    @staticmethod
    def crear_arbol(nuevo_dato: T) -> "ArbolBinario[T]":
        nuevo_arbol = ArbolBinario()
        nuevo_arbol.raiz = nuevo_dato
        return nuevo_arbol
    
    def es_vacio(self) -> bool:
        return self.raiz is None
    
    def agregar_si(self, si: "ArbolBinario[T]") -> None:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        self.raiz.si = si

    def agregar_sd(self, sd: "ArbolBinario[T]") -> None:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        self.raiz.sd = sd
    
    def __repr__(self) -> str:
        return f"ArbolBinario(raiz: {repr(self.raiz)})"
    
    
    # ejercicio 17
    def __str__(self) -> str:
        if self.es_vacio():
            return "Arbol Vacio"
        
        string = []
        def _interna(arbol, prefijo: str = "", es_ultimo: bool = True, es_raiz: bool= True):
            simbolo_rama = '+---> '
            if arbol.es_vacio():
                string.append(prefijo + "|")
                string.append(prefijo + simbolo_rama + "AV")
            elif es_raiz:
                string.append(str(arbol.raiz))
                _interna(arbol.raiz.si, prefijo, es_ultimo= False, es_raiz=False)
                _interna(arbol.raiz.sd, prefijo, es_ultimo=True, es_raiz=False)
            elif arbol.raiz.es_hoja():
                string.append(prefijo + "|")
                string.append(prefijo + simbolo_rama + str(arbol.raiz))
            else:
                string.append(prefijo + "|")
                string.append(prefijo + simbolo_rama + str(arbol.raiz))
                prefijo += ' '*6 if es_ultimo else '|' + ' '*4
                _interna(arbol.raiz.si, prefijo, False, False)
                _interna(arbol.raiz.sd, prefijo, True, False)

        _interna(self)
        return "\n".join(string)
    
    #ejercicio 2
    def cantidad_nodos(self):
        if self.es_vacio():
            return 0
        if self.raiz.es_hoja():
            return 1
        else:
            return 1 + self.raiz.si.cantidad_nodos() + self.raiz.sd.cantidad_nodos()
    
    # ejercicio 3
    def altura(self):
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.raiz.si.altura(), self.raiz.sd.altura())
    
    #ejercicio 4
    def __eq__(self, otro: "ArbolBinario[T]") -> bool:
        if self.es_vacio():
            return isinstance(otro, ArbolBinario) and otro.es_vacio()
        else:
            return self.raiz == otro.raiz and self.raiz.si == otro.raiz.si and self.raiz.sd == otro.raiz.sd

    # ejercicio 5
    def acceder(self, direcciones: list[str]) -> T:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        if len(direcciones) > self.altura():
            raise ValueError("Demasiadas direcciones")
        
        if not direcciones:
            return self.raiz.dato
        elif direcciones[0] == "izq":
            return self.raiz.si.acceder(direcciones[1:])
        elif direcciones[0] == "der":
            return self.raiz.sd.acceder(direcciones[1:])
        else:
            raise ValueError("Direccion incorrecta\nValores válidos: izq, der")
        
    #ejercicio 6.a
    def pertenece(self, dato: T) -> bool:
        if self.es_vacio():
            return False
        else:
            return self.raiz.dato == dato or self.raiz.si.pertenece(dato) or self.raiz.sd.pertenece(dato)
    
    #ejercicio 6.b
    def nivel(self, dato: T) -> int:
        def _interna(arbol, dato, nivel: int = 1):
            if arbol.es_vacio():
                return nivel + 1
            elif arbol.raiz.dato == dato:
                return nivel
            else:
                return min(_interna(arbol.raiz.si, dato, nivel + 1),_interna(arbol.raiz.sd, dato, nivel + 1))
        return _interna(self, dato)
    
    # ejercicio 6.c
    def padre(self, dato: T) -> T | None:
        if not self.si().es_vacio() and self.si().raiz.dato == dato:
            return self.raiz.dato
        
        if not self.sd().es_vacio() and self.sd().raiz.dato == dato:
            return self.raiz.dato

        padre_izq = None
        padre_der = None

        if not self.si().es_vacio():
            padre_izq = self.si().padre(dato)
        if not self.sd().es_vacio():
            padre_der = self.sd().padre(dato)

        return padre_izq if padre_izq is not None else padre_der

    
    # ejercicio 6.d
    def hijos(self, dato: T) -> list[T]:
        if self.raiz.es_hoja():
            return []
        elif self.raiz.dato == dato:
            return [self.raiz.si.raiz.dato] + [self.raiz.sd.raiz.dato]
        else:
            return self.raiz.si.hijos(dato) + self.raiz.sd.hijos(dato)

    # ejercicio 6.e
    def antecesores(self, dato: T) -> list[T]:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        def _buscar_antecesores(arbol, dato: T, antecesores: list[T]) -> bool:
            if arbol.es_vacio():
                return False
            if arbol.raiz.dato == dato:
                return True
            antecesores.append(arbol.raiz.dato)
            if _buscar_antecesores(arbol.raiz.si, dato, antecesores):
                return True
            if _buscar_antecesores(arbol.raiz.sd, dato, antecesores):
                return True
            antecesores.pop()
            return False

        antecesores = []
        if arbol.raiz is not None:
            _buscar_antecesores(arbol, dato, antecesores)
        return antecesores
    
    # ejercicio 7
    def sinHojas(self):
        if self.es_vacio():
            return ArbolBinario()
        
        nuevo_arbol = ArbolBinario()
        def _interna(arbol, nuevo_arbol):
            if not arbol.raiz.es_hoja():
                nuevo_arbol.raiz = arbol.raiz.dato
                if not arbol.raiz.si.es_vacio():
                    _interna(arbol.raiz.si, nuevo_arbol.raiz.si)
                if not arbol.raiz.sd.es_vacio():
                    _interna(arbol.raiz.sd, nuevo_arbol.raiz.sd)
        _interna(self, nuevo_arbol)
        return nuevo_arbol
    
    def si(self):
        return self.raiz.si
    
    def sd(self):
        return self.raiz.sd
    
    # ejercicio 8
    def ramas(self) -> list[list[T]]:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        
        ramas = []
        def _backtrack(arbol, rama:list[T] =[]) -> None:
            
            rama.append(arbol.raiz.dato)

            if arbol.raiz.es_hoja():
                ramas.append(rama.copy())
            else:
                if not arbol.raiz.si.es_vacio():
                    _backtrack(arbol.raiz.si, rama)
                if not arbol.raiz.sd.es_vacio():
                    _backtrack(arbol.raiz.sd, rama)

            rama.pop()

        _backtrack(self)
        return ramas

    # ejercicio 9
    def balanceado(self) -> bool:
        if self.es_vacio():
            raise ValueError("Arbol Vacio")
        
        longitud_ramas = []
        def _backtrack(arbol, rama:list[T] =[]) -> None:
            
            rama.append(arbol.raiz.dato)

            if arbol.raiz.es_hoja():
                longitud_ramas.append(len(rama))
            else:
                if not arbol.raiz.si.es_vacio():
                    _backtrack(arbol.raiz.si, rama)
                if not arbol.raiz.sd.es_vacio():
                    _backtrack(arbol.raiz.sd, rama)

            rama.pop()

        _backtrack(self)
        
        balanceado = (max(longitud_ramas) - min(longitud_ramas)) <= 1
        return balanceado
    
    def copy(self) ->"ArbolBinario[T]":
        if self.es_vacio():
            nuevo =  ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_arbol(self.raiz.dato)
            nuevo.agregar_si(self.si().copy())
            nuevo.agregar_sd(self.sd().copy())
        return nuevo 
    

    # ejercicio 10
    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            nuevo_arbol = ArbolBinario()
        else:
            nuevo_arbol = ArbolBinario.crear_arbol(self.raiz.dato)
            nuevo_arbol.agregar_si(self.sd().espejo())
            nuevo_arbol.agregar_sd(self.si().espejo())
        return nuevo_arbol
    
    # ejercicio 11
    # paso

    # ejercicio 12.a
    def preorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return [self.raiz.dato] + self.si().preorden() + self.sd().preorden()
    
    def inorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorden() + [self.raiz.dato] + self.sd().inorden()
        
    def posorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().posorden() + self.sd().posorden() + [self.raiz.dato]
        
    # ejercicio 12.b
    def preorden_cola(self) -> list[T]:
        def _recorrido(pila: list[ArbolBinario[T]], camino: list[T])-> list[T]:               
            if not pila:
                return camino
            else:
                arbol = pila.pop()
                if not arbol.es_vacio():
                    camino.append(arbol.raiz.dato)
                    pila.append(arbol.sd())
                    pila.append(arbol.si())
                return _recorrido(pila, camino)
        return _recorrido([self], [])
    
    
    def inorden_cola(self) -> list[T]:
        pass

    
    # ejercicio 13
    def bfs(self):
        bfs = []
        def _recorrer(cola: list[ArbolBinario[T]]):
            if cola:
                arbol = cola.pop(0)
                bfs.append(arbol.raiz.dato)
                if not arbol.si().es_vacio():
                    cola.append(arbol.si())
                if not arbol.sd().es_vacio():
                    cola.append(arbol.sd())
                _recorrer(cola)

        _recorrer([self])
        return bfs
    
    # ejercicio 14
    def insertar(self, valor: T) -> "ArbolBinario[T]":
        # agrega un nodo en el subarbol más pequeño, si son iguales:  al izquierdo
        # deberia agregarselo al 6, a izq
        # la idea es balancear un poco el arbol
        nuevo_arbol = self.copy()
        def _interna(arbol):
            if arbol.es_vacio():
                arbol.raiz = valor
            elif arbol.raiz.es_hoja():
                arbol.raiz.si = ArbolBinario.crear_arbol(valor)
            else:
                alt_si = arbol.si().altura()
                alt_sd = arbol.sd().altura()
                if alt_si <= alt_sd:
                    _interna(arbol.si())
                else:
                    _interna(arbol.sd())
        
        _interna(nuevo_arbol)
        return nuevo_arbol
    
    # ejercicio 15
    def eliminar(self, dato: T) -> "ArbolBinario[T]":
        # elimina toda la informacion del nodo, sus subarboles desaparecen
        
        if not self.pertenece(dato) or self.es_vacio():
            raise ValueError("El valor no forma parte del arbol")
        
        nuevo_arbol = self.copy()

        def _interna(arbol):
            if not arbol.si().es_vacio() and arbol.si().raiz.dato == dato:
                arbol.raiz.si = ArbolBinario()
            elif not arbol.sd().es_vacio() and arbol.sd().raiz.dato == dato:
                arbol.raiz.sd = ArbolBinario()
            
            else:
                if not arbol.si().es_vacio():
                    _interna(arbol.si())
                if not arbol.sd().es_vacio():
                    _interna(arbol.sd())

        _interna(nuevo_arbol)
        return nuevo_arbol

    # ejercicio 18
    def hermano(self, dato: T) -> T | None:
        if not self.si().es_vacio() and self.si().raiz.dato == dato:
            return self.sd().raiz.dato if not self.sd().es_vacio() else None
        elif not self.sd().es_vacio() and self.sd().raiz.dato == dato:
            return self.si().raiz.dato if not self.si().es_vacio() else None
        else:
            hermano_izq = None
            hermano_der = None
            if not self.si().es_vacio():
                hermano_izq = self.si().hermano(dato)
            if not self.sd().es_vacio():
                hermano_der = self.sd().hermano(dato)
            return hermano_izq if hermano_izq else hermano_der
        
    

if __name__ == "__main__":
    arbol = ArbolBinario.crear_arbol(1)
    a2 = ArbolBinario.crear_arbol(2)
    a3 = ArbolBinario.crear_arbol(3)
    a4 = ArbolBinario.crear_arbol(4)
    a5 = ArbolBinario.crear_arbol(5)
    a6 = ArbolBinario.crear_arbol(6)
    a7 = ArbolBinario.crear_arbol(7)
    a8 = ArbolBinario.crear_arbol(8)
    a9 = ArbolBinario.crear_arbol(9)
    a10 = ArbolBinario.crear_arbol(10)

    arbol.agregar_si(a2)
    arbol.agregar_sd(a3)
    a2.agregar_si(a4)
    a2.agregar_sd(a5)
    a3.agregar_si(a6)
    a3.agregar_sd(a7)
    a4.agregar_si(a8)
    a4.agregar_sd(a9)
    a8.agregar_si(a10)

    print(arbol)
    print(f"\nCantidad de nodos: {arbol.cantidad_nodos()}")

    dirs = ["izq", "der"]
    print(f"dirs a 5 es {dirs}?? : {arbol.acceder(dirs) == 5}")
    print(f"7 pertenece al arbol?: {arbol.pertenece(7)}")
    print(f"altura: {arbol.altura()}")
    print(f"nivel de 4: {arbol.nivel(4)}")
    print(f"padre de 6? : {arbol.padre(6)}")
    print(f"hijos de 2: {arbol.hijos(2)}")
    print(f"antecesores de 10: {arbol.antecesores(10)}")
    #print(f"arbol sin hojas:\n{arbol.sinHojas()}")
    print(f"ramas: {arbol.ramas()}")
    print(f"balanceado? :  {arbol.balanceado()}")
    #print(f"espejo: \n{arbol.espejo()}")
    # print(f"preorder: {arbol.preorden()}")
    # print(f"preorder cola: {arbol.preorden_cola()}")
    # print(f"inorder: {arbol.inorden()}")
    # print(f"inorder cola: {arbol.inorden_cola()}")
    # print(f"posorder: {arbol.posorden()}")
    print(f"bfs: {arbol.bfs()}")
    #print(f"arbol mas 11,12,13: \n{arbol.insertar(11).insertar(12).insertar(13)}")
    #print(f"elimino el 4:\n{arbol.eliminar(4)}")
    print(f"hermano de 7: {arbol.hermano(7)}")
    

    