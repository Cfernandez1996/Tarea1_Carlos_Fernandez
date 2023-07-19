class Empleado():
    def __init__(self, nombre, identidad, sueldo):
        self._nombre = nombre
        self.identidad = identidad
        self.__sueldo = sueldo

    @property #getter
    def sueldo(self):
        return f"Sueldo Base del empleado: {self.__sueldo} "
    
    @sueldo.setter
    def sueldo(self, valor):
        if valor> self.__sueldo:
            self.__sueldo=valor
        elif valor < self.__sueldo:
             print("No se le puede reducir el sueldo al empleado: ", self._nombre ,'sueldo:' ,self.__sueldo)
             exit()

    @property
    def nombre(self):
        return f"Nombre: {self._nombre}\nIdentidad: {self.identidad}\nSueldo con aumento:{self.__sueldo}"



emp=Empleado('Carlos Fernandez ', '0801-1996-10741 ', 20000)
print(emp.sueldo)

emp.sueldo=2750
print(emp.nombre)



