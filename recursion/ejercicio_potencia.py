from typing import Union

def potencia(base: float, exp: float) -> float:
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

print(potencia(2,2))
print(potencia(2,3))