from typing import Union, TypeAlias

__all__ = ['Nat', 'cero', 'division', 'es_cero', 'igual', 'mayor', 'mayor_igual', 'menor', 'menor_igual', 'nat_to_int', 'potencia', 'pred', 'producto', 'resta', 'suc', 'suma']

Nat: TypeAlias = Union["Cero", "Suc"]

# Clases constructoras de estructura
class Cero:
    def __repr__(self):
        return 'Cero'

    def __str__(self):
        return '0'

class Suc:
    def __init__(self, pred: Nat):
        self.pred = pred

    def __repr__(self):
        if isinstance(self.pred, Cero):
            return 'Suc(Cero)'
        else:
            return f'Suc({self.pred.__repr__()})'

    def __str__(self):
        return str(nat_to_int(self))

# Operaciones
def cero() -> Nat:
    return Cero()

def es_cero(n: Nat) -> bool:
    return isinstance(n, Cero)

def suc(n: Nat) -> Nat:
    return Suc(n)

def pred(n: Nat) -> Nat:
    if es_cero(n):
        raise ValueError('cero no tiene predecesor')
    else:
        return n.pred

def nat_to_int(n: Nat) -> int:
    if es_cero(n):
        return 0
    else:
        return 1 + nat_to_int(pred(n))

def suma(x: Nat, y: Nat) -> Nat:
    if es_cero(x):
        return y
    else:
        return suma(pred(x), suc(y))
    
def igual(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return es_cero(y)
    else:
        return igual(pred(x), pred(y))
    
def menor(x: Nat, y: Nat) -> bool:
    if es_cero(y):
        return False
    if es_cero(x):
        return not es_cero(y)
    else:
        return menor(pred(x), pred(y))

def mayor(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return False
    elif es_cero(y):
        return not es_cero(x)
    else:
        return mayor(pred(x), pred(y))

def menor_igual(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return True
    elif es_cero(y):
        return False
    else:
        return menor_igual(pred(x), pred(y))
    
def mayor_igual(x: Nat, y: Nat) -> bool:
    if es_cero(y):
        return True
    elif es_cero(x):
        return False
    else:
        return mayor_igual(pred(x), pred(y))

def resta(x: Nat, y: Nat) -> Nat:
    if mayor(y,x):
        raise ValueError("El segundo numero debe ser mayor al primero")
    if es_cero(y):
        return x
    else:
        return resta(pred(x), pred(y))
    
def producto(x: Nat, y: Nat) -> Nat:
    if es_cero(x) or es_cero(y):
        return cero()
    else:
        return suma(x, producto(x, pred(y)))

def division(x: Nat, y: Nat) -> Nat:
    if es_cero(y):
        raise ValueError("El divisor no puede ser cero")
    elif es_cero(x):
        return cero()
    else:
        def division_interna(dividendo: Nat, divisor: Nat, cociente: Nat) -> Nat:
            if menor(dividendo, divisor):
                return cociente
            else:
                return division_interna(resta(dividendo, divisor), divisor, suc(cociente))

        return division_interna(x, y, cero())
    
def potencia(base: Nat, exponente: Nat) -> Nat:
    if es_cero(exponente):
        return suc(cero())
    else:
        return producto(base, potencia(base, pred(exponente)))

if __name__ == '__main__':
    n1: Nat = cero()                # n1 = 0
    n2: Nat = suc(suc(suc(n1)))     # n2 = 3
    n3: Nat = suc(suc(n2))          # n3 = 5
    print(es_cero(n1))              # True
    n2 = pred(n2)                   # n2 = 2
    print(n2)                       # 2
    print(n3)                       # 5
    n4: Nat = suma(n2, n3)          # n4 = 7
    print(n4)                       # 7
    print(resta(n4, n2))            # 5
    print(repr(n4)) # Suc(Suc(Suc(Suc(Suc(Suc(Suc(Cero)))))))
    
    print(f'n2 < n4: {menor(n2, n4)}')
    print(f'n3 > n4: {mayor(n3, n4)}')
    print(f'producto(2, 7): {producto(n2, n4)}')  # 14
    print(f'resta(7, 2): {resta(n4,n2)}')
    print(f'division(7, 2): {division(n4, n2)}')  # 3
    print(f'potencia(2, 3): {potencia(suc(suc(cero())), suc(suc(suc(cero()))))}')  # 8
