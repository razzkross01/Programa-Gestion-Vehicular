# Validaciones de datos 
# -------------------------------------------------

def validar_patente(patente, vehiculos):
    """
    Valida que la patente sea válida y no esté duplicada.
    Retorna True o False.
    """
    if not isinstance(patente, str):
        return False

    patente = patente.strip().upper()

    for letra in patente[0:4]:
        if letra.isdigit():
            return False

    for letra in patente[4:6]:
        if letra.isalpha():
            return False    

    if patente == "":
        return False

    if patente in vehiculos:
        return False
    
    if len(patente) != 6:
        return False 
    
    return True


def validar_vehiculo(marca, modelo, color):
    """
    Valida los datos básicos de un vehículo.
    Retorna True o False.
    """
    if not isinstance(marca, str) or not isinstance(modelo, str) or not isinstance(color, str):
        return False

    

    if marca.strip() == "" or modelo.strip() == "" or color.strip() == "":
        return False

    return True

def validar_anio(anio):
    """
    Valida los datos básicos (año) de un vehículo.
    
    Retorna True o False.
    """
    if not isinstance(anio, int):
        return False

    if anio < 1900 or anio > 2026:
        return False

    return True


