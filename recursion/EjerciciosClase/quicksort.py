# def quicksort(xs: list[int]):
#     pivote = xs[-1]
#     def quicksort_interna(xs, pivote):
#         if pivote > 


def quicksort(xs: list[int])->list[int]:
    if len(xs) <= 1:
        return xs
    pivot = xs[-1]
    left = []
    right = []
    for i in xs[0:-1]:
        if i <= pivot:
            left.append(i) 
        else: 
            right.append(i) 
    return quicksort(left)+ [pivot] +quicksort(right)

