import copy
import time

'''
Mapa con un barquero, 1 barco y 1 oveja, 1 caja de coles, 1 lobo y dos orillas
separadas por un lago
Donde  el barquero y el barco seran el cambio  entre la lista de listas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
'''
estInicio = [[  [["Lobo","Obeja","Coles"],[]]  ]]
estFinal   = ["Lobo","Obeja","Coles"]
ListAux2 = []  
List = []
Ida=False
con=False

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 3 objetos que diga  con un true que  se ha completado todos los
objetivos
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
Quitamos la recursividad y la busqueda de las condiciones y solo ponemos que agrege el estado a una lista auxiliar la cual se trabajara en la busqueda
por anchura
En si funciona de la misma manera que es dar las validaciones correspondientes y lo que hara si es el caso tambien es importante tomar en cuenta
el sentido en que se envia la lista porque si se envia una lista con un sentido positivo se dara cuenta de el tipo de movmientos que seran validos
'''


def reglas(estado_inicial,sentido):
  orilla1 = estado_inicial[0]#Como en profundidad trabajremos con dos orilla segun lo hemos estructurado entonces la dividimos en la lista 
  orilla2 = estado_inicial[1]
  ListReglas=[]
  if sentido == False:
    if validacionExisObjeto(orilla1,"Obeja"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla1.remove("Obeja")
      copia_orilla2.append("Obeja")
      ListReglas.append([copia_orilla1,copia_orilla2])
    if validacionExisObjeto(orilla1,"Lobo"):
      if not validacionExisObjeto(orilla1,"Coles") and validacionExisObjeto(orilla1,"Obeja") or validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Lobo")
        copia_orilla2.append("Lobo")
        ListReglas.append([copia_orilla1,copia_orilla2])
    if validacionExisObjeto(orilla1,"Coles"):
      if not validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Obeja") or validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Coles")
        copia_orilla2.append("Coles")
        ListReglas.append([copia_orilla1,copia_orilla2])
    return ListReglas 
  if sentido == True: 
    if not validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Obeja") or not validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Lobo"):
      if not validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Obeja") or not validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") or validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Repollo"):
        ListReglas.append([orilla1,orilla2])
    if validacionExisObjeto(orilla2,"Obeja"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Obeja")
      copia_orilla1.append("Obeja")
      ListReglas.append([copia_orilla1,copia_orilla2])
    if validacionExisObjeto(orilla2,"Lobo"):
      if not validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Lobo")
        copia_orilla1.append("Lobo")
        ListReglas.append([copia_orilla1,copia_orilla2])
    if validacionExisObjeto(orilla2,"Coles"):
      if not validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Obeja") or validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Coles")
        copia_orilla1.append("Coles")
        ListReglas.append([copia_orilla1,copia_orilla2])
    return ListReglas  



'''
def busquedaA(estado_inicial,estado_final,sentido):
  cola_prueba=[[[[estado_inicial],[]]]]
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
 