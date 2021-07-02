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

estInicio = [[["R","R","R","V","S","S","S"]]]
estFinal   = ["S","S","S","V","R","R","R"]
List = []
variableparaWhile=False

'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
  for i in range(len(estado_inicial)):
    if estado_inicial[i] == "V":
      return i
      

def OnePiece(estado_inicial,estado_final):
  for i in range(len(estado_inicial)):
    if estado_inicial[i] != estado_final[i]:
      return False
  return True

def reglas(estado_inicial):
  
  i = busquedaEspacioVacio(estado_inicial)
  listaAux = []
  
  #Movimiento Rana Marrón 1
  if i+1 <= len(estado_inicial)-1 and estado_inicial[i+1] == "S":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[i] = "S"
    copia_estadoActual[i+1] = "V"
    listaAux.append(copia_estadoActual)

  #Movimiento Rana verde 2
  if i-2 >= 0 and estado_inicial[i-2] == "R":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[i] = "R"
    copia_estadoActual[i-2] = "V"
    listaAux.append(copia_estadoActual)  
  
  #Movimiento Rana Marrón 2
  if i+2 <= len(estado_inicial)-1 and estado_inicial[i+2] == "S":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[i] = "S"
    copia_estadoActual[i+2] = "V"
    listaAux.append(copia_estadoActual)
  
  #Movimiento Rana verde 1
  if i-1 >= 0 and estado_inicial[i-1] == "R":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[i] = "R"
    copia_estadoActual[i-1] = "V"
    listaAux.append(copia_estadoActual)
  
  return listaAux  

def busquedaProfundidad(estado_inicial,estado_final):
  while variableparaWhile == False:
    copia_estadoActual = copy.copy(estado_inicial) #Copiamos la lista de estados actuales en un auxiliar
    estado_inicial.clear()          #Limpiamos el estado Actual
    ListaDeListas = []  #Una Lista de Listas Auxiliar

    for a in copia_estadoActual: #Recorremos  toda  la  lista  de  listas  medainte  un  for  y  una  varaible  a  que  apunta  a  la  lista   de   listas   actual
      opciones = reglas(a[len(a)-1]) #Obtenemos una lista de todos los posibles movimientos de la ultima posicion de la lista guarada en a
      for i in opciones:#Recorremos  esa  lista  de  posibles   movminetos  con   un   for
        cca = copy.copy(a)#Creamos una copia de la lista a para  cada  posible  movimiento
        if OnePiece(i,estado_final):#validamos si el posible movimiento es el estado final
          a.append(i)#De ser el estado final agregamos este movimiento final a la copia de la lista a
          for c in a:#recorremos  esta  lista  con  la  solucion  con  un   for
            List.append(c)#Agregamos  todos  los   movimientos   en   la   pila
          return True#Cuando termine de agregar los movimientos retornamos True
        cca.append(i)#En caso de que no sea el estado final este posible movimiento, agregamos este movimiento en la copia de la lista a
        ListaDeListas.append(cca)#Agregamos esta copia de la lista a en la lista de listas auxiliar
    estado_inicial = copy.copy(ListaDeListas)#Copiamos todos la lista de listas auxiliar en  el  estado  actual 

'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio  para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()

if busquedaProfundidad(estInicio,estFinal):
  print("Llegaste a Laugh Tale")
  for i in List:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")

  