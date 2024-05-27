from pagina import Pagina

class SalidaConsola:
    def __init__(self) -> None:
        pass

    def mostrar(self, pagina: Pagina):
        print(pagina)

    def mostrar_error(self, error: str):
        print(f'ERROR! {error}')