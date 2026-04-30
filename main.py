from funciones import *

col = conectar()

salir = False

while salir == False:
    print("\n--- MENÚ EJERCICIOS ---")
    print("1. Insertar un ejercicio")
    print("2. Insertar varios ejercicios")
    print("3. Insertar varios ejercicios")
    print("4. Insertar varios ejercicios")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        insertar_uno(col)
    elif opcion == "2":
        insertar_varios(col)
    elif opcion == "3":
        eliminar_uno(col)
    elif opcion == "4":
        eliminar_varios(col)
    elif opcion == "5":
        print("Saliendo...")
        salir = True
    else:
        print("Opción no válida, elige entre 1 y 5.")
