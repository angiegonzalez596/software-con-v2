from printy import inputy, printy
from datetime import datetime
from .persona import Persona
from .usuario import Usuario

from .consts import *

class Tecnico(Persona):

    # Almacena las nuevas instancias creadas, la llave del
    # diccionario será el número de identificación.
    objects = {}

    CAMPOS = Persona.CAMPOS + ["disponible", "experiencia", "especialidad"]

    def __init__(
        self,
        identificacion: int,
        nombre: str,
        apellido: str,
        correo: str,
        telefono: str,
        ciudad: str,
        experiencia: int = 0,
        especialidad: str = DEFAULT_STR,
        # Este atributo será diligenciado programáticamente,
        # no por el usuario.
        disponible: bool = True,
    ) -> None:
        super().__init__(identificacion, nombre, apellido, correo, telefono, ciudad, experiencia, especialidad)

        self.disponible = disponible
        self.experiencia = experiencia
        self.especialidades = especialidad

    @classmethod
    def buscar_disponible(cls):
        """
        Obtiene cualquier técnico que esté disponible en el momento.
        """
        if disponible := list(filter(lambda x: x.disponible, cls.objects.values())):
            return disponible[0]

    def marcar_como_no_disponible(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True

    @staticmethod
    def solicitar_experiencia():
        return inputy(
            "Ingrese los años de experiencia del técnico (Presiona ENTER para omitir): ",
            QUESTION_COLOR,
            default=0,
        )

    @staticmethod
    def solicitar_especialidad():
        return inputy(
            "Ingrese la especialidad del técnico (Presiona ENTER para omitir): ",
            QUESTION_COLOR,
            default=0,
        )

    @classmethod
    def obtener_data(cls):
        """
        Solicita la información del tecnico.
        """
        data = super(Tecnico, cls).obtener_data()
        # Agrega los datos que son exclusivos del objeto Usuario
        data["experiencia"] = cls.solicitar_experiencia()
        data["especialidad"] = cls.solicitar_especialidad()
        return data

    @classmethod
    def actualizar(cls) -> str:
        """
        Actualiza la información de un tecnico basado en su número de
        identificación.
        """
        printy("ACTUALIZANDO UN TECNICO")
        super(Tecnico, cls).actualizar()

    @classmethod
    def crear(cls):
        """
        Abre una interfaz de usuario en consola para ingresar datos
        y crear un nuevo usuario.
        """
        printy("CREANDO UN NUEVO TÉCNICO", TITLE_COLOR)
        # objeto usuario
        usuario = super(Tecnico, cls).crear()
        printy("Técnico creado con éxito!", SUCCESS_COLOR)
        printy(usuario.as_dict())