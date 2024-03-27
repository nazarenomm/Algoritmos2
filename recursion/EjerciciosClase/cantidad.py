def cantidad(xs: list[int], n: int) -> int:
    def cantidad_interna(xs,n,acc):
        if not xs:
            return acc
        else:
            if xs[0] == n:
                acc +=1
            return cantidad_interna(xs[1:],n,acc)
    return cantidad_interna(xs,n,0)

def cantidad_pila(xs: list[int], n: int) -> int:
    if not xs:
        return 0
    else:
        valor = 0
        if xs[0] == n:
            valor = 1
        return valor + cantidad_pila(xs[1:],n)
    
if __name__ == "__main__":
    xs = [1,2,3,4]
    print(cantidad(xs,2))
    print(cantidad_pila(xs,2))
