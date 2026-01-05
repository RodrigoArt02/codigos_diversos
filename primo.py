import math

def es_primo(numero):
    """
    Determina si un número entero es primo utilizando
    la optimización de la raíz cuadrada.
    """
    # 1. Los números menores a 2 no son primos por definición
    if numero < 2:
        return False
    
    # 2. Buscamos divisores desde 2 hasta la raíz cuadrada del número
    # Usamos int() para redondear y sumamos 1 porque range() en Python excluye el último número
    limite = int(math.sqrt(numero)) + 1
    
    for i in range(2, limite):
        # El operador % (módulo) nos da el residuo de la división.
        # Si el residuo es 0, significa que 'i' es un divisor.
        if numero % i == 0:
            return False # Encontramos un divisor, NO es primo
            
    # 3. Si terminamos el ciclo sin encontrar divisores, ES primo
    return True

# --- Bloque principal para interactuar con el usuario ---
if __name__ == "__main__":
    try:
        entrada = input("Introduce un número entero para verificar si es primo: ")
        num_usuario = int(entrada)
        
        if es_primo(num_usuario):
            print(f"¡El número {num_usuario} ES PRIMO!")
        else:
            print(f"El número {num_usuario} NO ES PRIMO.")
            
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")