# ----------------------------------------------------------------
# Script: mychar.py
# Descripción: Aplicación de gestión de cadenas y suite de pruebas.
# Autor: John Omar Peña Cumpa
# Version: 1
# ----------------------------------------------------------------

import unittest
import sys

# --- APARTADO 1: Función principal ---
def cadena_mas_larga(lista_cadenas):
    if not isinstance(lista_cadenas, list):
        raise TypeError("Se esperaba una lista.")
    
    if not lista_cadenas:
        return ""

    for elemento in lista_cadenas:
        # 1. ¿Es un string?
        if not isinstance(elemento, str):
            raise TypeError("Todos los elementos deben ser cadenas de texto.")
        
        # 2. ¿Tiene espacios? (Usamos ' ' in elemento)
        if " " in elemento:
            raise ValueError(f"Error: '{elemento}' contiene espacios. No se permiten.")
        
        # 3. ¿Es puramente alfabético? (Sin números ni símbolos)
        if not elemento.isalpha():
            raise ValueError(f"Error: '{elemento}' contiene números o símbolos. Solo letras.")
    
    # Si pasa los filtros, buscamos la más larga
    longitud_max = max(len(s) for s in lista_cadenas)
    candidatas = [s for s in lista_cadenas if len(s) == longitud_max]
    
    # Orden alfabético en caso de empate
    return sorted(candidatas)[0]

# --- APARTADO 2: Clase de Testing ---
class Test(unittest.TestCase):
    def test_enunciado(self):
        self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")
    
    def test_errores_estrictos(self):
        # Este test pasará (OK) si la función RECHAZA estas entradas
        with self.assertRaises(ValueError):
            cadena_mas_larga(["palabra1", "letras", "12345"]) # Contiene números
        with self.assertRaises(ValueError):
            cadena_mas_larga(["con espacio", "valido"])      # Contiene espacio
        with self.assertRaises(ValueError):
            cadena_mas_larga(["hola!", "mundo", "$$//--%"])             # Contiene símbolo

# --- APARTADO 3: Ejecución ---
if __name__ == "__main__":
    print("--- Programa mychar.py ---")
    palabras = []
    
    while len(palabras) < 5:
        entrada = input(f"Palabra {len(palabras)+1}: ")
        try:
            # Validamos la entrada individualmente usando la función
            cadena_mas_larga([entrada])
            palabras.append(entrada)
        except (ValueError, TypeError) as e:
            print(f"Entrada no válida: {e}")
            print("Por favor, introduce solo letras sin espacios.")

    print(f"\nResultado final: {cadena_mas_larga(palabras)}")