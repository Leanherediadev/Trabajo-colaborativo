# Calculadora: Suma de dos números

def sumar(a, b):
    return a + b

# Solicitar datos al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamar a la función y mostrar resultado
resultado = sumar(num1, num2)
print("La suma es:", resultado)
