import copy
import time

'''
Un mapa donde dos orillas se unen por un puente y se encuentran 6 personas
con una lámpara
Donde  el puente  seran el cambio  entre la lista de listas que trabajan con pilas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
la lampara sera un condicional dentro de nuestra busqueda ya que no tiene que exeder los 30 segundos
'''
estInicio = [[[[1,3,6,8,12],[]]]]
estFinal = [1,3,6,8,12]
linterna=30
List = []
Ida=False

'''
Si la orilla destino, tiene los lementos que bucamos de nuestro estado final  que nuestro buen roger ria!
'''
def OnePiece(estado_inicial, estado_final):
  if len(estado_inicial[1]) == len(estado_final):
    return True
  else:
    return False

'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla, objeto):
  for x in Orilla:
    if x == objeto:
      return True
  return False

 '''
 Como en los demas metodos que se creen las orillas dependiendo del estado inicialpara tener el objetivo y el inicio y de ese punto
 fue creo que es el mas largo porque se tuvo que hacer las psoibildiades decrecientes de los movmientos del integrante mas rapido al mas lento y sus res
 pectivos acompañantes <3 pero ya quedo a mimir!
 ''' 

def reglas(estado_inicial,sentido):
  orilla1 = estado_inicial[0]
  orilla2 = estado_inicial[1]
  ListReglas=[]
  if sentido == True:
        #cambiosentido= False
        if validacionExisObjeto(orilla2,1):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla2.remove(1)
          copia_orilla1.append(1)    
          ListReglas.append( [ copia_orilla1 , copia_orilla2] )

        if validacionExisObjeto(orilla2,3):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla2.remove(3)
          copia_orilla1.append(3)
          ListReglas.append( [ copia_orilla1 , copia_orilla2] )
        
        if validacionExisObjeto(orilla2,6):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla2.remove(6)
          copia_orilla1.append(6) 
          ListReglas.append( [ copia_orilla1 , copia_orilla2] )
        
        if len(orilla2) > 0 and validacionExisObjeto(orilla2,8):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla2.remove(8)
          copia_orilla1.append(8)
          ListReglas.append( [ copia_orilla1 , copia_orilla2] )
      
        if len(orilla2) > 0 and validacionExisObjeto(orilla2,12):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla2.remove(12)
          copia_orilla1.append(12)
          ListReglas.append( [ copia_orilla1 , copia_orilla2] )

        return ListReglas
        
  if sentido == 0:
        if validacionExisObjeto(orilla1,1):
          #Posibles movmimientos con la persona de velocidad 1 y aledaños
          if validacionExisObjeto(orilla1,3):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(1)
            copia_orilla1.remove(3)
            copia_orilla2.append(1)
            copia_orilla2.append(3)   
            ListReglas.append( [ copia_orilla1 , copia_orilla2])

          if validacionExisObjeto(orilla1,6):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(1)
            copia_orilla1.remove(6)
            copia_orilla2.append(1)
            copia_orilla2.append(6)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

          if validacionExisObjeto(orilla1,8):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(1)
            copia_orilla1.remove(8)
            copia_orilla2.append(1)
            copia_orilla2.append(8)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

          if validacionExisObjeto(orilla1,12):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(1)
            copia_orilla1.remove(12)
            copia_orilla2.append(1)
            copia_orilla2.append(12) 
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

        #Posibles movmimientos con la persona de velocidad 3 y aledaños
        if validacionExisObjeto(orilla1,3):
          if validacionExisObjeto(orilla1,6):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(3)
            copia_orilla1.remove(6)
            copia_orilla2.append(3)
            copia_orilla2.append(6)
            ListReglas.append( [ copia_orilla1 , copia_orilla2])

          if validacionExisObjeto(orilla1,8):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(3)
            copia_orilla1.remove(8)
            copia_orilla2.append(3)
            copia_orilla2.append(8)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

          if validacionExisObjeto(orilla1,12):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(3)
            copia_orilla1.remove(12)
            copia_orilla2.append(3)
            copia_orilla2.append(12)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

        #Posibles movmimientos con la persona de velocidad 6 y aledaños
        if validacionExisObjeto(orilla1,6):
          if validacionExisObjeto(orilla1,8):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(6)
            copia_orilla1.remove(8)
            copia_orilla2.append(6)
            copia_orilla2.append(8)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )
         
          if validacionExisObjeto(orilla1,12):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(6)
            copia_orilla1.remove(12)
            copia_orilla2.append(6)
            copia_orilla2.append(12)
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )

        #Posibles movmimientos con la persona de velocidad 8 y aledaños
        if validacionExisObjeto(orilla1,8):
          if validacionExisObjeto(orilla1,12):
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla1.remove(8)
            copia_orilla1.remove(12)
            copia_orilla2.append(8)
            copia_orilla2.append(12) 
            ListReglas.append( [ copia_orilla1 , copia_orilla2] )
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
        copia_apuntador1 = copy.copy(apuntador1)
        if OnePiece(apuntador2,estado_final):
          apuntador1.append(apuntador2)
          for apuntador3 in apuntador1:
            #print(apuntador3)
            List.append(apuntador3)
          return True
        copia_apuntador1.append(apuntador2)
        ListAux2.append(copia_apuntador1)
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
 
