# Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo.
# class Rectangulo: 
#     def __init__(self,Base,Altura):
#         self.base=Base
#         self.altura=Altura 

#     def area(self):

#         return self.base*self.altura
# rectangulo1=Rectangulo(8,9)
# rectangulo1.area()

# b=float(input("Por favor ingrese la base del rectangulo: "))
# h=float(input("Por davor ingrese la altura del rectangulo: "))
# rectangulo=Rectangulo(b,h)
# print(f"El area del rectangulo es {rectangulo.area()}")
# Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
#  La clase debe contener
# como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
# class Mate:
#     def __init__(self,N):
#         self.cebadasrest=N
#         self.estado=False
#         self.n=N

#     def cebar(self): 
#         if self.estado==True:
#             print("Cuidado, te quemaste!")
#         elif self.cebadasrest>0:
#             self.cebadasrest-=1
#             self.estado=True

#     def beber(self):
#         if self.estado==False:
#             print("El mate esta vacio")
#         else: 
#             if self.cebadasrest==0:
#                 self.estado=False
#                 print("El mate está lavado")
#             else:
#                 self.estado=False

# mate1=Mate(2)
# mate1.cebar()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.beber()

"""
Ejercicio3: Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho.
"""

# class Corcho:
#     def __init__(self,bodega:str):
#         self.Bodega= bodega

# class Botella: 
#     def __init__(self,corcho:Corcho=None):
#         self.CorchoDeBotella=corcho

# class Sacacorcho:
#     def __init__(self):
#             self.Corcho_sacado=None
#     def destapar(self,botella:Botella):
#             if botella.CorchoDeBotella==None:
#                 print("La botella no tiene corcho.")
#             else:
#                 if self.Corcho_sacado!=None:
#                     print(f"El sacacorcho tiene un corcho: {self.Corcho_sacado}")
#                 else:
#                     self.Corcho_sacado=botella.CorchoDeBotella
#                     botella.CorchoDeBotella=None
#     def limpiar(self):
#         if self.Corcho_sacado==None:
#             print("No hay un corcho en el sacacorchos.")
#         else:
#             self.Corcho_sacado=None
#             print("El sacacorchos fue limpiado con éxito.")



# corcho1=Corcho("Salta")
# print(corcho1.Bodega)
# botella1=Botella(corcho1)
# sacacorcho1=Sacacorcho()
# sacacorcho1.destapar(botella1)
# print(botella1.CorchoDeBotella)
# sacacorcho1.limpiar()

"""
Ejercicio4:
Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. 
"""
class Restaurante:
    def __init__(self,nombre,tipo_comida):
        self.NombreRestaurante=nombre
        self.TipoComida=tipo_comida
    
    def describir_restaurante(self):
        print(f"Bienvenidos al restaurante: {self.NombreRestaurante}, donde pueden encontrar las comidas: {self.TipoComida}")
    
    def abrir_restaurante(self):
        print(f"El restaurante {self.NombreRestaurante} abrió sus puertas.")

class Heladeria(Restaurante):
    def __init__(self, sabores,nombre,tipocomida):
        super().__init__(nombre,tipocomida)
        self.SaboresHelado=sabores
    
    def mostrarsabores(self):
        for n in self.SaboresHelado:
            print(n,end=" - ")


# sabores=["chocolate","vainilla","dulce de leche","limon","crema cookie"]
# heladeria1=Heladeria(sabores,"Grido","helados")
# heladeria1.describir_restaurante()
# heladeria1.abrir_restaurante()
# heladeria1.mostrarsabores()

"""
Ejercicio5:
Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada

"""


# class Personaje:
#     def __init__(self,vida,posicion,velocidad):
#         self.Vida_Personaje=vida
#         self.Posicion_Personaje=posicion
#         self.Velocidad_Personaje=velocidad

#     def recibir_ataque(self,ataque):
#         self.Vida_Personaje-=ataque
#         if self.Vida_Personaje<=0:
#             print("Te mamaste we, moriste.")
#         else:
#             print(f"Recibiste un ataque, salud actual: {self.Vida_Personaje}")
    
#     def mover(self,direccion):
#         if direccion==True:
#             self.Posicion_Personaje+=self.Velocidad_Personaje
#         else:
#             self.Posicion_Personaje-=self.Velocidad_Personaje

# class Soldado(Personaje):
#     def __init__(self,vida,posicion,velocidad,ataque):
#         super().__init__(vida,posicion,velocidad)
#         self.Ataque_Soldado=ataque
    
#     def atacar(self,persona:Personaje):
#         persona.recibir_ataque(self.Ataque_Soldado)
    
# class Campesino(Personaje):
#     def __init__(self,vida,posicion,velocidad,cosecha):
#         super().__init__(vida,posicion,velocidad)
#         self.Cosecha_Campesino=cosecha

#     def cosechar(self):
#         print(f"Cosechaste {self.Cosecha_Campesino} de trigo.")

# soldado1=Soldado(10,0,2,4)
# persona1=Personaje(8,0,3)
# campesino1=Campesino(8,0,3,5)

# soldado1.atacar(persona1)
# soldado1.atacar(persona1)

# print(f"La salud persona: {campesino1.Vida_Personaje}")
# soldado1.atacar(campesino1)
# print(f"La salud persona: {campesino1.Vida_Personaje}")
# campesino1.cosechar()

"""
Ejercicio 6:
Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

"""

class Usuario:
    def __init__(self,nombre,apellido,edad):
        self.Nombre_Usuario=nombre
        self.Apellido_Usuario=apellido
        self.Edad_Usuario=edad

    def describir_usuario(self):
        print(f"Nombre: {self.Nombre_Usuario}\nApellido: {self.Apellido_Usuario}\nEdad: {self.Edad_Usuario}")
    
    def saludar_usuario(self):
        print(f"Buen día {self.Nombre_Usuario}")

# persona1=Usuario("Emilio","Cesped",40)
# persona2=Usuario("Camila","Cesped",34)
# persona3=Usuario("Facundo","Altube",24)
# persona4=Usuario("Inej","Brekker",24)
# persona1.describir_usuario()
# persona1.saludar_usuario()
# persona2.describir_usuario()
# persona2.saludar_usuario()
# persona3.describir_usuario()
# persona3.saludar_usuario()
# persona4.describir_usuario()
# persona4.saludar_usuario()


"""
Ejercicio7:
Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

"""
class Privilegios:
    def __init__(self,privilegios):
        self.Privilegios=privilegios
        
    def mostrar_privilegios(self):
        for n in self.Privilegios:
            print(n)

class Admin(Usuario):
    def __init__(self,nombre,apellido,edad,privilegios):
        super().__init__(nombre,apellido,edad)
        self.Privilegios_Admin=privilegios
    
    def mostrar_privilegios(self,privilegio:Privilegios):
        privilegio.mostrar_privilegios()
        

# privilegios=["Puede postear en el foro","Puede borrar un post","Puede banear un usuario"]
# admin1=Admin("Raul","Perez",38,privilegios)

# admin1.describir_usuario()
# admin1.saludar_usuario()
# admin1.mostrar_privilegios()

""""
Ejercicio8: 
Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios.

"""
# class Privilegios:
#     def __init__(self,privilegios):
#         self.Privilegios=privilegios
        
#     def mostrar_privilegios(self):
#         for n in self.Privilegios:
#             print(n)



# privilegio1=Privilegios(["Permiso de ban","Permiso de publicar","Permiso de borrar"])
# admin2=Admin("Raul","Perez",54,privilegio1)
# admin2.mostrar_privilegios(privilegio1)










































