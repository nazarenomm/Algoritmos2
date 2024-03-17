def digitos(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + digitos(n // 10)

# Una función recursiva reversa_num que, dado un número entero,
# retorne su imagen especular. Por ejemplo: reversa_num(345) = 543
def reversa_num(n: int) -> int:
    if n < 10:
        return n
    else:
        potencia = 10 ** (digitos(n) - 1)
        primer_digito = n // potencia
        valor_previo = reversa_num(n - primer_digito * potencia)
        return valor_previo * 10 + primer_digito

def reversa_num2(n: int) -> int:
    if n < 10:
        return n
    else:
        potencia = 10 ** (digitos(n) - 1)
        ultimo = n % 10
        valor_previo = reversa_num2(n // 10)
        return potencia * ultimo + valor_previo
    
# Una función recursiva suma_digitos que, dado un número entero, 
# retorne la suma de sus dígitos.
def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    else:
        ultimo = n % 10
        valor_previo = suma_digitos(n // 10)
        return ultimo + valor_previo

# Una función recursiva que retorne los dos valores anteriores
# a la vez como un par, aprovechando la recursión.
def rev_suma(n: int) -> tuple[int, int]:
    if n < 10:
        return (n, n)
    else:
        ultimo = n % 10
        potencia = 10 ** (digitos(n) - 1)
        reverso_previo, suma_previa = rev_suma(n // 10)    # (reverso, suma_d)
        reverso = potencia * ultimo + reverso_previo
        suma = ultimo + suma_previa
        return (reverso, suma)

if __name__ == '__main__':
    n = 1234567
    print(f'Digitos de {n}: {digitos(n)}')
    print(f'reversa de {n}: {reversa_num(n)}')
    print(f'reversa de {n}: {reversa_num2(n)}')
    print(f'suma_digitos {n}: {suma_digitos(n)}')
    print(f'rev_suma {n}: {rev_suma(n)}')