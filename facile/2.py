class animal:
    def hablar(self):
        pass

class perro(animal):
    def hablar(self):
        print("groff")

class gato(animal):
    def hablar(self):
        print("miami")

animales=[perro(),gato(),perro()]

for animal in animales:
    animal.hablar()