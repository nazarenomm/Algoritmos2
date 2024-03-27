from quicksort import quicksort
def busquedaBinaria(xs, n):
    xs = quicksort(xs)
    mitad = len(xs)//2
    if not xs:
        return False
    elif len(xs) <= 1:
        return xs[0] == n
    elif xs[mitad] == n:
        return True
    elif xs[mitad] > n:
        return busquedaBinaria(xs[0:mitad], n)
    else:
        return busquedaBinaria(xs[mitad:],n )

if __name__ == "__main__":
    xs = []
    
    print(busquedaBinaria(xs,5))