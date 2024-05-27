from pagina import Pagina
from internechi import Internechi
from entrada_consola import EntradaConsola
from salida_consola import SalidaConsola

class Navegador:
    def __init__(self, web: Internechi) -> None:
        # TODO: historia
        # self.historial = Historial()
        self.home: Pagina = Pagina('HOME','HOME MI NAVEGADOR')
        self.pagina_actual: Pagina = self.home
        self.operaciones = {
            'abrir': self.abrir_pagina,
            'ir': self.ir_vinculo,
            'cerrar': self.cerrar,
            'atras': self.atras,
            'adelante': self.adelante,
        }
        self.entrada = EntradaConsola(list(self.operaciones.keys()))
        self.salida = SalidaConsola()
        self.web = web


    def set_home(self, nombre: str):
        try:
            self.home = self.web.obtener_pagina(nombre)
        except ValueError:
            raise ValueError('Pagina inexistente')

    def abrir_pagina(self, nombre: str):
        try:
            self.pagina_actual = self.web.obtener_pagina(nombre)
        except ValueError:
            self.salida.mostrar_error('Pagina no encontrada')

    def ir_vinculo(self, nombre_vinculo: str):
        try:
            self.pagina_actual = self.pagina_actual.obtener_pagina_vinculo(
                nombre_vinculo
            )
        except ValueError:
            self.salida.mostrar_error('Vinculo inexistente')


    def cerrar(self):
        pass

    def atras(self):
        pass

    def adelante(self):
        pass

    def run(self):
        comando = ''
        while comando != 'cerrar':
            try:
                self.salida.mostrar(self.pagina_actual)
                comando, argumentos = self.entrada.leer()
                # TODO: mejorar
                if argumentos:
                    self.operaciones[comando](argumentos[0])
                else:
                    self.operaciones[comando]()
            except ValueError as e:
                self.salida.mostrar_error(e.__str__())

