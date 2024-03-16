def sumatoria(n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        return n + sumatoria(n + 1)
    else:
        return n + sumatoria(n-1)
    

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El valor de n debe ser un entero positivo")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("El valor de n debe ser un entero positivo")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def producto(z: int, v: int) -> int:
    if v == 0:
        return 0
    elif v > 0:
        return z + producto(z, v - 1)
    else:
        return -producto(z, -v)

def potencia(x: int, y: int) -> int:
    if x == 1 or y == 0:
        return 1
    else:
        return x * x**(y - 1)
    
def cociente(x: int, y: int) -> int:
    if y == 0:
        raise ValueError("No se puede dividir por cero")
    if x < y:
        return 0
    else:
        return 1 + cociente(x - y, y)

def resto(x: int, y: int) -> int:
    return x - cociente(x,y) * y

print("sumatoria(5): ", sumatoria(5))
print("factorial(4): ", factorial(4))
print("fibonacci(7): ", fibonacci(7))
print("producto(4,3):", producto(4,3))
print("potencia(2,3):", potencia(2,3))
print("8 // 4 = ", cociente(8,4))
print("resto:", resto(8,4))