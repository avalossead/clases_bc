class Persona:
    nombre_persona= None
    edad_persona = None
    def __init__(self,un_nombre,una_edad):
        self.nombre_persona=un_nombre
        self.edad_persona=una_edad
        print("hola soy una persona y me llamo",self.nombre_persona,"y mi edad es",self.edad_persona)
    def get_nombre_persona(self):
        return self.nombre_persona
    def get_edad_persona(self):
        return self.edad_persona
yo = Persona("pepito",25)

