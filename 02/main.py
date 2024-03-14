from cuenta_bancaria import CuentaBancaria

def main():
    cliente = CuentaBancaria("Sofia", "1395491-AF2", 1000)
    cliente.mostrar_saldo()
    cliente.depositar(1000)
    cliente.mostrar_saldo()
    cliente.retirar(1500)
    cliente.mostrar_saldo()


if __name__ == "__main__":
    main()