# La moneda falsa es la menos pesada de todas?

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def tamano(self):
        return len(self.items)

def buscar_falsa(pila):
    
    
if __name__ == "__main__":
    monedas = Pila()
    monedas.apilar(3)
    monedas.apilar(4)
    monedas.apilar(7)
    monedas.apilar(2)
    monedas.apilar(4)
    monedas.apilar(5)
    monedas.apilar(6)


