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

estInicio = ["R","R","R","V","S","S","S"]  
estFinal  = ["S","S","S","V","R","R","R"]
lista = []

'''
Definimos la comparacion que se realizara de los elementos dentro de losa rreglos para ver si se ha llegado al estado final requerido
Mientras no encuentres ninguna similitud dentro de los elementos  returna un false 
'''

def OnePiece(estado_inicial,estado_final):
    for i in range(len(estado_inicial)):
        if estado_inicial[i] != estado_final[i]:
          return False
    return True
'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
    for i in range(len(estado_inicial)):
        if estado_inicial[i] == "V":
            return i
            break

'''
dado el indice del espacio vacio cerificara si el sapo esta en la posicion para moverse
y se copiara el estado en el que se encuentra y mandarlo dentro de la lista recursiva que verificara si es el estado final
y si no lo es hara de nuevo la busqueda entr los posibles movimientos, asi en u  ciclo hasta que  encuentre
'''
Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola
#Aislaremos las reglas para que la profundidad haga lo suyo
def busquedaProfundidad(estado_inicial,estado_final):
  lista.append(estado_inicial) #Comenzamos agregando el estado inicial a la lista para tener nuestro primer nodo
  if OnePiece(estado_inicial,estado_final) and len(lista)-1 < Prof:
      return True #Si encuentras la solucion ya salte amigo
  else: #Si no haras los siguientes pasos para resolver el problema de la vida
      i=busquedaEspacioVacio(estado_inicial) 
      if i+1 <= len(estado_inicial)-1 and estado_inicial[i+1] == "S":
        copiaestado = copy.copy(estado_inicial)
        copiaestado[i] = "S"
        copiaestado[i+1] = "V"
        if busquedaProfundidad (copiaestado, estado_final): #Aplicamos la recursividad con la copia del estado inicial para elarguemnto quede en el estado actual
          return True

      if i-2 >= 0 and estado_inicial[i-2] == "R":
        copiaestado = copy.copy(estado_inicial)
        copiaestado[i] = "R"
        copiaestado[i-2] = "V"
        if busquedaProfundidad(copiaestado,estado_final):
          return True

      if i+2 <= len(estado_inicial)-1 and estado_inicial[i+2] == "S":
        copiaestado = copy.copy(estado_inicial)
        copiaestado[i] = "S"
        copiaestado[i+2] = "V"
        if busquedaProfundidad(copiaestado,estado_final):
           return True

      if i-1 >= 0 and estado_inicial[i-1] == "R":
          copiaestado = copy.copy(estado_inicial)
          copiaestado[i] = "R"
          copiaestado[i-1] = "V"
          if busquedaProfundidad(copiaestado,estado_final):
            return True
      lista.pop()
      return False
'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''

profundidad_inicio = time.time()

if busquedaProfundidad(estInicio,estFinal):
  print("Llegaste a Laugh Tale")
  for i in lista:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")