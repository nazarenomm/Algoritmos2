from functools import reduce
lista = [1, 4, 6, 12]

lista2 = map(lambda i: i*i, lista)

for i in lista2:
    print(i)

print(type(lista2))

num = reduce(lambda i, j: i*j, lista)

print(num)