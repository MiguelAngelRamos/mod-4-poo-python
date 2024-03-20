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


# class Calculadora:
#     def sumar(self, *args):
#         tu_valor_3 = args[3]
#         print(tu_valor_3)
#         # for args in args:
#         #     print(args)


# calculadora = Calculadora()
# calculadora.sumar(1,2,3,4)