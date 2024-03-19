"""
Menus for the interface
"""

from printy import inputy
from .persona import Persona
from .tecnico import Tecnico
from .usuario import Usuario
from .servicio import SolicitudServicio

def menu_usuario():
    """Muestra opciones de menu para administrar usuarios"""
    # Diccionario que mapea una opción del menú con una acción (método de una clase)
    opciones_de_menu = {
        "Crear Usuario": Usuario.crear,
        "Actualizar Usuario": Usuario.actualizar,
        "Consultar Usuario": Usuario.consultar,
        "Eliminar Usuario": Usuario.eliminar,
        "Ver Todos Los Usuarios": Usuario.ver_objetos,
        "Volver a menú principal": menu_principal,
        "Salir": exit,
    }
    seleccion = inputy(
        "Selecciona una opción: ", "b", options=list(opciones_de_menu.keys())
    )

    # Ejecuta la acción de acuerdo a la opción seleccionada
    opciones_de_menu[seleccion]()

    # Una vez terminada la acción, volvemos a preguntar el menú
    menu_usuario()


def menu_tecnico():
    """Muestra opciones de menu para administrar técnicos"""
    # Diccionario que mapea una opción del menú con una acción (método de una clase)
    opciones_de_menu = {
        "Crear Técnico": Tecnico.crear,
        "Actualizar Técnico": Tecnico.actualizar,
        "Consultar Técnico": Tecnico.consultar,
        "Eliminar Técnico": Tecnico.eliminar,
        "Ver Todos Los Técnicos": Tecnico.ver_objetos,
        "Volver a menú principal": menu_principal,
        "Salir": exit,
    }
    seleccion = inputy(
        "Selecciona una opción: ", "y", options=list(opciones_de_menu.keys())
    )

    # Ejecuta la acción de acuerdo a la opción seleccionada
    opciones_de_menu[seleccion]()

    # Una vez terminada la acción, volvemos a preguntar el menú
    menu_tecnico()


def menu_solicitud():
    """Muestra opciones de menu para administrar solicitudes de servicio"""
    # Diccionario que mapea una opción del menú con una acción (método de una clase)
    opciones_de_menu = {
        "Crear Solicitud": SolicitudServicio.crear,
        # "Actualizar Técnico": Tecnico.actualizar,
        # "Consultar Técnico": Tecnico.consultar,
        # "Eliminar Técnico": Tecnico.eliminar,
        "Ver Todas las Solicitudes": SolicitudServicio.ver_objetos,
        "Volver a menú principal": menu_principal,
        "Salir": exit,
    }

    seleccion = inputy(
        "Selecciona una opción: ", "y", options=list(opciones_de_menu.keys())
    )

    # Ejecuta la acción de acuerdo a la opción seleccionada
    opciones_de_menu[seleccion]()

    # Una vez terminada la acción, volvemos a preguntar el menú
    menu_solicitud()


def menu_principal():
    # Diccionario que mapea una opción del menú con una acción (método de una clase)
    opciones_de_menu = {
        "Administrar Usuarios": menu_usuario,
        "Administrar Técnicos": menu_tecnico,
        "Administrar Solicitudes": menu_solicitud,
        "Salir": exit,
    }
    seleccion = inputy("Qué deseas hacer?", "mB", options=list(opciones_de_menu.keys()))

    # Ejecuta la acción de acuerdo a la opción seleccionada
    opciones_de_menu[seleccion]()

    # Una vez terminada la acción, volvemos a preguntar el menú
    menu_principal()
