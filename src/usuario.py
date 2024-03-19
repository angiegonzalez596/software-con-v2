from typing import Set, Optional
from printy import inputy, printy
from datetime import datetime
from .persona import Persona

from .consts import *

class Usuario(Persona):

    # Almacena las nuevas instancias creadas, la llave del
    # diccionario será el número de identificación.
    objects = {}

    CAMPOS = Persona.CAMPOS + ["empresa", "cargo"]

    def __init__(
        self,
        identificacion: int,
        nombre: str,
        apellido: str,
        correo: str,
        telefono: str,
        ciudad: str,
        empresa: Optional[str] = DEFAULT_STR,
        cargo: Optional[str] = DEFAULT_STR,
    ) -> None:
        super().__init__(identificacion, nombre, apellido, correo, telefono, ciudad)

        self.empresa = empresa
        self.cargo = cargo

    def as_dict(self):
        data = super().as_dict()
        data["empresa"] = self.empresa
        data["cargo"] = self.cargo

        return data

    @staticmethod
    def solicitar_empresa():
        return inputy(
            "Ingrese el nombre de la empresa (Presiona ENTER para omitir): ",
            QUESTION_COLOR,
            default=DEFAULT_STR,
        )

    @staticmethod
    def solicitar_cargo():
        return inputy(
            "Ingrese el cargo dentro de la empresa (Presiona ENTER para omitir): ",
            QUESTION_COLOR,
            default=DEFAULT_STR,
        )

    @classmethod
    def obtener_data(cls):
        """
        Solicita la información del usuario.
        """
        data = super(Usuario, cls).obtener_data()
        # Agrega los datos que son exclusivos del objeto Usuario
        data["empresa"] = cls.solicitar_empresa()
        data["cargo"] = cls.solicitar_cargo()
        return data

    @classmethod
    def actualizar(cls) -> str:
        """
        Actualiza la información de un usuario basado en su número de
        identificación.
        """
        printy("ACTUALIZANDO UN USUARIO")
        super(Usuario, cls).actualizar()

    @classmethod
    def crear(cls):
        """
        Abre una interfaz de usuario en consola para ingresar datos
        y crear un nuevo usuario.
        """
        printy("CREANDO UN NUEVO USUARIO", TITLE_COLOR)
        # objeto usuario
        usuario = super(Usuario, cls).crear()
        printy("Usuario creado con éxito!", SUCCESS_COLOR)
        printy(usuario.as_dict())