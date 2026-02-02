# Funciones de gestión de vehículos
# -------------------------------------------------

def buscar_patente(patente, vehiculos):
    """
    Verifica si una patente existe en el sistema.
    Retorna True o False.
    """
    patente = patente.strip().upper()
    return patente in vehiculos


def obtener_datos(patente, vehiculos):
    """
    Retorna los datos del vehículo.
    Retorna None si no existe.
    """
    patente = patente.strip().upper()
    return vehiculos.get(patente)


def tiene_deuda(patente, vehiculos):
    """
    Verifica si el vehículo tiene deuda.
    Retorna True o False.
    """
    patente = patente.strip().upper()

    if patente not in vehiculos:
        return False

    return vehiculos[patente]["tiene_deuda"]

def permiso_pagado(patente, vehiculos):
    """
    Verifica si el vehículo pago el permiso.
    Retorna True o False.
    """
    patente = patente.strip().upper()

    if patente not in vehiculos:
        return False

    return vehiculos[patente]["permiso_pagado"]


def registrar_vehiculo(patente, marca, modelo, color, anio, vehiculos):
    """
    Registra un nuevo vehículo en el sistema.
    Retorna True si se registra, False si ya existe.
    """
    patente = patente.strip().upper()

    if patente in vehiculos:
        return False

    vehiculos[patente] = {
        "marca": marca.strip(),
        "modelo": modelo.strip(),
        "color": color.strip(),
        "anio": anio,
        "tiene_deuda": False,
        "monto_deuda": 0,
        "permiso_pagado": False,
        "valor_permiso": 0
    }

    return True


def pago_deuda(patente, vehiculos):
    """
    Registra el pago de la deuda del vehículo.
    Retorna True si se paga, False si no corresponde.
    """
    patente = patente.strip().upper()

    if patente not in vehiculos:
        return False

    if not vehiculos[patente]["tiene_deuda"]:
        return False

    vehiculos[patente]["tiene_deuda"] = False
    vehiculos[patente]["monto_deuda"] = 0

    return True


def pagar_permiso(patente, vehiculos, valor_permiso):
    """
    Registra el pago del permiso de circulación.
    Retorna True si se paga, False si no corresponde.
    """
    patente = patente.strip().upper()

    if patente not in vehiculos:
        return False

    if vehiculos[patente]["tiene_deuda"]:
        return False

    if vehiculos[patente]["permiso_pagado"]:
        return False

    vehiculos[patente]["permiso_pagado"] = True
    vehiculos[patente]["valor_permiso"] = valor_permiso

    return True


def listar_vehiculos(vehiculos):
    """
    Retorna una lista de patentes registradas.
    """
    return list(vehiculos.keys())