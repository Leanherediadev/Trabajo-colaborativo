def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            suma()
        elif opcion == '2':
            resta()
        elif opcion == '3':
            multiplicacion()
        elif opcion == '4':
            division()
        elif opcion == '5':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()