def producto_escalar(xs,ys):
    if len(xs) != len(ys):
        raise ValueError("Los vectores tienen que ser de la misma dimensiòn")
    if not xs:
        return 0
    else:
        return xs[0]*ys[0] + producto_escalar(xs[1:],ys[1:])
    
if __name__ == "__main__":
    xs = [1,2,3]
    ys = [1,1,1]
    
    print(producto_escalar(xs,ys))