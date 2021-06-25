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
List = []

'''
Definimos la comparacion que se realizara de los elementos dentro de losa rreglos para ver si se ha llegado al estado final requerido
'''

def EstadoFEncontrado(estado_inicial,estado_final):
    for i in range(len(estado_inicial)):
        if estado_inicial[i] == estado_final[i]:
          return True
    return False
'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
    for i in range(len(estado_inicial)):
        if estadoinicial[i] == "V":
            return i
            break

'''
dado el indice del espacio vacio cerificara si el sapo esta en la posicion para moverse
y se copiara el estado en el que se encuentra y mandarlo dentro de la lista recursiva que verificara si es el estado final
y si no lo es hara de nuevo la busqueda entr los posibles movimientos, asi en u  ciclo hasta que  encuentre
'''
def busquedaProfundidad(estado_inicial,estado_final):
  List.append(estado_inicial) #Comenzamos agregando el estado inicial a la lista para tener nuestro primer nodo
  if EstadoFEncontrado(estado_inicial,estado_final):
      return True #Si encuentras la solucion ya salte amigo------------------------------------
  else:
      i=busquedaEspacioVacio(estado_inicial) #Si no haras los siguientes pasos para resolver el problema de la vida---------
      if i+1 <= len(estado_inicial)-1 and estado_inicial[i+1] == "S":
        copiaestado = copy.copy(estado_inicial)
        copiaestado[i] = "S"
        copiaestado[i+1] = "V"
        if busquedaProfundidad (copiaestado, estado_final): #Aplicamos la recursividad con la copia del estado inicial para elarguemnto quede en el estado actual
          return True

      if i-2 >= 0 and estadoinicial[i-2] == "R":
        copiaestado = copy.copy(estadoinicial)
        copiaestado[i] = "R"
        copiaestado[i-2] = "V"
        if busquedaProfundidad(copiaestado,estadofinal):
          return True

      if i+2 <= len(estadoinicial)-1 and estadoinicial[i+2] == "S":
        copiaestado = copy.copy(estadoinicial)
        copiaestado[i] = "S"
        copiaestado[i+2] = "V"
        if busquedaProfundidad(copiaestado,estadofinal):
           return True

      if i-1 >= 0 and estadoinicial[i-1] == "R":
          copiaestado = copy.copy(estadoinicial)
          copiaestado[i] = "R"
          copiaestado[i-1] = "V"
          if busquedaProfundidad(copiaestado,estadofinal):
            return True
      List.pop()
      return False

profundidad_inicio = time.time()

if busquedaProfundidad(estInicio,estFinal):
  print("Solución Encontrada")
  for i in lista:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")