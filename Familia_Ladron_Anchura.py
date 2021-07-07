import copy
import time

estInicio = [[  [["Policia","Cholo","Papa","Hijo","Hijo","Mama","Hija","Hija"],[]]   ]]
estFinal   = ["Policia","Cholo","Papa","Hijo","Hijo","Mama","Hija","Hija"]
numero = 0
Ida=False
List = []
'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene el estado final, que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial,estado_final):
  if len(estado_inicial[1]) == len(estado_final):
    return True
  return False

'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla,Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  return False
'''
Como tenemos que validar los estados que pueden ser validas estbaleceremos dos opciones que seran dar una validacion de  lo que podemos tener de opciones validas y estas
nos ayudaran a que mientras estblezcamos las reglas y posiblesmovmientos validen mientras se hacen, es acortar yn poco lo que teniamos en profundidad en las opciones 
y expandir las reglas de movmientos para que se pueda mover nuestro algortimo, aunque no es como que se mueva sino haga una validacion simultaea en cada estado mientras se hacen los movmientos

'''

def OpcionesVal(estado_inicial):

  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]

  if len(orilla1) > 1 and validacionExisObjeto(orilla1,"Cholo") and not validacionExisObjeto(orilla1,"Policia"):
     return False

  if len(orilla2) > 1 and validacionExisObjeto(orilla2,"Cholo") and not validacionExisObjeto(orilla2,"Policia"):
    return False

  if validacionExisObjeto(orilla1,"Mama") and validacionExisObjeto(orilla1,"Hijo") and not validacionExisObjeto(orilla1,"Papa"):
    return False
  
  if validacionExisObjeto(orilla2,"Mama") and validacionExisObjeto(orilla2,"Hijo") and not validacionExisObjeto(orilla2,"Papa"):
    return False
  
  if validacionExisObjeto(orilla1,"Papa") and validacionExisObjeto(orilla1,"Hija") and not validacionExisObjeto(orilla1,"Mama"):
    return False
  
  if validacionExisObjeto(orilla2,"Papa") and validacionExisObjeto(orilla2,"Hija") and not validacionExisObjeto(orilla2,"Mama"):
    return False

  return True 

'''
hacemos lo mismo que los otros algoritmos  estblecemos las dos orillas con nuestro estado inicial en sus dos listas de listas y comenzamos con lo demas
'''
def reglas(estado_inicial,sentido):
  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]
  lista = []
  if sentido == False:  #Nos     damos orientacion para ver si venimos o vamos de las orillas y facilita la busqueda, intente sin esto en anchura y las validaciones se hacen muy grandes 
    if validacionExisObjeto(orilla1,"Policia"):
      if validacionExisObjeto(orilla1,"Cholo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Cholo")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Cholo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])
            
      if validacionExisObjeto(orilla1,"Hijo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Hijo")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Hijo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Hija"):  
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Hija")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Hija")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla1,"Papa"):
      if validacionExisObjeto(orilla1,"Hijo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Papa")
        copia_orilla1.remove("Hijo")
        copia_orilla2.append("Papa")
        copia_orilla2.append("Hijo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Mama"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Papa")
        copia_orilla1.remove("Mama")
        copia_orilla2.append("Papa")
        copia_orilla2.append("Mama")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla1,"Mama"):
      if validacionExisObjeto(orilla1,"Hija"): 
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Mama")
        copia_orilla1.remove("Hija")
        copia_orilla2.append("Mama")
        copia_orilla2.append("Hija")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Papa"):
        if validacionExisObjeto(orilla1,"Mama"):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla1.remove("Mama")
          copia_orilla1.remove("Papa")
          copia_orilla2.append("Mama")
          copia_orilla2.append("Papa")
          if OpcionesVal([copia_orilla1,copia_orilla2]):
            lista.append([copia_orilla1,copia_orilla2])
    return lista

  if sentido == True:  
    if validacionExisObjeto(orilla2,"Policia"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Policia")
      copia_orilla1.append("Policia")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Policia"):
      if validacionExisObjeto(orilla2,"Cholo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Policia")
        copia_orilla2.remove("Cholo")
        copia_orilla1.append("Policia")
        copia_orilla1.append("Cholo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Papa"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Papa")
      copia_orilla1.append("Papa")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Mama"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Mama")
      copia_orilla1.append("Mama")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    return lista

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
  es genial que el algoritmo jale para todos, primero dios que este bien formulado 
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
  print("Nota: Obvia el estado donde regresa solo y no lo agrega a ls List de estados")
  print("|")
  print("v")
  for i in List:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")