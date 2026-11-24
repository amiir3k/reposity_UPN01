from funciones import (
    cargar_expedientes,
    registrar_expediente,
    eliminar_expediente,
    buscar_por_dni,
    buscar_por_codigo,
    buscar_por_area,
    mostrar_todos
)

cargar_expedientes()

while True:

    print("\n================================")
    print("       MESA DE PARTES")
    print("       CENTRO MEDICO")
    print("================================")
    print("1. Registrar expediente")
    print("2. Eliminar expediente")
    print("3. Buscar por DNI")
    print("4. Buscar por codigo")
    print("5. Buscar por area")
    print("6. Mostrar todos los expedientes")
    print("7. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_expediente()

    elif opcion == "2":
        eliminar_expediente()

    elif opcion == "3":
        buscar_por_dni()

    elif opcion == "4":
        buscar_por_codigo()

    elif opcion == "5":
        buscar_por_area()

    elif opcion == "6":
        mostrar_todos()

    elif opcion == "7":
        print("\nGracias por utilizar el sistema.")
        break

    else:
        print("\nOpcion no valida. Intente nuevamente.")