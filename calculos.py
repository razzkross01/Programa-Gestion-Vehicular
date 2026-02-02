
# Funciones de cálculo (recursividad)


def calcular_permiso(anio_vehiculo, anio_actual, valor_actual, monto_minimo):
    """
    Calcula el valor del permiso de circulación usando recursividad.

    Parámetros:
    anio_vehiculo (int): año del vehículo
    anio_actual (int): año actual
    valor_actual (int): valor base inicial
    monto_minimo (int): monto mínimo permitido

    Retorna:
    int: valor final del permiso
    """

    # Caso base: si alcanzamos el año actual o el monto mínimo
    if anio_vehiculo >= anio_actual or valor_actual <= monto_minimo:
        return max(valor_actual, monto_minimo)

    # Caso recursivo: vehículo más antiguo, se reduce el valor
    return calcular_permiso(
        anio_vehiculo + 1,
        anio_actual,
        valor_actual - 10000,
        monto_minimo
    )
 