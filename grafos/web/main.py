from internechi import Internechi
from navegador import Navegador
from pagina import Pagina

def crear_internechi():
    internechi = Internechi()
    google = Pagina('google', 'Esto es google')
    unsam = Pagina('unsam', 'Esto es unsam')
    duck = Pagina('duck', 'Esto es duck')
    github = Pagina('github', 'Esto es github')
    ubuntu = Pagina('ubuntu', 'Esto es ubuntu')

    google.agregar_vinculo('unsam', unsam)
    google.agregar_vinculo('duck', duck)
    google.agregar_vinculo('github', github)
    google.agregar_vinculo('ubuntu', ubuntu)

    duck.agregar_vinculo('unsam', unsam)
    duck.agregar_vinculo('google', google)
    duck.agregar_vinculo('github', github)
    duck.agregar_vinculo('ubuntu', ubuntu)

    ubuntu.agregar_vinculo('unsam', unsam)
    ubuntu.agregar_vinculo('google', google)
    github.agregar_vinculo('ubuntu', ubuntu)
    unsam.agregar_vinculo('github', github)

    internechi.agregar_pagina(google)
    internechi.agregar_pagina(unsam)
    internechi.agregar_pagina(duck)
    internechi.agregar_pagina(github)
    internechi.agregar_pagina(ubuntu)

    return internechi

def main():
    navegador = Navegador(crear_internechi())
    navegador.run()

if __name__ == '__main__':
    main()