# Calculadora de división en Python
def division():
    # Pedimos al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Verificamos que el divisor no sea cero
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
