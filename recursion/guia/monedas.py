import copy

class Moneda:
    def __init__(self, peso: int = 3):
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
        pilas = [Pila() for _ in range(n)]
        while not self.esta_vacia():
            for p in pilas:
                if not self.esta_vacia():
                    p.apilar(self.desapilar())
        return pilas

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

def buscar_falsa2(pila): 
    # dividir en 3
    # pesar las subbpilas que tengan el mismo len o mejor usar promedio

# Divide las 30 monedas en tres grupos de 10 monedas cada uno.
# Pesa dos de estos grupos entre sí. Si el peso es igual,
#entonces la moneda más liviana debe estar en el tercer grupo no pesado.
# Si un grupo resulta más liviano, divide ese grupo en tres subgrupos de 3 monedas cada uno y
# vuelve al paso 2 con estos subgrupos.
# Repite este proceso hasta que encuentres la moneda más liviana o
# hasta que hayas alcanzado el límite de 4 pesajes


# Pesaje 1: Pesa dos grupos de 10 monedas cada uno.

# Si son iguales, la moneda más liviana está en el tercer grupo no pesado.
# Si uno es más ligero, procede al siguiente paso.
# Pesaje 2: Toma el grupo más ligero de 10 monedas y divídelo en tres subgrupos de 3 monedas cada uno. 
# Pesa los dos subgrupos de 3 monedas entre sí.

# Si son iguales, la moneda más liviana está en el subgrupo no pesado.
# Si uno es más ligero, procede al siguiente paso.
# Pesaje 3: Dentro del subgrupo más ligero de 3 monedas, pesa dos de las monedas entre sí.

# Si son iguales, la moneda más liviana es la tercera moneda no pesada.
# Si una es más ligera, esa es la moneda más liviana.
    
if __name__ == "__main__":
    monedas = Pila()

    cantidad_monedas = 10
    for i in range(cantidad_monedas):
        if i == cantidad_monedas // 2:
            monedas.apilar(Moneda(1))
        else:
            monedas.apilar(Moneda())

    print(monedas)
    print("Mondeda encontrada: ", buscar_falsa(monedas))


