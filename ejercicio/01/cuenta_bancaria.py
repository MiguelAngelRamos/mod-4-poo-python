class CuentaBancaria:
    
    def __init__(self, saldo_incial=0):
        self.__saldo = saldo_incial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            # self._saldo = self.__saldo + cantidad
            self.__saldo += cantidad
            print(f"Deposito exitoso, Saldo Actual: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positivo")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            # self._saldo = self.saldo - cantidad
            self.__saldo -= cantidad
            print(f"Retiroso exitos. Saldo actual: {self.__saldo}")
        else:
            print("La operacion no se puede realizar, Verifique la cantidad y el saldo disponible")

    def consultar_saldo(self):
        return self.__saldo
    
  
    # @property
    # def saldo(self):
    #     return self.__saldo
    
    # @saldo.setter
    # def saldo(self, valor):
    #     if isinstance(valor, float) and valor >=0:
    #         self.__saldo += valor
    #     else:
    #          raise ValueError("No se admiten valores negativos para el saldo")
    


# cuenta = CuentaBancaria(10000)
# cuenta.depositar(50)
# cuenta.retirar(4000)
# print(f"Saldo final: {cuenta.consultar_saldo()}")


