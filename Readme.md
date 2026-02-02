# Sistema de Gestión Vehicular 

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión vehicular en consola, implementado en Python, que permite registrar vehículos, gestionar deudas, calcular el permiso de circulación y mostrar información asociada a cada vehículo.

---

## Objetivo

Diseñar e implementar un sistema de gestión de datos que:

- Permita registrar vehículos identificados por su patente
- Gestione deudas asociadas a los vehículos
- Calcule el permiso de circulación utilizando recursividad
- Registre el pago del permiso
- Visualice información completa de un vehículo


---

## Estructura del proyecto

```text
gestion_vehicular/
│
├── main.py              # Flujo principal del programa y menú
├── validaciones.py      # Validaciones de datos de entrada
├── vehiculos.py         # Gestión y manipulación de vehículos
├── calculos.py          # Cálculo recursivo del permiso
├── pruebas_sistema_gestion_vehicular.txt
└── README.md

Estructura de datos utilizada
Cada vehículo se almacena en un diccionario con la siguiente estructura:

python
Copiar código
{
    "marca": str,
    "modelo": str,
    "color": str,
    "anio": int,
    "tiene_deuda": bool,
    "monto_deuda": int,
    "permiso_pagado": bool,
    "valor_permiso": int
}
Los vehículos se almacenan en un diccionario principal donde la patente es la clave única:

python
Copiar código
vehiculos = {
    "PATENTE": {datos_del_vehiculo}
}