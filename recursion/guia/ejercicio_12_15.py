def ackermann(n:int, m:int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m, n-1))

#print(ackermann(1,1))  ???????????
    
def raiz(a:int) -> float:
    if a < 0:
        raise ValueError("A debe ser positivo")
    if a == 1:
        return 1
    else:
        return (1 / 2) * (raiz(a - 1) + (a / raiz(a - 1)))

from ejercicios_1_6 import factorial
def taylor(x:float, tol: float, n:int = 0) -> float:
    termino = ((-1)**n)*(x**(2*n + 1)) / factorial(2*n +1)
    if abs(termino) < tol:
        return termino
    else:
        return termino + taylor(x, tol, n+1)

#print(taylor(1, 0.05))
    
def pares(n:int, x:int = 1, lista_pares:list[tuple[int, int]] = []) -> None:
    if n < 2:
        raise ValueError("El número debe ser mayor a uno")
    if n <= x :
        for par in lista_pares:
            print(par)
    else:
        par = (x,n-1)
        lista_pares.append(par)
        pares(n - 1, x + 1, lista_pares)

#pares(10)