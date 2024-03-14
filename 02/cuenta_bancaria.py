class CuentaBancaria:
    def __init__(self, titular_de_cuenta, numero_cuenta, saldo=0.0):
        self.titular = titular_de_cuenta
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def mostrar_saldo(self):
        print(f"Saldo actual del cliente {self.titular} es de: {self.saldo}")
    
    def depositar(self, monto):
        if monto > 0:
            # self.saldo = self.saldo + monto
            self.saldo += monto
            print(f"Deposito de: {monto}, realizado con exito!")
        else:
            print("El monto a depositar debe ser positivo")
    # 100000 saldo
    # retirar 12000
    def retirar(self, monto):
        if monto > 0:
            if self.saldo >= monto:
                # self.saldo = self.saldo - monto
                self.saldo -= monto
                print(f"Retiro realizado: {monto}")
            else:
                print(f"El Saldo: {self.saldo}, es insuficiente para el retiro")
        else:
            print("El monto a retirar debe ser positivo")
