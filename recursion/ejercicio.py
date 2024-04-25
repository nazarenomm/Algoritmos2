def es_par(n: int) -> bool:
    if n >= 0:
        return n == 0 or es_impar(n - 1)
    else:
        return es_impar(n + 1)

def es_impar(n: int) -> bool:
    if n >= 0:
        return False if n == 0 else es_par(n - 1)
    else:
        return es_par(n + 1)

def mostrar_pares(n: int) -> None:
    def pares(n:int, x:int, lista_pares:list[tuple[int, int]] = []) -> None:
        if n < 2:
            raise ValueError("El número debe ser mayor a uno")
        if n <= x :
            for par in lista_pares:
                print(par)
        else:
            par = (x,n-1)
            lista_pares.append(par)
            pares(n - 1, x + 1, lista_pares)
    pares(n, 1, [])

# Convertir la función resta_lista que utiliza una pila explícita de forma 
# que no use ningún tipo de recursión y sólo utilice iteración.
def resta_lista(xs: list[int]) -> int:
    def apilado(xs: list[int], pila: list[int]):
        if xs != []:
            pila.append(xs[0])
            apilado(xs[1:], pila)

    def desapilado(pila: list[int], acumulador: int) -> int:
        if pila == []:
            return acumulador
        else:
            return desapilado(pila, pila.pop() - acumulador)
    
    pila = []
    apilado(xs, pila)
    return desapilado(pila, 0)

def resta_lista_iter(xs: list[int]) -> int:
    resta = 0
    while xs:
        resta = xs[-1] - resta
        xs = xs[:-1]
    return resta

#Implementar una versión con recursión de cola que produzca el resultado esperado
# al pasar una lista: `suma_resta_alternada([1, 2, 3, 4, 5]) = 1 + 2 - 3 + 4 - 5 = -1                  

def suma_resta_alternada(xs: list[int]) -> int:
    def interna(xs: list[int], acumulador: int) -> int:
        if len(xs) == 1:
            acumulador += xs[-1]
            return acumulador
        else:
            if len(xs)%2 == 0:
                acumulador += xs[-1]
            else:
                acumulador -= xs[-1]
            return interna(xs[:-1], acumulador)
    return interna(xs, 0)

if __name__ == "__main__":
    print(suma_resta_alternada([1, 2, 3, 4, 5]))
