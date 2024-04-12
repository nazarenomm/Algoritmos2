def fibonacci_cola(n: int, actual: int = 0, siguiente: int = 1) -> int:
    if n <= 0:
        raise ValueError("n debe ser natural")
    if n == 1:
        return siguiente
    else:
        return fibonacci_cola(n - 1, siguiente, siguiente + actual)
    
def fibonacci(n: int) -> int:
    print(f"invoca fib({n})")
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
def fibo_tail(n: int) -> int:
    def fibo(pila: list[int], acc: int = 0):
        print(pila)
        if not pila:
            return acc
        else:
            actual = pila.pop()
            if actual < 2:
                acc += actual
            else:
                pila.append(actual - 1)
                pila.append(actual - 2)
            return fibo(pila, acc)
    return fibo([n])

def fibonacci_eficiente(n: int):
    mem = {}
    def fibo_interna(n: int):
        if n <= 1:
            return n
        else:
            if not n in mem:
                mem[n] = fibo_interna(n-2) + fibo_interna(n-1)
            return mem[n]
    return fibo_interna(n)

if __name__ == "__main__":
    print(fibonacci_cola(7))
    print(fibo_tail(4))