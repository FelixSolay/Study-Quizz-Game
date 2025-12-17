# Study-Quizz-Game
Un viejo proyecto en Python que he usado para estudiar en la universidad, revivido, reversionado y mejorado.

La idea principal era armar un juego dinámico de cuestionarios al que se le puedan cargar opciones y respuestas leyendo distintos archivos.

En principio se usaban archivos txt para las respuestas, pero se decidió pasar a JSON por seguridad, confiabilidad y escalabilidad. 

La interfaz del juego está diseñada sobre la biblioteca **Tkinter**.

## Características
- **Carga dinámica:** Generación automática de UI basada en archivos JSON.
- **Selector de Temas:** Permite cambiar de cuestionario sin reiniciar la aplicación.
- **Feedback Visual:** Indica aciertos y errores mediante cambios de color en la interfaz.
- **Dificultad ajustable:** Selector en tiempo real para definir cuántas opciones mostrar por pregunta.

## Cómo crear tus propios cuestionarios
El juego lee automáticamente cualquier archivo .json dentro de la carpeta /data. Para añadir tu propio tema, tenés que crearlo con la siguiente estructura y agregarlo a la carpeta:
```json
{
  "titulo": "Nombre del Tema",
  "opciones": {
    "OPCION A": 1,
    "OPCION B": 2,
    "OPCION C": 3
  },
  "preguntas": [
    {
      "texto": "Acá va la descripción o pregunta",
      "id": 1
    }
  ]
}
```
## Pro Tip: Generar preguntas masivamente con IA
No hace falta que escribas los JSON a mano. Puedes usar modelos de lenguaje (como Gemini o ChatGPT) para convertir tus apuntes, PDFs o resúmenes en archivos listos para jugar.

Copia y pega este Prompt en tu IA favorita:

    "Actúa como un experto en pedagogía y programación. Lee el siguiente texto [PEGA TU TEXTO ACÁ] y genera un archivo JSON para un juego de preguntas. La estructura debe ser la siguiente un diccionario llamado 'opciones' donde las claves sean los conceptos principales y los valores sean IDs numéricos únicos. Luego, una lista llamada 'preguntas' donde cada elemento tenga el 'texto' (definición o pregunta) y el 'id' correspondiente a la respuesta correcta. 
    Ejemplo:
      {
      "titulo": "Nombre del Tema",
      "opciones": {
         "OPCION A": 1,
         "OPCION B": 2,
         "OPCION C": 3
      },
      "preguntas": [
         {
            "texto": "Acá va la descripción o pregunta",
            "id": 1
         }
      ]
      }    
    Asegúrate de que el formato sea estrictamente JSON válido teniendo en cuenta el ejemplo provisto."

## Instalación y Uso
1. Necesita Python 3.x instalado.
2. Clona el repositorio:
   `git clone https://github.com/FelixSolay/Study-Quizz-Game.git`
3. Coloca tus archivos generados en la carpeta data/. (Eliminá los archivos de ejemplo si molestan)
4. Ejecuta el juego:
   `python src/main.py`
