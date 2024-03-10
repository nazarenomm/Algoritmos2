from collections.abc import Iterator

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primos() -> Iterator[int]:
    numero: int = 1
    while True:
        if es_primo(numero):
            yield numero
        numero += 1

for primo in primos():
    while primo < 100:
        print(primo)    
    