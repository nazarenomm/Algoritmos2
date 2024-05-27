

class EntradaConsola:
    def __init__(self, comandos: list[str]) -> None:
        self.comandos = comandos
    
    '''Retorna (funcion comando, [args])'''
    def parse(self, entrada: str) -> tuple:
        entrada_partes = entrada.strip().split(' ')
        comando = entrada_partes[0]
        
        if comando not in self.comandos:
            raise ValueError('Comando inexistente')
        
        return comando, entrada_partes[1:]

    def leer(self):
        entrada = input('Navegador> ')
        return self.parse(entrada)