from typing import Set, Optional
from printy import inputy, printy
from datetime import datetime
from .persona import Persona
from .usuario import Usuario
from .tecnico import Tecnico

from .consts import *


class SolicitudServicio:

    # Diccionario que almacenará todas las solicitudes, cuyas llaves será un
    # entero autoincremental.
    objects = {}

    # Cada vez que se cree una nueva instancia se aumentará en 1
    last_key = 0

    # Opciones de Estados
    ESTADO_ABIERTA = "Abierta"
    ESTADO_ASIGNADA = "Asignada"
    ESTADO_EN_PROGRESO = "En Progreso"
    ESTADO_FINALIZADA = "Finalizada"

    # Opciones de vía de soporte
    VIA_SOPORTE_VIRTUAL = "Virtual"
    VIA_SOPORTE_PRESENCIAL = "Presencial"

    # Opciones de Sistemas operativos
    SO_WINDOWS = "Windows"
    SO_LINUX = "Linux"
    SO_IOS = "IOs"

    # Opciones procesador
    PROCESADOR_INTEL = "Intel"
    PROCESADOR_AMD = "AMD"

    def __init__(
        self,
        usuario: Usuario,
        via_soporte: str,
        # Los siguientes atributos son opcionales, y se pueden diligenciar
        # luego de haber creado la solicitud (en campo, por ejemplo).
        # Datos Equipo:
        marca: Optional[str] = DEFAULT_STR,
        sn: Optional[str] = DEFAULT_STR,
        ram: Optional[int] = DEFAULT_STR,
        disco_duro: Optional[int] = DEFAULT_STR,
        so: Optional[str] = DEFAULT_STR,
        modelo: Optional[str] = DEFAULT_STR,
        procesador: Optional[str] = DEFAULT_STR,
        cores: Optional[int] = DEFAULT_STR,
        # incidencias:
        error_software: Optional[bool] = False,
        error_hardware: Optional[bool] = False,
        error_red: Optional[bool] = False,
        error_seguridad: Optional[bool] = False,
        error_usuario: Optional[bool] = False,
        error_critico: Optional[bool] = False,
    ) -> None:

        # Obtenemos la llave actual, que es la última mas uno
        key = SolicitudServicio.last_key + 1

        # Asignamos el número de servicio
        self.numero_servicio = key

        self.tecnico = Tecnico.buscar_disponible()
        self.estado = self.marcar_como_abierta()
        # Si hay técnico disponible, el estado se cambia a Asignada
        if self.tecnico:
            self.tecnico.marcar_como_no_disponible()
            self.marcar_como_asignada()

        self.usuario = usuario
        self.via_soporte = via_soporte
        self.fecha = datetime.now()

        self.marca = marca
        self.sn = sn
        self.ram = ram
        self.disco_duro = disco_duro
        self.so = so
        self.modelo = modelo
        self.procesador = procesador
        self.cores = cores
        self.error_software = error_software
        self.error_hardware = error_hardware
        self.error_red = error_red
        self.error_seguridad = error_seguridad
        self.error_usuario = error_usuario
        self.error_critico = error_critico

        # Guardamos el objeto
        #################################################
        self.objects[key] = self
        # Guarnamos la última llave
        SolicitudServicio.last_key = key

    def __str__(self):
        return f"Solicitud # {self.numero_servicio} - {self.fecha.isoformat()} - {self.usuario}"

    def marcar_como_abierta(self):
        """Cambia el estado de la solicitud a ABIERTA"""
        self.estado = self.ESTADO_ABIERTA

    def marcar_como_asignada(self):
        """cambia el estado de la solicitud a ASIGNADA"""
        self.estado = self.ESTADO_ASIGNADA

    def marcar_como_en_progreso(self):
        """cambia el estado de la solicitud a EN_PROGRESO"""
        self.estado = self.ESTADO_EN_PROGRESO

    def marcar_como_finalizada(self):
        """cambia el estado de la solicitud a FINALIZADA"""
        self.estado = self.ESTADO_FINALIZADA

    @staticmethod
    def solicitar_usuario():
        return inputy(
            "Ingrese la identifiación del usuario: ", QUESTION_COLOR, type="int"
        )

    @classmethod
    def solicitar_via_soporte(cls):
        return inputy(
            "Ingrese la via de soporte: ",
            QUESTION_COLOR,
            options=[cls.VIA_SOPORTE_PRESENCIAL, cls.VIA_SOPORTE_VIRTUAL],
        )

    # Metodos para solicitar información del equipo

    @staticmethod
    def solicitar_marca():
        return inputy("Ingrese la marca del equipo: ", QUESTION_COLOR)

    @staticmethod
    def solicitar_sn():
        return inputy("Ingrese el número de serial del equipo: ", QUESTION_COLOR)

    @classmethod
    def solicitar_ram(cls):
        return inputy(
            "Ingrese la memoria RAM del equipo (en MB): ", QUESTION_COLOR, type="int"
        )

    @staticmethod
    def solicitar_disco_duro():
        return inputy(
            "Ingrese el disco duro del equipo (en MB): ", QUESTION_COLOR, type="int"
        )

    @classmethod
    def solicitar_so(cls):
        return inputy(
            "Ingrese el sistema operativo del equipo: ",
            QUESTION_COLOR,
            options=[cls.SO_WINDOWS, cls.SO_LINUX, cls.SO_IOS],
        )

    @staticmethod
    def solicitar_modelo():
        return inputy("Ingrese el modelo del equipo: ", QUESTION_COLOR)

    @classmethod
    def solicitar_procesador(cls):
        return inputy(
            "Ingrese el procesador del equipo: ",
            QUESTION_COLOR,
            options=[cls.PROCESADOR_INTEL, cls.PROCESADOR_AMD],
        )

    @staticmethod
    def solicitar_cores():
        return inputy(
            "Ingrese el número de CORES del equipo: ", QUESTION_COLOR, type="int"
        )

    # Metodos para solicitar información de la incidencia

    @staticmethod
    def solicitar_error_software():
        return inputy(
            "Fue un error de software? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @staticmethod
    def solicitar_error_hardware():
        return inputy(
            "Fue un error en el hardware? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @staticmethod
    def solicitar_error_red():
        return inputy(
            "Fue un error de red? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @staticmethod
    def solicitar_error_de_seguridad():
        return inputy(
            "Fue un error de seguridad? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @staticmethod
    def solicitar_error_usuario():
        return inputy(
            "Fue un error del usuario? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @staticmethod
    def solicitar_error_critico():
        return inputy(
            "Fue un error crítico? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
            default=False,
        )

    @classmethod
    def obtener_data_equipo(cls):
        """
        Obtiene la información del equipo
        """
        data = {}
        data["marca"] = cls.solicitar_marca()
        data["sn"] = cls.solicitar_sn()
        data["ram"] = cls.solicitar_ram()
        data["disco_duro"] = cls.solicitar_disco_duro()
        data["so"] = cls.solicitar_so()
        data["modelo"] = cls.solicitar_modelo()
        data["procesador"] = cls.solicitar_procesador()
        data["cores"] = cls.solicitar_cores()

        return data

    @classmethod
    def obtener_data_incidencia(cls):
        """
        Obtiene la información de la incidencia
        """
        data = {}
        data["error_software"] = cls.solicitar_error_software()
        data["error_hardware"] = cls.solicitar_error_hardware()
        data["error_red"] = cls.solicitar_error_red()
        data["error_seguridad"] = cls.solicitar_error_seguridad()
        data["error_usuario"] = cls.solicitar_error_usuario()
        data["error_critico"] = cls.solicitar_error_critico()

        return data

    @classmethod
    def obtener_data(cls):
        """
        Obtiene la información inicial para crear una solicitud.
        Solo el usuario y la via de soporte son requeridos para crear
        una nueva solicitud. Los demás datos son opcionales.
        """
        data = {}

        # Solicitamos la identificación del usuario, si existe, retornamos
        # el objeto usuario, si no, seguimos preguntando.
        valid_id = False
        while not valid_id:
            usuario_id = cls.solicitar_usuario()
            if usuario_id in Usuario.objects:
                valid_id = True
                data["usuario"] = Usuario.objects[usuario_id]
            else:
                print("No existe ningún usuario con ese número de identificación")
        data["via_soporte"] = cls.solicitar_via_soporte()

        # Si deseamos agregar la información del equipo al momento de crear
        # la solicitud, procedemos a preguntar esta información.
        if inputy(
            "Desea agregar la información del equipo? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
        ):
            data.update(cls.obtener_data_equipo())

        # Si deseamos agregar la información de la incidencia al momento de crear
        # la solicitud, procedemos a preguntar esta información.
        if inputy(
            "Desea agregar la información de la incidencia? ",
            QUESTION_COLOR,
            type="bool",
            options=["y", "n"],
            condition="i",
        ):
            data.update(cls.obtener_data_incidencia())

        return data

    @classmethod
    def crear(cls):
        """
        Crea una nueva solicitud de servicio
        """
        printy("CREANDO UNA NUEVA SOLICITUD DE SERVICIO", TITLE_COLOR)
        data = cls.obtener_data()
        # nueva instancia de clase
        objeto = cls(**data)
        printy("La solicitud fue creada con éxito", SUCCESS_COLOR)
        return objeto

    @classmethod
    def ver_objetos(cls):
        """imprime en pantalla el diccionario de objetos"""
        printy(cls.objects)
        