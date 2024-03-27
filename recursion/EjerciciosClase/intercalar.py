def intercalar(xs: list[int],ys: list[int]) -> list[int]:
    if len(xs) == 1 and len(ys) == 1:
        return xs + ys
    else:
        return [xs[0],ys[0]] + intercalar(xs[1:], ys[1:])
    
xs = [1,3,5]

ys = [2,4,6]

print(intercalar(xs,ys))

        