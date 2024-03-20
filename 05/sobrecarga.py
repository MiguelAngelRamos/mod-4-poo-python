# class Calculadora:
#     def sumar(self, numero_1, numero_2, numero_3 = 0):
#         return numero_1 + numero_2 + numero_3

# calculadora = Calculadora()
# print(calculadora.sumar(2,3))
# print(calculadora.sumar(2,3,6))

class Calculadora:
    def sumar(self, *args):
        return sum(args)

calculadora = Calculadora()
print(calculadora.sumar(10, 20))
print(calculadora.sumar(11, 22, 99))
print(calculadora.sumar(20, 10, 108, 77))