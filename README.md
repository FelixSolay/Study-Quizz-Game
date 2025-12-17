# Study-Quizz-Game
Un viejo proyecto en Python que he usado para estudiar en la universidad, revivido, reversionado y mejorado.
La idea principal era armar un juego dinámico de cuestionarios al que se le puedan cargar opciones y respuestas leyendo distintos archivos.
En principio se usaban archivos txt para las respuestas, pero se decidió pasar a JSON por seguridad, confiabilidad y escalabilidad. 
La interfaz del juego está diseñada sobre la biblioteca **Tkinter**

## Características
- **Carga dinámica:** Lee archivos JSON para generar preguntas y opciones automáticamente.
- **Selector de Temas:** Permite cambiar de cuestionario sin reiniciar la aplicación.
- **Feedback Visual:** Indica aciertos y errores mediante cambios de color en la interfaz.

## Cómo ejecutarlo
1. Necesita Python 3.x instalado.
2. Clona el repositorio:
   `git clone https://github.com/FelixSolay/Study-Quizz-Game.git`
3. Ejecuta el juego:
   `python src/main.py`
