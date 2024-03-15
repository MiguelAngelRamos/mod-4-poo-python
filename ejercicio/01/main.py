from cuenta_bancaria import CuentaBancaria

def menu():
    cuenta = CuentaBancaria()  # Creas una instancia de CuentaBancaria
    while True:
        print("\nCuenta Bancaria")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Saldo actual: {cuenta.consultar_saldo()}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema de cuenta bancaria.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
