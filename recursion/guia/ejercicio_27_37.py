def longitud(lista: list[int]) -> int:
    if len(lista) == 0:
        return 0
    else:
        return longitud(lista[1:]) + 1
    
def igualdad(lista: list[int], otra: list[int]) -> int:
    if len(lista) != len(otra):
        return False
    elif len(lista) == 0:
        return True
    else:
        return lista[0] == otra[0] and igualdad(lista[1:], otra[1:])
    
def sumatoria(lista: list[int]) -> int:
    def suma_interna(lista: list[int], acc:int = 0) -> int:
        if len(lista) == 0:
            return acc
        else:
            acc += lista[0]
            return suma_interna(lista[1:], acc)
    return suma_interna(lista)

def pertenece(lista: list[int], e: int) -> bool:
    if len(lista) == 0:
        return False
    else:
        return lista[0] == e or pertenece(lista[1:], e)

def concatenacion(lista: list[int], otra: list[int]) -> list[int]:
    concatenada = lista.copy()
    def concat_interna(lista: list[int], otra: list[int]) -> list[int]:
        if len(otra) == 0:
            return lista
        else:
            lista.append(otra[0])
            return concatenacion(lista, otra[1:])
    return concat_interna(concatenada, otra)    

def ultimo(lista: list[int]) -> int:
    if len(lista) == 1:
        return lista[0]
    else:
        return ultimo(lista[1:])

def penultimo(lista: list[int]) -> int:
    return ultimo(lista[:-1])

def primeros(lista: list[int], n: int) -> list[int]:
    def interna(lista: list[int], n: int, primeros: list[int] = []):
        if len(primeros) == n:
            return primeros
        else:
            primeros.append(lista[0])
            return interna(lista[1:], n, primeros)
    return interna(lista, n)


def posicion(lista: list[int], n: int) -> int: #__getitem__
    if n >= len(lista) or n < (-1*len(lista)) :
        raise IndexError()
    if n == 0 or n == -1:
        return lista[n]
    elif n < 0:
        return posicion(lista[:-1], n + 1)
    else:
        return posicion(lista[1:], n - 1)

def maximo(lista: list[int]) -> int:
    def interna(lista: list[int], maximo) -> int:
        if len(lista) == 0:
            return maximo
        else:
            if lista[0] > maximo:
                maximo = lista[0]
            return interna(lista[1:], maximo)
    return interna(lista, lista[0])

def reversa(lista: list[int]) -> list[int]:
    if len(lista) == 0:
        return lista
    else:
        return reversa(lista[1:]) + [lista[0]]
    
if __name__ == "__main__":
    xs: list[int] = [1,2,4,3,5,6,7,10]
    ys: list[int] = [1,3,4,6,8,0]
    zs: list[int] = [-1,-3,-4,-6,-1]

    print(f'xs: {xs}')
    print(f'ys: {ys}')
    print(f'ys: {zs}')

    print(f'longitud de xs: {longitud(xs)}')
    print(f'longitud de ys: {longitud(ys)}')

    print(f'xs == ys? {igualdad(xs, ys)}')
    print(f'xs == xs? {igualdad(xs, xs)}')

    print(f'suma de xs: {sumatoria(xs)}')
    print(f'suma de ys: {sumatoria(ys)}')

    print(f'5 pertenece a xs? {pertenece(xs, 5)}')
    print(f'5 pertenece a ys? {pertenece(ys, 5)}')

    print(f'concatenación de xs e ys: {concatenacion(xs, ys)}')

    print(f'último de xs: {ultimo(xs)}')
    print(f'último de ys: {ultimo(ys)}')

    print(f'penúltimo de xs: {penultimo(xs)}')
    print(f'penúltimo de ys: {penultimo(ys)}')

    print(f'primeros 3 de xs: {primeros(xs, 3)}')
    print(f'primeros 2 de ys: {primeros(ys, 2)}')

    print(f'tercer elemento de xs: {posicion(xs,2)}')
    print(f'antepenúltimo elemento de xs: {posicion(xs,-3)}')

    print(f'máximo de xs: {maximo(xs)}')
    print(f'máximo de ys: {maximo(ys)}')
    print(f'máximo de zs: {maximo(zs)}')

    print(f'reversa de xs: {reversa(xs)}')
