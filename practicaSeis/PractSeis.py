"""
Se piden 3 calificaciones  si como el nombre del alumno
se promedian las calirficaciones  
"""
class calificaciones:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c 

    def promedio(self):
        self.P=(self.a + self.b + self.c)/3
        return self.P

    def comparacion(self):
        if(self.P >= 70 ):
            print("Aprobado")
        elif(self.P < 70):
            print("Reprobado")
    
n=input("Ingresa el nombre del alumno: ")
c1=float(input("Ingrasa la primer calificcacion: "))
c2=float(input("Ingrasa la segunda calificcacion: "))
c3=float(input("Ingrasa la tercer calificcacion: "))
prom = calificaciones(c1,c2,c3)
print("Promedio: ",prom.promedio())
print(prom.comparacion)