def bitwise_operations(num1, num2):
    # Operación AND a nivel de bits
    result_and = num1 & num2
    
    # Operación OR a nivel de bits
    result_or = num1 | num2
    
    # Operación XOR a nivel de bits
    result_xor = num1 ^ num2
    
    # Desplazamiento a la izquierda (equivale a multiplicar por 2^n)
    left_shift = num1 << 2
    
    # Desplazamiento a la derecha (equivale a dividir por 2^n)
    right_shift = num2 >> 1
    
    print("Operación AND:", result_and)
    print("Operación OR:", result_or)
    print("Operación XOR:", result_xor)
    print("Desplazamiento a la izquierda:", left_shift)
    print("Desplazamiento a la derecha:", right_shift)

# Ejemplo de uso
num1 = 10  # Representación binaria: 1010
num2 = 6   # Representación binaria: 0110
bitwise_operations(num1, num2)
