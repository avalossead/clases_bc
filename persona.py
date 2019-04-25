class Persona:
    nombre_persona= None
    edad_persona = None

    def __init__(self,un_nombre,una_edad):
        self.nombre_persona=un_nombre
        self.edad_persona=una_edad
        print("hola soy una persona y me llamo",self.nombre_persona,"y mi edad es",self.edad_persona)
    
    def get_edad_persona(self):
        print (self.edad_persona)

    def sumar_anhos(self):
         self.edad_persona= edad_persona+1

yo = Persona("pepito",25)

####


