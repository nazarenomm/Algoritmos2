def contar_hacia_atras_par (n):
    if n == 0:
        return print(0)
    elif n % 2 == 0:
        print(n)
        return contar_hacia_atras_impar(n-1)
    else:
        return contar_hacia_atras_impar(n)

def contar_hacia_atras_impar (n):
    if n == 1:
        return print(n)
    elif n % 2 != 0:
        print(n)
        return contar_hacia_atras_par(n-1)
    else:
        return contar_hacia_atras_par(n)

if __name__ == "__main__":
    contar_hacia_atras_impar(5)