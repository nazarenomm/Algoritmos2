
class Pagina:
    def __init__(
            self,
            nombre: str,
            contenido: str
         ) -> None:
        
        self.nombre = nombre
        self.contenido = contenido
        self.vinculos: dict[str, Vinculo] = {}


    def agregar_vinculo(self, label: str, destino: "Pagina"):
        self.vinculos[label] = Vinculo(label, destino)
    

    def obtener_pagina_vinculo(self, nombre: str) -> "Pagina":
        if nombre not in self.vinculos:
            raise ValueError('Vinculo inexistente')
        
        return self.vinculos[nombre].get_destino()

    def __str__(self):
        return f'''
        Pagina {self.nombre}\n 
        ------------------------------ \n
        {self.contenido} \n
        ------------ \n
        <Vinculos>: {list(self.vinculos.keys())}
        '''


class Vinculo:
    def __init__(self, label: str, destino: Pagina) -> None:
        self.label = label
        self.destino = destino

    def get_destino(self) -> Pagina:
        return self.destino
    
    def __str__(self):
        return self.label

