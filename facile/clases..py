class persona:
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
    def get_edad(self):
        return self.edad
    def get_nombre(self):
        return self.nombre
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

class empleado(persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto= puesto
    

    def presentarse(self):
        print(f"Hola, me llamo {self.get_nombre()} y trabajo como {self.puesto}")


        
    def get_puesto(self):
        return self.puesto

   





persona2= empleado("alberto",21, "trabajador")
persona2.presentarse()