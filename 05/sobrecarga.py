# class Calculadora:
#     def sumar(self, numero_1, numero_2, numero_3 = 0, numero_4 = 0):
#         return numero_1 + numero_2 + numero_3 + numero_4

# calculadora = Calculadora()
# print(calculadora.sumar(2,3))
# print(calculadora.sumar(2,3,6))
# print(calculadora.sumar(10, 20, 40, 100))

class Calculadora:
    def sumar(self, *args):
        return sum(args)

calculadora = Calculadora()
print(calculadora.sumar(10, 20))
print(calculadora.sumar(11, 22, 99))
print(calculadora.sumar(20, 10, 108, 77))