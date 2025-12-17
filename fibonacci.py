import customtkinter as ctk

# --- Configuración Visual ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class FibonacciApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Fibonacci Moderno")
        self.geometry("500x550")
        self.resizable(False, False)

        # 1. Título y Subtítulo
        self.lbl_titulo = ctk.CTkLabel(self, text="Generador de Fibonacci", font=("Roboto", 24, "bold"))
        self.lbl_titulo.pack(pady=(30, 5))
        
        self.lbl_instruccion = ctk.CTkLabel(self, text="Ingresa un número límite y presiona Enter", text_color="gray")
        self.lbl_instruccion.pack(pady=(0, 20))

        # 2. Área de Entrada (Input)
        self.frame_input = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_input.pack(pady=10)

        self.entrada = ctk.CTkEntry(self.frame_input, placeholder_text="Ej. 100", width=200, justify="center")
        self.entrada.grid(row=0, column=0, padx=10)

        # NUEVO: Vinculamos la tecla Enter (Return) a la función de calcular
        self.entrada.bind('<Return>', self.calcular_fibonacci)

        self.btn_calcular = ctk.CTkButton(self.frame_input, text="Generar", command=self.calcular_fibonacci)
        self.btn_calcular.grid(row=0, column=1, padx=10)

        # 3. Área de Resultados
        self.lbl_res_titulo = ctk.CTkLabel(self, text="Secuencia Generada:", font=("Roboto", 14))
        self.lbl_res_titulo.pack(pady=(20, 5))

        self.txt_resultado = ctk.CTkTextbox(self, width=400, height=150, corner_radius=10)
        self.txt_resultado.pack(pady=5)
        self.txt_resultado.configure(state="disabled")

        # 4. Tarjetas de Información Final
        self.frame_info = ctk.CTkFrame(self, fg_color=("gray90", "gray20"), corner_radius=10)
        self.frame_info.pack(pady=20, padx=50, fill="x")

        self.lbl_final = ctk.CTkLabel(self.frame_info, text="El número final es: --", font=("Roboto", 16))
        self.lbl_final.pack(pady=10)

        self.lbl_falta = ctk.CTkLabel(self.frame_info, text="Faltan -- para llegar al límite", font=("Roboto", 14), text_color="#3B8ED0")
        self.lbl_falta.pack(pady=(0, 10))

    # MODIFICADO: Agregamos 'event=None' para que funcione con el botón (sin evento) y con Enter (con evento)
    def calcular_fibonacci(self, event=None):
        """Lógica del programa conectada a la interfaz"""
        limite_str = self.entrada.get()

        # Validación de error (si está vacío o no es número)
        if not limite_str.isdigit():
            self.lbl_final.configure(text="Error: Ingresa solo números", text_color="red")
            self.lbl_falta.configure(text="")
            return
        
        limite_usuario = int(limite_str)
        if limite_usuario <= 0:
            self.lbl_final.configure(text="Error: El número debe ser > 0", text_color="red")
            return

        # --- Algoritmo de Fibonacci ---
        a, b = 0, 1
        secuencia = []
        ultimo_valido = 0

        while a < limite_usuario:
            secuencia.append(str(a))
            ultimo_valido = a
            a, b = b, a + b

        diferencia = limite_usuario - ultimo_valido

        # --- Actualizar la Interfaz ---
        self.txt_resultado.configure(state="normal")
        self.txt_resultado.delete("0.0", "end")
        self.txt_resultado.insert("0.0", ", ".join(secuencia))
        self.txt_resultado.configure(state="disabled")

        self.lbl_final.configure(text=f"El número final es: {ultimo_valido}", text_color=("black", "white"))
        self.lbl_falta.configure(text=f"Faltan {diferencia} números para llegar a {limite_usuario}")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = FibonacciApp()
    app.mainloop()