import os
os.system("cls")

from validaciones import (
    validar_patente, 
    validar_vehiculo, 
    validar_anio)

from vehiculos import (
    buscar_patente,
    obtener_datos,
    registrar_vehiculo,
    pago_deuda,
    permiso_pagado,
    pagar_permiso,
    tiene_deuda,
    listar_vehiculos
)

from calculos import calcular_permiso

MENU_OPCIONES = (
    "1. Registrar vehículo",
    "2. Pagar deuda",
    "3. Pagar permiso de circulación",
    "4. Mostrar datos del vehículo",
    "5. Listar vehículos registrados",
    "6. Salir"
)

vehiculos = {
    "ABCD12": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "color": "Blanco",
        "anio": 2018,
        "tiene_deuda": False,
        "monto_deuda": 0,
        "permiso_pagado": False,
        "valor_permiso": 0
    },
    "WXYZ34": {
        "marca": "Hyundai",
        "modelo": "Accent",
        "color": "Gris",
        "anio": 2015,
        "tiene_deuda": True,
        "monto_deuda": 120000,
        "permiso_pagado": False,
        "valor_permiso": 0
    }
}


def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN VEHICULAR ---")
    for opcion in MENU_OPCIONES:
        print(opcion)
    

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            os.system("cls")
            print("\n--- REGISTRO DE VEHÍCULO ---")

            while True:

                patente = input("Patente: ")

                if not validar_patente(patente, vehiculos):
                    print("Patente inválida o duplicada.")
                    continue

                marca = input("Marca: ")
                modelo = input("Modelo: ")
                color = input("Color: ")
                anio = int(input("Año: "))

                if not validar_anio(anio):
                    print("Ingrese un año valido")
                    continue

                if not validar_vehiculo(marca, modelo, color):
                    print("Datos del vehículo inválidos.")
                    continue

                if registrar_vehiculo(patente, marca, modelo, color, anio, vehiculos):
                    print("Vehículo registrado correctamente.")
                    break
                else:
                    print("No se pudo registrar el vehículo.")


        elif opcion == "2":
            os.system("cls")
            print("\n--- PAGO DE DEUDA ---")
            patente = input("Ingrese patente: ").strip().upper()

            while True:
                if  tiene_deuda(patente, vehiculos):
                    print(f"La deuda de su vehiculo es: {vehiculos[patente]['monto_deuda']}")
                    print ("1.- Pagar")
                    print ("2.- Salir")

                    opcion2 = input("Seleccione una opción: ").strip()

                    if opcion2 == "1":
                        if pago_deuda(patente, vehiculos):
                            print("Deuda pagada correctamente.")
                            break
                    elif opcion2 == "2":
                        break
                else:        
                    print("Su vehículo no cuenta con deuda.")
                    break

        elif opcion == "3":
            os.system("cls")

            while True: 
                print("\n--- PAGO PERMISO DE CIRCULACIÓN ---")
                patente = input("Ingrese patente: ")

                if not buscar_patente(patente, vehiculos):
                    print("Patente no encontrada.")
                    continue

                if tiene_deuda(patente, vehiculos):
                    print("El vehículo tiene deuda pendiente.")

                    opcion_volver = input("¿Desea ingresar otra patente? (si/no): ").strip().lower()

                    if opcion_volver == "si":
                        continue
                    else:
                        break

                if permiso_pagado(patente, vehiculos):
                    print("El vehículo ya pago el permiso.")
                    break

                datos = obtener_datos(patente, vehiculos)

                valor = calcular_permiso(
                    datos["anio"],
                    2026,
                    200000,
                    50000
                )
                print (f"El valor de su permiso es: {valor}")
                print ("1.- Pagar")
                print ("2.- Salir")

                opcion2 = input("Seleccione una opción: ").strip()

                if opcion2 == "1":
                    os.system("cls")
                    if pagar_permiso(patente, vehiculos, valor):
                        print(f"Permiso pagado correctamente. Valor: ${valor}")
                        break

                elif opcion2 == "2":        
                        break

                else:
                    print("No fue posible pagar el permiso.")
                    break

        elif opcion == "4":
            os.system("cls")
            print("\n--- Mostrar datos del vehiculo ---")

            patente = input("Ingrese patente: ")


            datos = obtener_datos(patente, vehiculos)

            if datos is None:
                print("Patente no encontrada.")
            else:
                print("\n---Datos del vehículo---")
                print(f"Patente: {patente.strip().upper()}")
                print(f"Marca: {datos['marca']}")
                print(f"Modelo: {datos['modelo']}")
                print(f"Color: {datos['color']}")
                print(f"Año: {datos['anio']}")
                print(f"Tiene deuda: {'Sí' if datos['tiene_deuda'] else 'No'}")
                print(f"Monto deuda: ${datos['monto_deuda']}")
                print(f"Permiso pagado: {'Sí' if datos['permiso_pagado'] else 'No'}")

                if datos["permiso_pagado"]:
                    print(f"Valor permiso: ${datos['valor_permiso']}")
                
        elif opcion == "5":
            os.system("cls")
            print("\n--- VEHÍCULOS REGISTRADOS ---")

            lista_patentes = set(listar_vehiculos(vehiculos))


            if not lista_patentes:
                print("No hay vehículos registrados.")
            else:
                for patente in lista_patentes:
                    print(f"- {patente}")


        elif opcion == "6":
            os.system("cls")
            print("Saliendo del sistema...")
            
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
