import Suma
import Resta
import Multiplicación
import División
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
            Suma.suma()
        elif opcion == '2':
            Resta.resta()
        elif opcion == '3':
            Multiplicación.multiplicacion()
        elif opcion == '4':
            División.division()
        elif opcion == '5':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()