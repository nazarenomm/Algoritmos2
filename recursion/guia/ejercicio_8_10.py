def mcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return mcd(y, x % y)
    
def factores(n: int, divisor:int  = 2) -> None:
    if n <= 1:
        return
    if n % divisor == 0:
        print(divisor)
        factores(n // divisor, divisor)
    else:
        factores(n, divisor + 1)

lista_factores: list[int] = []
def factores_sin_repetir(n: int, divisor: int = 2) -> None:
    global lista_factores
    if n <= 1:
        for factor in lista_factores:
            print(factor)
        return
    if n % divisor == 0:
        if divisor not in lista_factores:
            lista_factores.append(divisor)
        factores_sin_repetir(n // divisor, divisor)
    else:
        factores_sin_repetir(n, divisor + 1)

def factores_sin_repetir2(n: int, divisor: int = 2, factores: list[int] = []) -> None:
    if n <= 1:
        for factor in factores:
            print(factor)
        return
    if n % divisor == 0:
        if divisor not in factores:
            factores.append(divisor)
        factores_sin_repetir2(n // divisor, divisor, factores)
    else:
        factores_sin_repetir2(n, divisor + 1, factores)

def combinatorio(n: int, k: int) -> int:
    if k < 0:
        raise ValueError("Deben ser enteros mayor a cero")
    elif n < k:
        raise ValueError("n debe ser mayor a k")
    
    if k == 0 or k == n:
        return 1
    else:
        return combinatorio(n - 1, k - 1) + combinatorio(n - 1, k)
    
print("mcd(24,6): ", mcd(24,6))
print("Factores de 20: ")
factores(20)
print("Factores sin repetir de 20: ")
factores_sin_repetir(20)
print("Factores sin repetir (v2) de 20: ")
factores_sin_repetir2(20)
print("Combinatorio (6,2): ", combinatorio(6,2))