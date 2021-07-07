#Se empieza esto con todooooo y ya con la nocion de profundidad
import copy
import time
'''
Mapa con que tiene 1 barca y 3 caníbales y 3 misioneros y dos orillas en donde las orillas seran nuestro elemento de la lista de listas
y los elementos canibales y misioneros estrana dentro de ella, la barca se considera las condciones necesarias para que los movimientos
de los canibales de efectue
List= Sera en donde guardemos nuestros estados 
dir= Al tener problemas con la priorizcion  de la direccion en que se tienen que mover se implemento un cambio de variable
cada que se mueve de una orilla asi alternando las condicionales if y que tenga un libre funcionamiento dentro de la recursividad

'''
estInicio = [[  [[ "Canibal","Canibal","Canibal","Misionero","Misionero","Misionero" ],[]]   ]]
estFinal   = [ "Canibal","Canibal","Canibal","Misionero","Misionero","Misionero" ]
Ida = False

List = []
'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 6 objetos que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial,estado_final):
  if len(estado_inicial[1]) == len(estado_final):
    return True
  else:
    return False
'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de canibales para poder hacer las comparaciones despues
'''
def BusquedaCanibal(Orilla):
  canibales  = 0
  for i in Orilla:
    if i == "Canibal":
      canibales += 1
  return canibales
'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de Misioneros para poder hacer las comparaciones despues
'''


def BusquedaMisionero(Orilla):
  misioneros = 0
  for i in Orilla:
    if i == "Misionero":
      misioneros += 1
  return misioneros  

'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla,Objeto):
  for x in Orilla:
    if x == Objeto:
      Objeto +=1
  return Objeto
#Aqui ya que tenemos los if solo seria quitar la parte de recursividad porque en si son las reglas  pero aqui si tendremos que agregar  el sentido
#ya que al no estar de manera recursiva no sabe este punto
Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola
def reglas(estado_inicial,sentido):
  ListReglas=[]
  orilla1   = estado_inicial[0]
  orilla2   = estado_inicial[1]

  if sentido == False:
    if BusquedaCanibal(orilla1) >= 2 and BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 2 or BusquedaCanibal(orilla1) >= 2 and BusquedaMisionero(orilla2) == 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla1.remove("Canibal")
      copia_orilla1.remove("Canibal")
      copia_orilla2.append("Canibal")
      copia_orilla2.append("Canibal")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 2 and (BusquedaMisionero(orilla2) + 2) - BusquedaCanibal(orilla2) >= 0 or BusquedaMisionero(orilla1) >= 2 and (BusquedaMisionero(orilla2) + 2) - BusquedaCanibal(orilla2) >= 0 :
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla1.remove("Misionero")
      copia_orilla1.remove("Misionero")
      copia_orilla2.append("Misionero")
      copia_orilla2.append("Misionero")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaCanibal(orilla1) >= 1 and BusquedaMisionero(orilla1) >= 1 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0 and BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla1.remove("Canibal")
      copia_orilla1.remove("Misionero")
      copia_orilla2.append("Canibal")
      copia_orilla2.append("Misionero")
      ListReglas.append([copia_orilla1,copia_orilla2])      
    return ListReglas
  
  if sentido == True:
    if BusquedaCanibal(orilla2) >= 1 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1)>= 1 or BusquedaCanibal(orilla2) >= 1 and BusquedaMisionero(orilla1) == 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Canibal")
      copia_orilla1.append("Canibal")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaMisionero(orilla2) >= 1 and BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2)>= 1 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1)>= 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Misionero")
      copia_orilla1.append("Misionero")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaCanibal(orilla2) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1)>= 2 or BusquedaCanibal(orilla2) >= 2 and BusquedaMisionero(orilla1) == 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Canibal")
      copia_orilla2.remove("Canibal")
      copia_orilla1.append("Canibal")
      copia_orilla1.append("Canibal")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Misionero")
      copia_orilla2.remove("Misionero")
      copia_orilla1.append("Misionero")
      copia_orilla1.append("Misionero")
      ListReglas.append([copia_orilla1,copia_orilla2])

    if BusquedaCanibal(orilla2) >= 1 and BusquedaMisionero(orilla2) >= 1 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0:
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Canibal")
      copia_orilla2.remove("Misionero")
      copia_orilla1.append("Canibal")
      copia_orilla1.append("Misionero")
      ListReglas.append([copia_orilla1,copia_orilla2])  
    return ListReglas
  
def busquedaAnchura(estado_inicial,estado_final,sentido):
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
    ListAux2=[]    
    for apuntador1 in copia_estadoinicial: 
      opciones = reglas(apuntador1[len(apuntador1)-1],sentido) 
      for apuntador2 in opciones:
        #print(apuntador2)
        cca = copy.copy(apuntador1)
        if OnePiece(apuntador2,estado_final):
          apuntador1.append(apuntador2)
          for apuntador3 in apuntador1:
            #print(apuntador3)
            List.append(apuntador3)
          return True
        cca.append(apuntador2)
        ListAux2.append(cca)
    sentido= True if sentido == False else False
    estado_inicial.clear()   
    estado_inicial = copy.copy(ListAux2)


'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()
if busquedaAnchura(estInicio,estFinal,Ida):
  print("Llegaste a Laugh Tale")
  print("|")
  print("v")
  for i in List:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n") 