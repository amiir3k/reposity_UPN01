import os
from datetime import datetime


expedientes = []

ARCHIVO = "expedientes.txt"


def cargar_expedientes():
    if not os.path.exists(ARCHIVO):
        return

    lineas_malas = 0

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) != 6:
                lineas_malas += 1
                continue

            expediente = {
                "codigo": datos[0],
                "dni": datos[1],
                "nombre": datos[2],
                "area": datos[3],
                "asunto": datos[4],
                "fecha": datos[5]
            }
            expedientes.append(expediente)

    if lineas_malas > 0:
        print("Líneas omitidas por formato incorrecto:", lineas_malas)


def guardar_expedientes():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for e in expedientes:
            linea = e["codigo"] + ";" + e["dni"] + ";" + e["nombre"] + ";" + e["area"] + ";" + e["asunto"] + ";" + e["fecha"]
            archivo.write(linea + "\n")


def registrar_expediente():
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("El código ya se encuentra registrado.")
            return

    dni = input("Ingrese el DNI del paciente: ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe contener 8 números.")
        return

    nombre = input("Ingrese el nombre del paciente: ").strip()
    area = input("Ingrese el área médica: ").strip()
    asunto = input("Ingrese el asunto del expediente: ").strip()

    if codigo == "" or nombre == "" or area == "" or asunto == "":
        print("Todos los campos son obligatorios.")
        return

    if ";" in nombre or ";" in area or ";" in asunto:
        print("No use el carácter ; en los datos.")
        return

    nuevo_expediente = {
        "codigo": codigo,
        "dni": dni,
        "nombre": nombre,
        "area": area,
        "asunto": asunto,
        "fecha": datetime.now().strftime("%d/%m/%Y")
    }

    expedientes.append(nuevo_expediente)
    guardar_expedientes()

    print("\n¡Expediente registrado correctamente!")


def eliminar_expediente():
    print("\n--- ELIMINAR EXPEDIENTE ---")

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expedientes.remove(expediente)
            guardar_expedientes()

            print("Expediente eliminado correctamente.")
            return

    print("No se encontró el expediente.")


def mostrar_expediente(expediente):
    print("\n------------------------------")
    print("Código:", expediente["codigo"])
    print("DNI:", expediente["dni"])
    print("Paciente:", expediente["nombre"])
    print("Área:", expediente["area"])
    print("Asunto:", expediente["asunto"])
    print("Fecha:", expediente["fecha"])
    print("------------------------------")


def buscar_por_dni():
    print("\n--- BUSCAR POR DNI ---")

    dni = input("Ingrese el DNI: ").strip()
    encontrado = False

    for expediente in expedientes:
        if expediente["dni"] == dni:
            mostrar_expediente(expediente)
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes con ese DNI.")


def buscar_por_codigo():
    print("\n--- BUSCAR POR CÓDIGO ---")

    codigo = input("Ingrese el código: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            mostrar_expediente(expediente)
            return

    print("No se encontró el expediente.")


def buscar_por_area():
    print("\n--- BUSCAR POR ÁREA ---")

    area = input("Ingrese el área médica: ").strip().lower()
    encontrado = False

    for expediente in expedientes:
        if expediente["area"].lower() == area:
            mostrar_expediente(expediente)
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes en esa área.")


def mostrar_todos():
    print("\n--- LISTA DE EXPEDIENTES ---")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    for expediente in expedientes:
        mostrar_expediente(expediente)

def ordenar_por_codigo():
    print("\n--- ORDENAR POR CÓDIGO ---")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    n = len(expedientes)

    # Ordenamiento burbuja: compara pares vecinos y los intercambia
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]

    guardar_expedientes()

    print("Expedientes ordenados por código:")
    for expediente in expedientes:
        print(expediente["codigo"], "-", expediente["nombre"], "-", expediente["area"])
