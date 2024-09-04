class Triangulo:
    """
    Define un triangulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        r=(self.b * self.h)/2
        return(r) 
ba=float(input( "Ingresa la base" ))  
ha=float(input( "Ingresa la altura" ))   
triangulo = Triangulo(ba, ha)
print("El area del triangulo con base:",ba, "Y altura:",ha, "es de:" , triangulo.area()), 