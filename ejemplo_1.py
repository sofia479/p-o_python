# clase persona 

class persona:

    # metodo costructor
    def __init__(self, nombre, apellidos,edad):
        self.nombre =nombre
        self.Apellidos0=apellidos
        self.edad=edad

    #metodo para mostrar los datos de una persona 
    def MostrarPersona(self):
        print("nombre:"+ self.Apellidos)
        print("Apellidos:"+ self.Apellidos)
        print("edad"+ str(self.apellidos))
        
   # metodo principal
def main():
    p1 = persona("sofia,galvis",16)
    p1.MostarPersona() 
    p2 =MostrarPersona()
    p2.edad=29
    p1.MostrarPersona()
    p1=p2
    p1.MostrarPersona()
    p2.MostrarPersona()


if __name__== "__main__":
    main()   