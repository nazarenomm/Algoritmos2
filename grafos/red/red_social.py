# Practica para el parcial

from typing import TypeVar

from grafos.grafo import Arista

T = TypeVar("T")

class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None: #sarasa
        self.nombre = nombre
        self._contraseña = contraseña

    @property
    def contraseña(self):
        return self._contraseña
    
    @contraseña.setter
    def contraseña(self, nueva: str):
        # TODO: contraseña no lo suficiente segura etc
        self._contraseña = nueva


class Amistad(Arista): # arista simple
    def __init__(self, usuario1: Usuario, usuario2: Usuario) -> None:
        super().__init__(usuario1, usuario2)



class Seguimiento(Arista): # arista con direccion
    def __init__(self, seguidor, seguido) -> None:
        super().__init__(seguidor, seguido, direccionada = True)


        
class RedSocial:
    def __init__(self) -> None:
        self.usuarios: list[Usuario] = []
        self.amistades: list[Amistad] = []
        self.seguimientos: list[Seguimiento] = []

    def agregar_usuario(self, usuario: Usuario) -> None:
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
        else:
            raise ValueError("Usuario existente")
        
    def eliminar_usuario(self, usuario: Usuario):
        pass

    
