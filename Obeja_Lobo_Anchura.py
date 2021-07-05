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
List = []
Ida=False

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

def reglas(estado_inicial,sentido):
  orilla1 = estado_inicial[0]
  orilla2 = estado_inicial[1]
  ListReglas=[]
  
  #ORIGEN -> DESTINO
  if sentido == False:
    #accion = 1
    #OBEJA
    if validacionExisObjeto(orilla1,"Obeja"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla1.remove("Obeja")
      copia_orilla2.append("Obeja")
      ListReglas.append([copia_orilla1,copia_orilla2])
    #LOBO 
    if validacionExisObjeto(orilla1,"Lobo"):
      if not validacionExisObjeto(orilla1,"Coles") and validacionExisObjeto(orilla1,"Obeja") or validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Lobo")
        copia_orilla2.append("Lobo")
        ListReglas.append([copia_orilla1,copia_orilla2])
    #REPOLLO
    if validacionExisObjeto(orilla1,"Coles"):
      if not validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Obeja") or validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Coles")
        copia_orilla2.append("Coles")
        ListReglas.append([copia_orilla1,copia_orilla2])
    #print(0," Estado Actual: ",ea," posibles mov: ", lista)
    return ListReglas 
  #DESTINO -> ORIGEN
  if sentido == True: 
    #accion = 0
    #NOSOTROS SOLOS CON LA BARCA
    if not validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Obeja") or not validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Lobo"):
      if not validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Obeja") or not validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") or validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Repollo"):
        ListReglas.append([orilla1,orilla2])
    #NOSOTROS CON LA OBEJA
    if validacionExisObjeto(orilla2,"Obeja"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Obeja")
      copia_orilla1.append("Obeja")
      ListReglas.append([copia_orilla1,copia_orilla2])
    #NOSOTROS CON EL LOBO
    if validacionExisObjeto(orilla2,"Lobo"):
      if not validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Lobo")
        copia_orilla1.append("Lobo")
        ListReglas.append([copia_orilla1,copia_orilla2])
    #NOSOTROS CON EL REPOLLO
    if validacionExisObjeto(orilla2,"Coles"):
      if not validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Obeja") or validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Coles")
        copia_orilla1.append("Coles")
        ListReglas.append([copia_orilla1,copia_orilla2])
    #print(1," Estado Actual: ",ea," posibles mov: ", lista)    
    return ListReglas  

'''
Esto lo dejo comentado porque fue la base del de profundidad 
def reglas(estado_inicial,sentido):
  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]
  #Validamos estado final o inicial

  if sentido==True:
    
    #si quiero  hacer esto acabo de tener en ceunta que tengo un archivo con todo asi
    if validacionExisObjeto (orilla1, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Oveja")
          copia_orilla2.append("Oveja")
          ListAux.append([copia_orilla1,copia_orilla2])
    #Vericia si el lobo esta en la orilla
    if validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Lobo") and  validacionExisObjeto(orilla,"Oveja") and not validacionExisObjeto(orilla1,"Coles"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Lobo")
          copia_orilla2.append("Lobo")
          ListAux.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla1,"Coles") and validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Coles") and  validacionExisObjeto(orilla1,"Oveja") and not validacionExisObjeto(orilla1,"Lobo"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Coles")
          copia_orilla2.append("Coles")
          ListAux.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Oveja")
          copia_orilla1.append("Oveja")
          ListAux.append([copia_orilla1,copia_orilla2])

            #Vericia si el lobo esta en la orilla
    if validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Oveja") or validacionExisObjeto(orilla2,"Lobo") and  validacionExisObjeto(orilla2,"Oveja") and not validacionExisObjeto(orilla2,"Coles"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Lobo")
          copia_orilla1.append("Lobo")
          ListAux.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Oveja") or validacionExisObjeto(orilla2,"Coles") and  validacionExisObjeto(orilla2,"Oveja") and not validacionExisObjeto(orilla2,"Lobo"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Coles")
          copia_orilla1.append("Coles")
          ListAux.append([copia_orilla1,copia_orilla2])
  return ListAux

'''

def busquedaAnchura(estado_inicial,estado_final,sentido):
  ListAux2 = []  #Una Lista de Listas Auxiliar
  bandera = False
  
  while bandera == False:
    aux = copy.copy(estado_inicial) #Copiamos la lista de estados actuales en un auxiliar
    estado_inicial.clear()          #Limpiamos el estado Actual
   
    for x in aux: #Recorremos  toda  la  lista  de  listas  medainte  un  for  y  una   varaible   a   que   apunta   a   la   lista   de   listas   actual
      opciones = reglas(x[len(x)-1],sentido) #Obtenemos una lista de todos los posibles movimientos de la ultima posicion de la lista guarada en a
      for y in opciones:#Recorremos  esa  lista  de  posibles   movminetos  con   un   for
        copia_x = copy.copy(x)#Creamos una copia de la lista a para  cada  posible  movimiento
        if OnePiece(y,estado_final):#validamos si el posible movimiento es el estado final
          x.append(y)#De ser el estado final agregamos este movimiento final a la copia de la lista a
          for z in x:#recorremos  esta  lista  con  la  solucion  con  un   for
            List.append(z)#Agregamos  todos  los   movimientos   en   la   pila
          return True#Cuando termine de agregar los movimientos retornamos True
        copia_x.append(y)#En caso de que no sea el estado final este posible movimiento, agregamos este movimiento en la copia de la lista a
        ListAux2.append(copia_x)#Agregamos esta copia de la lista a en la lista de listas auxiliar
    estado_inicial = copy.copy(ListAux2)#Copiamos todos la lista de listas auxiliar en  el  estado  actual 
    #Con esto le estamos diciendo que cambie di direcicon en su busqueda
    if sentido == 0:
      sentido = 1
    elif sentido == 1:
      sentido = 0
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
 


 