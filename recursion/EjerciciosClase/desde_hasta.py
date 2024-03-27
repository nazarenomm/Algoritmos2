def desde_hasta(x:int, y:int) ->list[int]:
    def desde_hasta_interna(x:int, y:int, z:list[int]):
        if x <= y:
            z.append(x)
            return desde_hasta_interna(x+1,y,z)
        else:
            return z
    return desde_hasta_interna(x,y,z = [])

print(desde_hasta(3,3))