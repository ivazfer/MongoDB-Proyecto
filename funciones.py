from pymongo import MongoClient

def conectar():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["gimnasio"]
    coleccion = db["ejercicios"]
    return coleccion


def insertar_uno(col):
    nuevo = {
        "id": 999,
        "activo": True,
        "puntuacion": 4.0,
        "series_recomendadas": 3,
        "imagen_miniatura": None,
        "etiquetas": ["espalda", "fuerza", "barra"],
        "historial_pesos": [40.0, 50.0, 60.0],
        "nombre": {
            "identificador": "remo-con-barra",
            "visible": "Remo con barra"
        },
        "descripcion": {
            "resumen": "Ejercicio para fortalecer la espalda.",
            "nivel_dificultad": "intermedio",
            "duracion_estimada_minutos": 20
        },
        "clasificacion": {"tipo": {"nombre": "compuesto"}},
        "musculos": {
            "principal": {"nombre": "espalda"},
            "secundarios": [{"nombre": "biceps"}, {"nombre": "hombros"}]
        },
        "material": {
            "equipo": [{"elemento": {"nombre": "barra", "tipo": "peso libre"}}]
        },
        "estadisticas": {
            "veces_realizado": 10,
            "ultimo_peso_kg": 60.0,
            "record_personal_kg": 70.0,
            "porcentaje_progreso": 16.6
        }
    }
    resultado = col.insert_one(nuevo)
    print("Ejercicio insertado con id:", resultado.inserted_id)

def insertar_varios(col):
    nuevos = [
        {
            "id": 1001,
            "activo": True,
            "puntuacion": 3.8,
            "series_recomendadas": 3,
            "imagen_miniatura": None,
            "etiquetas": ["piernas", "compuesto", "barra"],
            "historial_pesos": [60.0, 80.0, 100.0],
            "nombre": {
                "identificador": "sentadilla",
                "visible": "Sentadilla"
            },
            "descripcion": {
                "resumen": "Ejercicio rey para el tren inferior.",
                "nivel_dificultad": "intermedio",
                "duracion_estimada_minutos": 25
            },
            "clasificacion": {"tipo": {"nombre": "compuesto"}},
            "musculos": {
                "principal": {"nombre": "cuadriceps"},
                "secundarios": [{"nombre": "gluteos"}, {"nombre": "isquiotibiales"}]
            },
            "material": {
                "equipo": [{"elemento": {"nombre": "barra", "tipo": "peso libre"}}]
            },
            "estadisticas": {
                "veces_realizado": 80,
                "ultimo_peso_kg": 100.0,
                "record_personal_kg": 120.0,
                "porcentaje_progreso": 20.0
            }
        },
        {
            "id": 1002,
            "activo": False,
            "puntuacion": 2.5,
            "series_recomendadas": 2,
            "imagen_miniatura": None,
            "etiquetas": ["cardio", "peso corporal"],
            "historial_pesos": [],
            "nombre": {
                "identificador": "saltar-cuerda",
                "visible": "Saltar a la cuerda"
            },
            "descripcion": {
                "resumen": "Ejercicio cardiovascular sencillo.",
                "nivel_dificultad": "principiante",
                "duracion_estimada_minutos": 10
            },
            "clasificacion": {"tipo": {"nombre": "cardio"}},
            "musculos": {
                "principal": {"nombre": "piernas"},
                "secundarios": []
            },
            "material": {
                "equipo": [{"elemento": {"nombre": "cuerda", "tipo": "cardio"}}]
            },
            "estadisticas": {
                "veces_realizado": 5,
                "ultimo_peso_kg": 0,
                "record_personal_kg": 0,
                "porcentaje_progreso": 0.0
            }
        }
    ]
    resultado = col.insert_many(nuevos)
    print("Ejercicios insertados, ids:", resultado.inserted_ids)

def eliminar_uno(col):
    nombre = input("Nombre del ejercicio a eliminar (identificador): ")
    resultado = col.delete_one({"nombre.identificador": nombre})
    if resultado.deleted_count > 0:
        print("Ejercicio eliminado correctamente.")
    else:
        print("No se encontró ningún ejercicio con ese identificador.")

def eliminar_varios(col):
    nivel = input("Eliminar todos los ejercicios con nivel de dificultad: ")
    resultado = col.delete_many({"descripcion.nivel_dificultad": nivel})
    print("Ejercicios eliminados:", resultado.deleted_count)
    
    
def actualizar_uno(col):
    nombre = input("Identificador del ejercicio a actualizar: ")
    nueva_puntuacion = float(input("Nueva puntuación: "))
    resultado = col.update_one(
        {"nombre.identificador": nombre},
        {"$set": {"puntuacion": nueva_puntuacion}}
    )
    if resultado.matched_count > 0:
        print("Ejercicio actualizado correctamente.")
    else:
        print("No se encontró el ejercicio.")
    

def actualizar_varios(col):
    resultado = col.update_many(
        {"descripcion.nivel_dificultad": "principiante"},
        {"$set": {"activo": False}}
    )
    print("Ejercicios actualizados:", resultado.modified_count)

def reemplazar_uno(col):
    nombre = input("Identificador del ejercicio a reemplazar: ")
    nuevo_documento = {
        "id": 9999,
        "activo": True,
        "puntuacion": 5.0,
        "series_recomendadas": 5,
        "imagen_miniatura": None,
        "etiquetas": ["test", "reemplazo"],
        "historial_pesos": [10.0, 20.0],
        "nombre": {
            "identificador": nombre,
            "visible": "Ejercicio reemplazado"
        },
        "descripcion": {
            "resumen": "Este ejercicio fue reemplazado desde el programa.",
            "nivel_dificultad": "avanzado",
            "duracion_estimada_minutos": 30
        },
        "clasificacion": {"tipo": {"nombre": "compuesto"}},
        "musculos": {
            "principal": {"nombre": "cuerpo completo"},
            "secundarios": []
        },
        "material": {
            "equipo": [{"elemento": {"nombre": "ninguno", "tipo": "peso corporal"}}]
        },
        "estadisticas": {
            "veces_realizado": 1,
            "ultimo_peso_kg": 20.0,
            "record_personal_kg": 20.0,
            "porcentaje_progreso": 0.0
        }
    }
    resultado = col.replace_one({"nombre.identificador": nombre}, nuevo_documento)
    if resultado.matched_count > 0:
        print("Ejercicio reemplazado correctamente.")
    else:
        print("No se encontró el ejercicio.")



