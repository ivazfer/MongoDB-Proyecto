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


