import tkinter as tk
from tkinter import messagebox

class SumadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sumador Interactivo")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')  # Fondo gris claro
        
        self.suma_total = 0.0
        
        # Marco principal para centrar todo
        self.marco_principal = tk.Frame(root, bg='#f0f0f0')
        self.marco_principal.pack(expand=True, fill='both', padx=20, pady=40)
        
        # Configuración de la interfaz
        self.label_instruccion = tk.Label(
            self.marco_principal, 
            text="Ingresa un número y presiona 'Sumar' o Enter:",  # Texto actualizado
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.label_instruccion.pack(pady=10)
        
        self.entrada_numero = tk.Entry(
            self.marco_principal, 
            font=('Arial', 12), 
            justify='center',
            relief=tk.GROOVE,
            bd=2
        )
        self.entrada_numero.pack(pady=10, ipady=5)
        self.entrada_numero.bind("<Return>", self.sumar_numero)  # Corregido: sin lambda
        
        # Frame para los botones
        self.frame_botones = tk.Frame(self.marco_principal, bg='#f0f0f0')
        self.frame_botones.pack(pady=15)
        
        self.boton_sumar = tk.Button(
            self.frame_botones, 
            text="Sumar", 
            command=self.sumar_numero,  # Nota: aquí no hay parámetro 'event'
            font=('Arial', 10), 
            bg='#4CAF50', 
            fg='white',
            width=10
        )
        self.boton_sumar.pack(side=tk.LEFT, padx=10)
        
        self.boton_terminar = tk.Button(
            self.frame_botones, 
            text="Terminar (R)", 
            command=self.terminar, 
            font=('Arial', 10), 
            bg='#f44336', 
            fg='white',
            width=10
        )
        self.boton_terminar.pack(side=tk.LEFT, padx=10)
        
        self.label_resultado = tk.Label(
            self.marco_principal, 
            text=f"Suma actual: {self.suma_total}", 
            font=('Arial', 14, 'bold'),
            bg='#f0f0f0'
        )
        self.label_resultado.pack(pady=20)
        
        # Vincular la tecla "R" para terminar
        self.root.bind("<KeyPress>", self.detectar_tecla)
        self.entrada_numero.focus()  # Foco inicial en el campo de entrada
        
    def sumar_numero(self, event=None):  # Añadido event=None para manejar ambos casos
        entrada = self.entrada_numero.get()
        if entrada:
            try:
                numero = float(entrada)
                self.suma_total += numero
                self.label_resultado.config(text=f"Suma actual: {self.suma_total}")
                self.entrada_numero.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "¡Ingresa un número válido!")
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío")
    
    def terminar(self):
        messagebox.showinfo("Resultado final", f"La suma total es: {self.suma_total}")
        self.root.quit()
    
    def detectar_tecla(self, event):
        if event.char.lower() == 'r':
            self.terminar()

if __name__ == "__main__":
    root = tk.Tk()
    app = SumadorApp(root)
    root.mainloop()