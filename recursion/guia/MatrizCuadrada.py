from typing import Optional

class MatrizCuadrada:
    def __init__(self, elementos: list[list] = []):
        for fila in elementos:
            if len(fila) != len(elementos):
                raise ValueError("La matriz debe ser cuadrada")
        self._elementos = elementos
    
    @property
    def elementos(self):
        return self._elementos

    @elementos.setter
    def elementos(self, lista: list[list]):
        self._elementos = lista

    def __str__(self) -> str:
        out = ""
        for fila in self._elementos:
            fila_str = " ".join(str(elem) for elem in fila)
            out += f"| {fila_str} |\n"
        return out
    
    def size(self) -> tuple[int, int]:
        return (len(self.elementos),len(self.elementos[0]))
    
    def __getitem__(self, i, j: Optional[int] = None):
        if j is None:
            return self.elementos[i]
        else:
            return self.elementos[i][j]
    
    def __add__(self, otra: "MatrizCuadrada") -> "MatrizCuadrada":
        if self.size() != otra.size():
            raise ValueError("Las matrices deben tener la misma dimensión")
        nueva_matriz = []
        for fila_self, fila_otra in zip(self._elementos, otra.elementos):
            nueva_fila = [elem_self + elem_otra for elem_self, elem_otra in zip(fila_self, fila_otra)]
            nueva_matriz.append(nueva_fila)
        return MatrizCuadrada(nueva_matriz)
    
    def __sub__(self, otra):
        if self.size() != otra.size():
            raise ValueError("Las matrices deben tener la misma dimensión")
        nueva_matriz = []
        for fila_self, fila_otra in zip(self._elementos, otra.elementos):
            nueva_fila = [elem_self - elem_otra for elem_self, elem_otra in zip(fila_self, fila_otra)]
            nueva_matriz.append(nueva_fila)
        return MatrizCuadrada(nueva_matriz)
    
    def __mul__(self, otro):
       # Multiplicación por escalar
       if isinstance(otro, (int, float)):
           nueva_matriz = [[elem * otro for elem in fila] for fila in self._elementos]
           return MatrizCuadrada(nueva_matriz)
       # Multiplicación de matrices
       elif isinstance(otro, MatrizCuadrada):
           if len(self._elementos[0]) != len(otro.elementos):
               raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
           nueva_matriz = []
           for i in range(len(self._elementos)):
               fila_resultado = []
               for j in range(len(otro.elementos[0])):
                   suma = sum(self._elementos[i][k] * otro.elementos[k][j] for k in range(len(otro.elementos)))
                   fila_resultado.append(suma)
               nueva_matriz.append(fila_resultado)
           return MatrizCuadrada(nueva_matriz)
       else:
           raise ValueError("Operación no soportada")
       
if __name__ == '__main__':
    x = MatrizCuadrada([[1,2,3], [4,5,6], [7,8,9]])
    y = MatrizCuadrada([[1,0,1], [3,1,3], [2,0,0]])
    print(x)
    print(y)
    print(f'dimensión de x: {x.size()}')
    print(f'segunda fila de x: {x[1]}')
    print(f'primer elemento de x: {x[0][0]}')
    print(x + y)
    print(x - y)

    print(x*10)
    print(x*y)