def aplanar(xs: list[list[int]])->list[int]:
    if not xs:
        return []
    else:
        return xs[0] + aplanar(xs[1:])
    
def aplanar_cola(xs: list[list[int]])->list[int]:
    def aplanar_interna(xs,ac):
        if not xs:
            return ac 
        else:
            ac += xs[0]
            return aplanar_interna(xs[1:],ac)
    return aplanar_interna(xs,[])


if __name__ == "__main__":
    xs= [[1,2],[],[3],[4,5]]
    ys= []
    
    print(aplanar(xs))
    print(aplanar_cola(xs))
    
    print(xs)    
