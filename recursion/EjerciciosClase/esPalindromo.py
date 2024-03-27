def esPalindromo(xs :list[int])-> bool:
    if len(xs) <= 1:
        return True
    else:
        primero = xs[0]
        ultimo = xs[-1]
        return primero == ultimo and esPalindromo(xs[1:-1]) 
        

if __name__ == "__main__":
    xs=[1,2,3,2,1]
    print(esPalindromo(xs))