class Poligono:

    
    """Define un polígono según su base y su altura."""
    def __init__(self, b, h):
        self.b = b
        self.h = h
class Rectangulo(Poligono):
    def area(self):
        return self.b * self.h
class Triangulo(Poligono):
    def area(self):
        return (self.b * self.h) / 2
ba=float(input( "Ingresa la base del rectangulo" ))  
ha=float(input( "Ingresa la altura del rectangulo" ))  
rectangulo = Rectangulo(ba, ha)
ba=float(input( "Ingresa la base del triangulo" ))  
ha=float(input( "Ingresa la altura del tritangulo" ))  
triangulo = Triangulo(ba, ha)
print("Área del rectángulo:", rectangulo.area())
print("Área del triángulo:", triangulo.area())

""" realizar el menu"""