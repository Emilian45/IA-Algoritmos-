import copy
import time

'''
Siendo el estado: 7 piedras en un estanque donde se encuentran 3 sapos y 3 ranas sobre las
piedras, en donde tomaremos las piedras como espacios dentro del arreglo  y los sapos y ranos los elementos que entan dentro de este de definen
los siguientes espacios inciales y finales de la sigueinte manera 
R= Rana
V=Espacio vacio
S= Sapos
List= Sera en donde guardemos nuestros estados 
'''
estInicio = ["Rana","Rana","Rana","Vacio","Sapo","Sapo","Sapo"]  
estFinal  = ["Sapo","Sapo","Sapo","Vacio","Rana","Rana","Rana"]
Prof=20
List = []

'''
Definimos la comparacion que se realizara de los elementos dentro de losa rreglos para ver si se ha llegado al estado final requerido
agregando nuestro toque personal en cuanto a referencias otakus
'''

def OnePiece(estado_inicial,estado_final):
    for x in range(len(estado_inicial)):
        if estado_inicial[x] != estado_final[x]:
          return False
    return True
'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
    for x in range(len(estado_inicial)):
        if estado_inicial[x] == "Vacio":
            return x
            

'''
dado el indice del espacio vacio cerificara si el sapo esta en la posicion para moverse
y se copiara el estado en el que se encuentra y mandarlo dentro de la lista recursiva que verificara si es el estado final
y si no lo es hara de nuevo la busqueda entr los posibles movimientos, asi en u  ciclo hasta que  encuentre
Cabe mencionar que nuestra variable estado inicial y las copias respectivas seran mas estados donde nos encontremos actualmente que estados iniciales
'''
def busquedaProfundidad(estado_inicial,estado_final):
  if len(List)<Prof: #Vemos que nuestra lista no supere el maximo de profundidad en caso de que entre en un bucle
    List.append(estado_inicial) #Comenzamos agregando el estado inicial a la lista para tener nuestro primer nodo
    if OnePiece(estado_inicial,estado_final):
        return True #Si encuentras Rie como Roger
    else:
        x=busquedaEspacioVacio(estado_inicial) #Si no aplicaras las reglas y encuentra la isla final
        if x+1 <= len(estado_inicial)-1 and estado_inicial[x+1] == "Sapo":
          copia_estado = copy.copy(estado_inicial) #Una vez verificada la condicion, hacemos una copia del estado inicial y en la posicion que nos retorna el vacio verificamos
          copia_estado[x] = "Sapo"
          copia_estado[x+1] = "Vacio"
          if busquedaProfundidad (copia_estado, estado_final): #Aplicamos la recursividad con la copia del estado inicial para elarguemnto quede en el estado actual
            return True

        if x-2 >= 0 and estado_inicial[x-2] == "Rana":
          copia_estado = copy.copy(estado_inicial)
          copia_estado[x] = "Rana"
          copia_estado[x-2] = "Vacio"
          if busquedaProfundidad(copia_estado,estado_final): #La magia de la recursividad
            return True

        if x+2 <= len(estado_inicial)-1 and estado_inicial[x+2] == "Sapo":
          copia_estado = copy.copy(estado_inicial)
          copia_estado[x] = "Sapo"
          copia_estado[x+2] = "Vacio"
          if busquedaProfundidad(copia_estado,estado_final): #La magia de la recursividad
            return True

        if x-1 >= 0 and estado_inicial[x-1] == "Rana":
            copia_estado = copy.copy(estado_inicial)
            copia_estado[x] = "Rana"
            copia_estado[x-1] = "Vacio"
            if busquedaProfundidad(copia_estado,estado_final): #La magia de la recursividad
              return True
        List.pop() #Si no es el caso mejor sacalo de la lista que trabaja como pila 
        return False
'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentran los estados que siguio  para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()

if busquedaProfundidad(estInicio,estFinal):
  print("Llegaste a Laugh Tale")
  print("|")
  print("v")
  for i in List:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")

 