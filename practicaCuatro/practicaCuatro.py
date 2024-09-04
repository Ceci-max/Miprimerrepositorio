class Rectangulo:
    """
    Define un rectángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h
ba=float(input( "Ingresa la base" ))  
ha=float(input( "Ingresa la altura" ))   
rectangulo = Rectangulo(ba, ha)
print("El area del rectángulo con base:",ba, "Y altura:",ha, "es de:" , rectangulo.area()), 