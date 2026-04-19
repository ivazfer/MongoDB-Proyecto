https://github.com/everkinetic/data/blob/main/exercises.json

Este documento ya fue editado para un proyecto de lenguaje de marcas.

Estructura del JSON original
Cada ejercicio incluye un id único, un nombre con su identificador interno y su nombre visible, una descripcion con un resumen del ejercicio, una clasificacion con el tipo de ejercicio, los musculos trabajados (principal y secundarios), el material necesario y la ejecucion con los pasos a seguir y consejos opcionales.

Cambios realizados para MongoDB

Se añadieron los campos _id (ObjectId), activo (Boolean), puntuacion (Double), series_recomendadas (Integer), fecha_creacion (Date) e imagen_miniatura (Null). También se incorporaron etiquetas e historial_pesos como arrays, y estadisticas como documento embebido con datos de rendimiento como el peso récord o el progreso acumulado.

Por último, el campo descripcion se amplió con nivel_dificultad y duracion_estimada_minutos para facilitar consultas más específicas.
