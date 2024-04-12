from dataclasses import dataclass
from functools import reduce

@dataclass
class ItemMochila:
    peso: float
    valor: float

    def valor_ajustado(self) -> float:
        return self.valor / self.peso
    
    def __gt__(self, otro: "ItemMochila"):
        return isinstance(otro, ItemMochila) and self.valor_ajustado() > otro.valor_ajustado()


class Mochila:
    def __init__(self, capacidad: float):
        self.capacidad = capacidad
        self.contenido = []

    def valor(self) -> float:
        return reduce(lambda acc, actual: acc + actual.valor, self.contenido, 0)

    def peso_disponible(self) -> float:
        return self.capacidad - reduce(lambda acc, actual: acc + actual.peso, self.contenido, 0)

    def entra_item(self, item: ItemMochila) -> bool:
        return self.peso_disponible() >= item.peso
    
    def agregar(self, item: ItemMochila):
        if self.entra_item(item):
            self.contenido.append(item)
        else:
            raise ValueError("Item no entra")

    def agregar_fraccion(self, item):
        nuevo_peso = min(self.peso_disponible(), item.peso)
        nuevo_valor = item.valor * nuevo_peso / item.peso
        nuevo_item = ItemMochila(nuevo_peso, nuevo_valor)
        self.agregar(nuevo_item)

    def __str__(self):
        ret = f"Peso disponible: {self.peso_disponible()}\n"
        ret += f"Valor: {self.valor()}"
        return ret
    
    def optimizar_greedy(self, items: list[ItemMochila]):
        def optimizar(items):
            item = items[0]
            if self.entra_item(item):
                self.agregar(item)
                optimizar(items[1:])

        items.sort(reverse= True)
        optimizar(items)

    def optimizar_greedy_fraccionado(self, items: list[ItemMochila]):
        def optimizar(items):
            if items and self.peso_disponible() > 0:
                for item in items:
                    if self.entra_item(item):
                        self.agregar(item)
                    else:
                        self.agregar_fraccion(item)
        items.sort(reverse= True)
        optimizar(items)

if __name__ == "__main__":
    items = [
        ItemMochila(2.4, 10),
        ItemMochila(5.9, 20),
        ItemMochila(9.4,3),
        ItemMochila(6.4, 6),
        ItemMochila(3.4, 17),
        ItemMochila(2.8, 8)
    ]

    mochila = Mochila(20)
    mochila.optimizar_greedy(items)
    print(mochila)


    mochila.optimizar_greedy_fraccionado(items)
    print(mochila)