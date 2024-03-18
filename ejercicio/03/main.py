from departamento import Departamento
from empleados import Empleado

def main():
    informatica = Departamento("Informatica")
    
    empleado_1 = Empleado("Sofia")
    empleado_2 = Empleado("Catalina")
    empleado_3 = Empleado("Richard")
    empleado_4 = Empleado("Bill")

    informatica.agregar_empleado(empleado_1)
    informatica.agregar_empleado(empleado_2)
    informatica.agregar_empleado(empleado_3)
    informatica.agregar_empleado(empleado_4)



    print(f"Empleados del departamento de {informatica.nombre} :")

    for empleado in informatica.empleados:
        print(f"- {empleado.nombre}")




if __name__ == "__main__":
    main()