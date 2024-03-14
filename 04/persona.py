class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # Atributo privado
        self.__edad = edad
    
    # Getter para nombre
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter para nombre
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self.__nombre = valor
        else:
            raise ValueError("Nombre debe ser una cadena de texto")
            
    @property
    def edad(self):
        # validacion tienes permiso?
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 120:
            self.__edad = valor
        else:
             raise ValueError("La edad debe ser un numero entero entre 0 y 120")
        
persona = Persona("Sofia", 27)
print(persona.nombre) # get
# set
persona.nombre = 10000
print(persona.nombre)
