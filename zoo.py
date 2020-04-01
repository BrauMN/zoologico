lista_a=[]
lista_t=[]
lista_m=[]
class animal: 
    def init(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    def set_nombre(self,nombre):
        self.nombre = nombre
          
    def get_nombre(self):
        print(self.nombre)
        self.get_miprueba()

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opción?: "))
            correcto=True
        except ValueError:
            print('Por favor elige una de las opciones')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("\n \n1. Añade un animal")
    print ("2. Ve lista")
    print ("3. Editar lista")
    print ("4. Salir") 
    print ("Elige una opcion")
 
    opcion = Menu()
 
    if opcion == 1:
     a=int (input ("¿Número de animales a agregar? \n"))
     for x in range (a):
            oof=input("Dame el nombre del animal \n")
            lista_a.append(oof)
            pregunta=input("Dame el tipo del animal\n")
            lista_t.append(pregunta)
    elif opcion == 2:
        lista_m = lista_a+lista_t
        for element in lista_m:
         print (element)
    elif opcion == 3:
        ulsa= int(input ("Editar elemento de las listas?\n1.Si\n2.No\n"))
        if ulsa== 1:
         p= input("Al nombre o al tipo del animal?\n ")
         if p==("nombre"):
          for element in lista_a:
           print(lista_a.index(element), element)          
          b=int (input("Dame el id del animal que quieres editar\n"))
          lista_a[b] = input("Agrega el nuevo nombre\n")
          print ("Lista nueva")
          for element in lista_a:
           print (element)
         if p==("tipo"):
          for element in lista_t:
           print(lista_t.index(element), element)          
          b=int (input("Ingresa el id del tipo de animal que quieres editar\n"))
          lista_t[b] = input("Agrega el nuevo nombre\n")
          print ("Lista nueva")
          for element in lista_t:
           print (element)
         
        if ulsa== 2:
         print("")
    elif opcion == 4:
        salir = True
    else:
        print ("Por favor elige una de las opciones")
 
print ("Fin")