import tkinter as tk
from tkinter import font

def generar_tabla():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Tabla de Complemento a 2 (8 bits)")
    ventana.geometry("450x600") # Tamaño inicial de la ventana

    # Crear un marco (Frame) para agrupar el texto y el scrollbar
    frame = tk.Frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Crear el Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Crear el área de Texto
    # Usamos fuente "Courier" (monoespaciada) para que las columnas se alineen perfecto
    fuente_mono = font.Font(family="Courier", size=11)
    area_texto = tk.Text(frame, yscrollcommand=scrollbar.set, font=fuente_mono, wrap=tk.NONE)
    area_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=area_texto.yview)

    # Generar el encabezado de la tabla
    contenido = "Dec | Entrada (Dipswitch) | Salida (LEDs)\n"
    contenido += "-" * 45 + "\n"

    # Generar las 256 combinaciones
    for i in range(256):
        # La regla matemática (el 0 se queda en 0)
        comp2 = 0 if i == 0 else 256 - i
        
        # Formato en binario de 8 bits
        bin_in = f"{i:08b}"
        bin_out = f"{comp2:08b}"
        
        # Separamos en bloques de 4 bits para leerlo más fácil
        formato_in = f"{bin_in[:4]} {bin_in[4:]}"
        formato_out = f"{bin_out[:4]} {bin_out[4:]}"
        
        # Agregamos la fila al contenido
        contenido += f"{i:3} | {formato_in}           | {formato_out}\n"

    # Insertar todo el texto generado en la ventana
    area_texto.insert(tk.END, contenido)
    
    # ¡Muy importante! Cambiamos el estado a DISABLED para que sea SOLO LECTURA
    area_texto.config(state=tk.DISABLED) 

    # Iniciar la interfaz gráfica
    ventana.mainloop()

if __name__ == "__main__":
    generar_tabla()