from typing import Any

class ClaseInmutable:
    __slots__ = ("_elementos",)

    def __init__(self, *args):
        super().__setattr__("_elementos", tuple(*args))
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError(f'No es posible setear el atributo {__name}')
    
    def __delattr__(self, __name: str) -> None:
        raise AttributeError(f'No es posible eliminar el atributo {__name}')
    
    def elementos(self):
        return self._elementos


inmu = ClaseInmutable([1,4,6])
print(inmu._elementos)
#inmu._elementos[0] = 10
inmu._elementos = (10,3,5)
print(inmu._elementos)