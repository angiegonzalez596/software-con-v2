from .persona import Persona
from .servicio import SolicitudServicio
from .tecnico import Tecnico
from .usuario import Usuario
from abc import ABC, abstractmethod

def inicializar():
    """
    Agrega información inicial en memoria, para no tener que
    agregar todo desde cero sino que podamos tener algo con
    qué empezar una demostración del software.
    """
    # Primero Creamos unos cuantos usuarios
    
    usuario_1 = Usuario(
        identificacion=12345,
        nombre="Juan",
        apellido="Perez",
        correo="juanperez@gmail.com",
        telefono="+57 301 000 1010",
        ciudad="Bogotá D.C.",
        empresa="Panadería Don Juan",
        cargo="Gerente",
    )
    usuario_2 = Usuario(
        identificacion=98765,
        nombre="Marcos",
        apellido="Cortéz",
        correo="marcortez@gmail.com",
        telefono="+57 310 111 1111",
        ciudad="Medellín, Antioquia",
        empresa="Drogas La Popular",
        cargo="Asistente de gerencia",
    )
    # Agregamos los usuarios a la lista
    Usuario.objects[usuario_1.identificacion] = usuario_1
    Usuario.objects[usuario_2.identificacion] = usuario_2

    # Creamos unos cuandos Técnicos
    tecnico_1 = Tecnico(
        identificacion=23456,
        nombre="Angie",
        apellido="Gonzalez",
        correo="angiegonzalez@gmail.com",
        telefono="+57 320 200 2020",
        ciudad="Bogotá D.C.",
        experiencia=2,
        especialidad="redes",
        disponible=False,
    )
    tecnico_2 = Tecnico(
        identificacion=78906,
        nombre="Jhonatan",
        apellido="Rodriguez",
        correo="jhonatanrod@gmail.com",
        telefono="+57 315 034 6789",
        ciudad="Bogotá D.C.",
        experiencia=6,
        especialidad="sistema",
        disponible=True,
    )
    # Agregamos los técnicos a la lista
    Tecnico.objects[tecnico_1.identificacion] = tecnico_1
    Tecnico.objects[tecnico_2.identificacion] = tecnico_2

    # Creamos una solicitud
    s = SolicitudServicio(
        usuario=usuario_1,
        via_soporte="chat",
        marca="Dell",
        sn="12123123",
        ram=1024,
        disco_duro=1024,
        so="Windows",
        modelo="Vostro 14",
        procesador="intel core i5",
        cores=8,
        error_software=False,
        error_hardware=True,
        error_red=False,
        error_seguridad=False,
        error_usuario=False,
        error_critico=False,
    )
    s.marcar_como_finalizada()