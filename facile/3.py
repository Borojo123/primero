
import math

class figura():
    def calcular_area(self):
        pass

class circulo(figura):
    def __init__(self, circulo):
        self.circulo=circulo
    def calcular_area(self):
        return math.pi*(self.circulo**2)

        
        
class recta(figura):
    def bola(self, ancho, alto):
        self.ancho= ancho
        self.alto=alto
    def calcular_area(self):
        return self.ancho*self.alto
    
rectas=circulo(3)

area= rectas.calcular_area()
print(area)