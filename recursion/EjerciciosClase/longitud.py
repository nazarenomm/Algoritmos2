def longitud_no_recursiva(lista:list[int]) -> int:
    count = 0
    while lista:
        lista = lista[1:]
        count += 1
    return count

xs=[1,2,3,4]

print(longitud_no_recursiva(xs))