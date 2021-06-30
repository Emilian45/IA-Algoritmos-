import copy
import time



'''
Mapa con un barquero, 1 barco y 1 oveja, 1 caja de coles, 1 lobo y dos orillas
separadas por un lago
Donde  el barquero y el barco seran el cambio  entre la lista de listas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
'''
estInicio = [["Lobo", "Obeja", "Coles"],[]]
estFinal=3
List=[]
Ida= False

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 3 objetos que diga  con un true que  se ha completado todos los
objetivos
'''
def OnePiece(estado_actual, estado_final):
    if len(estado_actual)==estado_final:
        return True
    else:
        return False

'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''

def validacionExisObjeto(Orilla, Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  else:
    return False

def reglas(estado_inicial,sentido):
  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]
  #Validamos estado final o inicial
  if validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Coles"):
    return True
  if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Lobo"):
    return True


  #Validamos si el movimiento fue de ida
  if sentido == True:
    if validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Lobo"):
      return False
    if validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Coles"):
      return False
  #Validamos si el movimiento fue de regreso      
  if sentido == False:
    if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Lobo"):
      return False
    if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Coles"):
      return False
  
  return True
 
   

'''
Comenzamos la funcion de profundidad y agregamos el estado inicial a nuestra lista de soluciones
Establecemos en base a la lista de listas cada elemento lista dentro de la lista sera una orilla a ala cual cruzar
establecemos la profundidad 
'''
Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola


'''
Vemos que elementos hay en las orillas que estamos a punto de mandar para que se cumplan las condicionales del juego y la manera en que se trabajo 
la parte de los estados recursivos es que cada vez que realize un m,ovimiento se haga una copia de ese estado y lo mande como el nuevo estado al inicio 
y comienze la verificacion de nuevo del nuevo estado sin haber guardado la lista de posibles caminos por recorrer, solo se va y espera a que encuentre
mientras no llegue al tope
'''

def busquedaProfundidad(estado_actual, estado_final, sentido, abajo):
  if reglas(estado_actual,sentido):   
    if len(List)-1 < Prof: 
      List.append(estado_actual)
      orilla1 = estado_actual[0]
      orilla2 = estado_actual[1]
      if OnePiece(orilla2, estado_final):
        return True
      else:

        if sentido==False:
          cambiosentido= True
          for x in orilla1:
            copia_orilla1 =copy.copy(orilla1)
            copia_orilla2 =copy.copy(orilla2)
            copia_orilla1.remove(x)
            copia_orilla2.append(x)
            copia_prof= copy.copy(abajo)
            copia_prof= copia_prof-1

            if busquedaProfundidad([copia_orilla1, copia_orilla2],estado_final,cambiosentido,copia_prof ):
              return True

        if sentido== True:
          cambiosentido= False
          copia_prof= copy.copy(abajo)
          copia_prof= copia_prof-1
          if busquedaProfundidad([orilla1, orilla2],estado_final,cambiosentido,copia_prof ):
              return True
                
        if sentido== True:
          cambiosentido= False
          for x in orilla2:
            copia_orilla1 =copy.copy(orilla1)
            copia_orilla2 =copy.copy(orilla2)
            copia_orilla2.remove(x)
            copia_orilla1.append(x)
            copia_prof= copy.copy(abajo)
            copia_prof= copia_prof-1
            if busquedaProfundidad([copia_orilla1, copia_orilla2],estado_final,cambiosentido,copia_prof ):
              return True
        List.pop()
        return False
  return False


'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''

profundidad_inicio = time.time()
if busquedaProfundidad(estInicio,estFinal,Ida, Prof):
  print("Llegaste a Laugh Tale")
  for i in List:
    print(i)
profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
 



