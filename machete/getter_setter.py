class clase():
    def __init__(self, _nombre_atributo):
        self._nombre_atributo = _nombre_atributo

    # getter
    @property
    def nombre_atributo(self):
        return self._nombre_atributo

    # setter, si no lo definis no vas a poder settear el atributo sin usar guion bajo
    @nombre_atributo.setter
    def nombre_atributo(self, valor):
        self._nombre_atributo = valor