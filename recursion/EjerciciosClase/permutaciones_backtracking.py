def permutaciones(lista: list[int]) -> list[list[int]]:
    def interna(actual, restante):
        if len(restante) == 0:
            resultado.append(actual)
        else:
            for i in range(len(restante)):
                interna(actual + [restante[i]], restante[:i] + restante[i+1:])
    resultado = []
    interna([], lista)
    return resultado

if __name__ == "__main__":
    lista = [1,2,3]
    print(permutaciones(lista))