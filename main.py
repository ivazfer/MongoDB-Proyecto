from funciones import *

col = conectar()

salir = False

while salir == False:
    print("\n--- MENÚ EJERCICIOS ---")
    print("1. Insertar un ejercicio")
    print("2. Insertar varios ejercicios")
    print("3. Eliminar un ejercicio")
    print("4. Eliminar varios ejercicios (por nivel)")
    print("5. Actualizar un ejercicio (puntuación)")
    print("6. Actualizar varios ejercicios (desactivar principiantes)")
    print("7. Reemplazar un ejercicio completo")
    print("8. Salir")

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
        actualizar_uno(col)
    elif opcion == "6":
        actualizar_varios(col)
    elif opcion == "7":
        reemplazar_uno(col)
    elif opcion == "8":
        print("Saliendo...")
        salir = True
    else:
        print("Opción no válida, elige entre 1 y 8.")
