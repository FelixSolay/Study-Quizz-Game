import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de preguntas fds")
        self.master.geometry("700x550")
        self.master.configure(bg="#f0f0f0")

        self.puntos = 0
        self.datos = None
        self.pregunta_actual = None
        self.preguntas_mostradas = []
        self.num_opciones = tk.IntVar(value=4)

        self.setup_ui()
        self.cargar_selector_temas()

    def setup_ui(self):
        # Estilos
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 11))
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"), background="#f0f0f0")

        self.frame_top = ttk.Frame(self.master)
        self.frame_top.pack(pady=10, fill="x", padx=20)
        # Cantidad de opciones (Header)
        ttk.Label(self.frame_top, text="Opciones por pregunta:").pack(side="left", padx=5)
        self.entry_opciones = ttk.Entry(self.frame_top, textvariable=self.num_opciones, width=5)
        self.entry_opciones.pack(side="left", padx=5)

        # Selector de archivos (Header)
        ttk.Label(self.frame_top, text="Tema:").pack(side="left", padx=5)
        self.combo_temas = ttk.Combobox(self.frame_top, state="readonly", width=30)
        self.combo_temas.pack(side="left", padx=10)
        self.combo_temas.bind("<<ComboboxSelected>>", self.cambiar_tema)

        # Área de pregunta
        self.lbl_pregunta = ttk.Label(self.master, text="Selecciona un tema para comenzar", 
                                      wraplength=500, justify="center", style="Header.TLabel")
        self.lbl_pregunta.pack(pady=40)

        # Contenedor de botones
        self.frame_respuestas = ttk.Frame(self.master)
        self.frame_respuestas.pack(pady=10)

        # Puntos
        self.lbl_puntos = tk.Label(self.master, text="Puntos: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.lbl_puntos.pack(side="bottom", pady=20)

    def cargar_selector_temas(self):
        # Definimos la ruta de la carpeta data
        ruta_data = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        if os.path.exists(ruta_data):
            archivos = [f for f in os.listdir(ruta_data) if f.endswith('.json')]
            self.combo_temas['values'] = archivos
        else:
            # Si no existe la carpeta, busca en la actual por si acaso
            archivos = [f for f in os.listdir('.') if f.endswith('.json')]
            self.combo_temas['values'] = archivos

    def cambiar_tema(self, event):
        archivo = os.path.join("data", self.combo_temas.get())
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                self.datos = json.load(f)
            self.puntos = 0
            self.preguntas_mostradas = []
            self.actualizar_puntos()
            self.siguiente_pregunta()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

    def generar_botones(self):
        # Limpiar botones anteriores
        for widget in self.frame_respuestas.winfo_children():
            widget.destroy()

        # Obtener número de opciones ya validado
        num_opciones = int(self.num_opciones.get())
        
        # Obtener todas las opciones
        todas_opciones = list(self.datos["opciones"].items())
        
        # Encontrar la opción correcta
        opcion_correcta = None
        for texto, valor in todas_opciones:
            if valor == self.pregunta_actual["id"]:
                opcion_correcta = (texto, valor)
                break
        
        # Seleccionar opciones aleatorias y asegurar que la correcta esté incluida
        opciones_a_mostrar = [opcion_correcta]
        opciones_restantes = [opt for opt in todas_opciones if opt != opcion_correcta]
        
        if len(opciones_restantes) >= num_opciones - 1:
            opciones_a_mostrar.extend(random.sample(opciones_restantes, num_opciones - 1))
        else:
            opciones_a_mostrar.extend(opciones_restantes)
        
        # Mezclar las opciones
        random.shuffle(opciones_a_mostrar)
        
        # Crear botones
        for texto, valor in opciones_a_mostrar:
            btn = ttk.Button(self.frame_respuestas, text=texto, 
                            command=lambda t=texto: self.verificar(t))
            btn.pack(pady=5, fill="x")

    def verificar(self, respuesta_usuario):
        id_usuario = self.datos["opciones"][respuesta_usuario]
        id_correcto = self.pregunta_actual["id"]

        if id_usuario == id_correcto:
            self.feedback_visual("#c8e6c9") # Verde claro
            self.puntos += 1
            self.siguiente_pregunta()
        else:
            self.feedback_visual("#ffcdd2") # Rojo claro
            self.puntos -= 1
        
        self.actualizar_puntos()

    def feedback_visual(self, color):
        original_bg = self.master.cget("bg")
        self.master.configure(bg=color)
        # Cambia el color de los labels también para que no se vea el recuadro gris
        self.lbl_pregunta.configure(background=color)
        self.master.after(300, lambda: self.restaurar_color(original_bg))

    def restaurar_color(self, color_original):
        self.master.configure(bg=color_original)
        self.lbl_pregunta.configure(background=color_original)

    def siguiente_pregunta(self):
        if self.datos and self.datos["preguntas"]:
            # Validar número de opciones
            try:
                num_opciones = int(self.num_opciones.get())
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido para las opciones")
                return

            total_opciones_json = len(self.datos["opciones"])
            
            if num_opciones > total_opciones_json:
                messagebox.showwarning("Advertencia", f"Solo hay {total_opciones_json} opciones disponibles en el archivo JSON")
                self.num_opciones.set(total_opciones_json)

            if num_opciones < 1:
                messagebox.showerror("Error", "Debe haber al menos 1 opción")
                return

            preguntas_disponibles = [p for p in self.datos["preguntas"] if p not in self.preguntas_mostradas]
            
            if not preguntas_disponibles:
                messagebox.showinfo("Fin del juego", f"¡Completaste todas las preguntas! Total de puntos: {self.puntos}")
                self.preguntas_mostradas = []
                preguntas_disponibles = self.datos["preguntas"]
            
            self.pregunta_actual = random.choice(preguntas_disponibles)
            self.preguntas_mostradas.append(self.pregunta_actual)
            self.lbl_pregunta.config(text=self.pregunta_actual["texto"])
            self.generar_botones()

    def actualizar_puntos(self):
        self.lbl_puntos.config(text=f"Puntos: {self.puntos}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()