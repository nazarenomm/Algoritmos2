from functools import reduce

class Moneda:
    def __init__(self, peso: float = 3):
        self.peso = peso
    
    def __lt__(self, otra: "Moneda"):
        return self.peso < otra.peso
    
    def __str__(self) -> str:
        if self.peso != 3:
            return "Moneda Falsa"
        else:
            return "Moneda Original"
        
    def __repr__(self) -> str:
        return f"Moneda({self.peso})"
        
class Pila():
    def __init__(self):
        self.items = []
    
    def __len__(self) -> int:
        return len(self.items)
    
    def __repr__(self) -> str:
        return (f"Pila({self.items})")

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item: Moneda):
        self.items.append(item)

    def desapilar(self) -> Moneda:
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def ver_tope(self) -> Moneda:
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")
        
    def copy(self):
        nueva_pila = Pila()
        for item in self.items:
            nueva_pila.apilar(item)
        return nueva_pila
    
    def dividir(self, n: int) -> list["Pila"]:
        pila = self.copy()
        pilas = [Pila() for _ in range(n)]
        while not pila.esta_vacia():
            for p in pilas:
                if not pila.esta_vacia():
                    p.apilar(pila.desapilar())
        return pilas
    
    def peso(self) -> float:
        return reduce(lambda acc, actual: acc + actual.peso, self.items, 0)
    
    def peso_prom(self) -> float:
        return self.peso() / len(self)

def buscar_falsa(pila: Pila) -> Moneda:
    pila_copia = pila.copy()
    ultima_moneda = pila.desapilar()
    def interna(pila, moneda_actual: Moneda) -> Moneda:
        if pila.esta_vacia():
            return moneda_actual
        else:
            moneda = pila.desapilar()
            if moneda < moneda_actual:
                moneda_actual = moneda
            return interna(pila, moneda_actual)
    return interna(pila_copia, ultima_moneda)

def buscar_falsa2(pila: Pila) -> tuple[Moneda,int]:
    def interna(pila: Pila, acc: int) -> tuple[Moneda,int]:
        if len(pila) == 1:
            return pila.desapilar(), acc
        else:
            pilas = pila.dividir(3)
            acc += 1 # uso la balanza
            if pilas[0].peso_prom() < pilas[1].peso_prom():
                pila_falsa = pilas[0]
            elif pilas[1].peso_prom() < pilas[0].peso_prom():
                pila_falsa = pilas[1]
            else:
                pila_falsa = pilas[2]
            return interna(pila_falsa, acc)
    return interna(pila, 0)

if __name__ == "__main__":
    monedas = Pila()

    cantidad_monedas = 30
    for i in range(cantidad_monedas):
        if i == 1: #cantidad_monedas // 2:
            monedas.apilar(Moneda(1))
        else:
            monedas.apilar(Moneda())
            
    busqueda = buscar_falsa2(monedas)
    print(f"Se encontró una {busqueda[0]} en {busqueda[1]} pesajes")