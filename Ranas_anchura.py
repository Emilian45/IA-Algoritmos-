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

estInicio = [[["Rana","Rana","Rana","Vacio","Sapo","Sapo","Sapo"]]]
estFinal   = ["Sapo","Sapo","Sapo","Vacio","Rana","Rana","Rana"]
List = []
ListAux2 = []  
variableparaWhile=False

'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
  for i in range(len(estado_inicial)):
    if estado_inicial[i] == "Vacio":
      return i
      
'''
Definimos la comparacion que se realizara de los elementos dentro de losa rreglos para ver si se ha llegado al estado final requerido
agregando nuestro toque personal en cuanto a referencias otakus
'''

def OnePiece(estado_inicial,estado_final):
  for i in range(len(estado_inicial)):
    if estado_inicial[i] != estado_final[i]:
      return False
  return True
'''
Quitamos la recursividad y la busqueda de las condiciones y solo ponemos que agrege el estado a una lista auxiliar la cual se trabajara en la busqueda
por anchura
'''

def reglas(estado_inicial):
  
  vacio_actual = busquedaEspacioVacio(estado_inicial) #Nos retorna de nuestra funcion la posicion del vacio ya que en cada estado habra una psoicion diferente asi podremos aplicar las reglas
  listaAux = []#Nos guardara nuestros estados generados en una lista de estados para poder trabajar con ella en nuestra anchura
  
  if vacio_actual+1 <= len(estado_inicial)-1 and estado_inicial[vacio_actual+1] == "Sapo":
    copia_estadoActual = copy.copy(estado_inicial) #Una vez verificada la condicion, hacemos una copia del estado inicial y en la posicion que nos retorna el vacio verificamos
    copia_estadoActual[vacio_actual] = "Sapo"
    copia_estadoActual[vacio_actual+1] = "Vacio"
    listaAux.append(copia_estadoActual)

  if vacio_actual-2 >= 0 and estado_inicial[vacio_actual-2] == "Rana":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[vacio_actual] = "Rana"
    copia_estadoActual[vacio_actual-2] = "Vacio"
    listaAux.append(copia_estadoActual)  

  if vacio_actual+2 <= len(estado_inicial)-1 and estado_inicial[vacio_actual+2] == "Sapo":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[vacio_actual] = "Sapo"
    copia_estadoActual[vacio_actual+2] = "Vacio"
    listaAux.append(copia_estadoActual)

  if vacio_actual-1 >= 0 and estado_inicial[vacio_actual-1] == "Rana":
    copia_estadoActual = copy.copy(estado_inicial)
    copia_estadoActual[vacio_actual] = "Rana"
    copia_estadoActual[vacio_actual-1] = "Vacio"
    listaAux.append(copia_estadoActual)
  
  return listaAux  

def busquedaAnchura(estado_inicial,estado_final):
  '''
  mientras nuestro no se encuentre la solucion no se llamara al return True que viene de las reglas, el cual hara que se rompa el loop infinito
  cipiamos el estadoinicial(actual donde nos encontremos) para poder recorrerlo con nuestro primer for y el apuntador1 ira rewcorriendo ese estadoactual
  dentro  de el el apuntaodr sera tratado como una orilla(la que nos piden las reglas) con los posibles movmientos del estado_actual en donde nos encontremos
   e igual se le pasa el otro parametro snetido que cambiara hasta abajo  y lo guardamos dentro de la variable opciones para poder iterarlo abajo
  Con el apuntador dos iteramos la variable opciones que contiene una lista de lista(que manjeamos como pila)  y al tener la lista preguntamos si es el nuestro
  estado final que buscamos en donde nos encontramos sin revisar aun los posibles movimientos, si es el caso agremaos a la lista(List) y retornamos el True que hara
  que nuestro while salga del  ciclo, si es el caso de que no sea nuestro estado final  agregamos el estadp a la copia del apuntador para generar un estado nuevo y ese
  estado lo agremos a la lista auxuliar 2
  si es el caso que volvemos a entrar en el while limpiamos el estado inicial de ese momento para no guardar nada y despues  la lista auxuliar dos  la volvemos nuestro
  estado inicial para que sin ahber guardado nada siga de ese punto  su recorrdido
  '''
  while not False:
    
    copia_estadoinicial = copy.copy(estado_inicial)      
    for apuntador1 in copia_estadoinicial: 
      opciones = reglas(apuntador1[len(apuntador1)-1]) 
      for apuntador2 in opciones:
        #print(apuntador2)
        copia_apuntador1 = copy.copy(apuntador1)
        if OnePiece(apuntador2,estado_final):
          apuntador1.append(apuntador2)
          for apuntador3 in apuntador1:
            #print(apuntador3)
            List.append(apuntador3)
          return True
        copia_apuntador1.append(apuntador2)
        ListAux2.append(copia_apuntador1)
    #sentido= True if sentido == False else False
    estado_inicial.clear()   
    estado_inicial = copy.copy(ListAux2)
    
'''
def busquedaA(estado_inicial,estado_final):
  cola_prueba=[[[[estado_inicial]]]
  while not OnePiece(estado_inicial,estado_final):
    pila= cola_prueba.pop(0)
    tope= pila[-1]
    variable1 = reglas(tope[0],tope[1])
    for x in variable1:
      pila_copia = copy.copy(pila)
      pila_copia.append(x)
      cola_prueba.append(pila_copia)
    pila=cola_prueba[0]
    tope= pila[-1]
    estado_inicial= tope[0]
    estado_final=tope[1]
  return cola_prueba.pop(0)
'''
'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio  para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
'''
resultado = busquedaProfundidad(estInicio, estFinal)
for i in resultado
  print(i)
'''
profundidad_inicio = time.time()

if busquedaAnchura(estInicio,estFinal):
  print("Llegaste a Laugh Tale")
  print("|")
  print("v")
  for i in List:
    print(i)
else:
  print("Aun esta Barbanegra")  

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")


