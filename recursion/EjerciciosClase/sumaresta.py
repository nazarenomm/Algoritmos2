def suma_resta_alternada(xs: list[int]) -> int:
    def suma(xs: list, acumulador) -> int:
            if not xs:
                return acumulador
            else:
                acumulador += xs[0]
                return resta(xs[1:], acumulador)
    def resta(xs: list[int], acumulador) -> int:
        if not xs:
            return acumulador
        else:
            acumulador-= xs[0]
            return suma(xs[1:],acumulador)
        
    if not xs:
        return 0
    else:   
        acumulador = xs[0]
        
        return suma(xs[1:], acumulador)

if __name__ =="__main__":
    xs=[1,2,3,4,5]
    print(suma_resta_alternada(xs))