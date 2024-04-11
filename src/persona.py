from typing import Set, Optional
from printy import inputy, printy
from datetime import datetime

from .consts import *

class Persona:
    """
    Clase abstracta de la cual heredarán Usuario y Tecnico,
    incluye algunos métodos base.
    """

    # Lista los nombres de los campos de la clase.
    # Útil al momento de solicitar información del
    # ususario en consola.
    CAMPOS = [
        "identificacion",
        "nombre",
        "apellido",
        "correo",
        "telefono",
        "ciudad",
    ]

    # Almacena las nuevas instancias creadas, la llave del
    # diccionario será el número de identificación.
    objects = {}

    def __init__(
        self,
        identificacion: int,
        nombre: str,
        apellido: str,
        correo: str,
        telefono: str,
        ciudad: str,
    ) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.ciudad = ciudad

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.correo})"

    def as_dict(self):
        """
        Retorna la información de la Persona como un diccionario.
        """
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono,
            "ciudad": self.ciudad,
        }

    @classmethod
    def ver_objetos(cls):
        """imprime en pantalla el diccionario de objetos"""
        printy(cls.objects)

    @staticmethod
    def solicitar_identificacion():
        return inputy("Ingrese la identifiación: ", QUESTION_COLOR, type="int")

    @staticmethod
    def solicitar_nombre():
        return inputy("Ingrese el nombre: ", QUESTION_COLOR)

    @staticmethod
    def solicitar_apellido():
        return inputy("Ingrese el apellido: ", QUESTION_COLOR)

    @staticmethod
    def solicitar_correo():
        return inputy("Ingrese el correo: ", QUESTION_COLOR)

    @staticmethod
    def solicitar_telefono():
        return inputy("Ingrese el telefono: ", QUESTION_COLOR)

    @staticmethod
    def solicitar_ciudad():
        return inputy("Ingrese la ciudad: ", QUESTION_COLOR)

    @classmethod
    def obtener_data(cls):
        """
        Obtiene la información relevante de la persona
        y devuelve un diccionario con esta.
        """
        data = {}

        # Dado que el valor de `identificacion` es la llave en el diccionario
        # de objetos creados, debemos validar si no existe primero.
        valid_id = False
        while not valid_id:
            identificacion = cls.solicitar_identificacion()
            if identificacion not in cls.objects:
                valid_id = True
                data["identificacion"] = identificacion
            else:
                print("Ya existe un usuario con esa identificacion")
        data["nombre"] = cls.solicitar_nombre()
        data["apellido"] = cls.solicitar_apellido()
        data["correo"] = cls.solicitar_correo()
        data["telefono"] = cls.solicitar_telefono()
        data["ciudad"] = cls.solicitar_ciudad()
        return data

    @classmethod
    def crear(cls):
        """
        Obtiene los datos y crea un nuevo objeto Persona, y lo almacena.
        """
        data = cls.obtener_data()
        # nueva instancia de clase
        objeto = cls(**data)
        # Agrega el nuevo objeto creado al objeto que almacena
        # todos las Personas.
        cls.objects[data["identificacion"]] = objeto
        return objeto

    @classmethod
    def consultar(cls) -> str:
        """
        Consulta la información de una Persona basado en su número de
        identificación y la imprime en pantalla.
        """
        try:
            identificacion = cls.solicitar_identificacion()
            # Imprime en pantalla la información de la persona
            printy(cls.objects[identificacion].as_dict())
        except KeyError:
            intentar_de_nuevo = inputy(
                "No existe un objecto con el número de identifiación ingresado. "
                "Desea realizar otra consulta?",
                WARNING_COLOR,
                type="bool",
                options=["y", "n"],
                condition="i",
            )
            if intentar_de_nuevo:
                cls.consultar()

    @classmethod
    def eliminar(cls) -> str:
        """
        Elimina una Persona de la lista de personas existentes
        basado en su número de identificación.
        """
        try:
            identificacion = cls.solicitar_identificacion()
            printy(
                f"'{cls.objects[identificacion]}' eliminado con éxito",
                SUCCESS_COLOR,
            )
            del cls.objects[identificacion]
        except KeyError:
            intentar_de_nuevo = inputy(
                "No existe un objecto con el número de identifiación ingresado. "
                "Desea intentarlo de nuevo?",
                WARNING_COLOR,
                type="bool",
                options=["y", "n"],
                condition="i",
            )
            if intentar_de_nuevo:
                cls.eliminar()

    @classmethod
    def actualizar(cls) -> str:
        """
        Actualiza la información de una persona basado en su número de
        identificación.
        """
        try:
            identificacion = cls.solicitar_identificacion()
            objeto = cls.objects[identificacion]
            campo_a_actualizar = inputy(
                "Qué campo desea actualizar? ", options=cls.CAMPOS
            )
            nuevo_valor = inputy(
                f"Ingrese el nuevo valor (antes '{getattr(objeto, campo_a_actualizar)}'): "
            )
            confirmacion = inputy(
                f"Está seguro de que quiere realizar esta actualización?: ",
                WARNING_COLOR,
                type="bool",
                options=["y", "n"],
                condition="i",
            )
            if confirmacion:
                setattr(objeto, campo_a_actualizar, nuevo_valor)
                printy("Objeto actualizado con éxito!", SUCCESS_COLOR)
                printy(objeto.as_dict())
                intentar_de_nuevo = inputy(
                    "Deseas actualizar otro campo? ",
                    WARNING_COLOR,
                    type="bool",
                    options=["y", "n"],
                    condition="i",
                )
                if intentar_de_nuevo:
                    cls.actualizar()
        except KeyError:
            intentar_de_nuevo = inputy(
                "No existe un objeto con el número de identifiación ingresado. "
                "Desea intentarlo de nuevo?",
                WARNING_COLOR,
                type="bool",
                options=["y", "n"],
                condition="i",
            )
            if intentar_de_nuevo:
                cls.actualizar()