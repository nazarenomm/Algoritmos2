def decimalBinario(decimal: int) -> str:
    if decimal == 0:
        return '0'
    elif decimal == 1:
        return '1'
    else:
        return decimalBinario(decimal // 2) + str(decimal % 2)

def cambioBaseDecimal(n: int, b: int) -> str:
    if n == 0:
        return '0'
    elif n < b:
        return str(n)
    else:
        return cambioBaseDecimal(n // b, b) + str(n % b)

def contiene_no_binario(cadena):
    for caracter in cadena:
        if caracter != '0' and caracter != '1':
            return True
    return False

def unosBinario(numero_binario: str) -> int:
    if contiene_no_binario(numero_binario):
        raise ValueError("No es un número binario")
    if not numero_binario:
        return 0
    elif numero_binario[0] == '1':
        return 1 + unosBinario(numero_binario[1:])
    else:
        return unosBinario(numero_binario[1:])
 
print(decimalBinario(4))
print(cambioBaseDecimal(23,2))
print(unosBinario("10101001"))