import copy
import time



'''
Mapa con un barquero, 1 barco y 1 oveja, 1 caja de coles, 1 lobo y dos orillas
separadas por un lago
Donde  el barquero y el barco seran el cambio  entre la lista de listas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
'''
estInicio = [["Lobo", "Coles", "Oveja"],[]]
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
  return False

def reglas(estado_actual, sentido):
  
  orilla1= estado_inicial[0]
  orilla2= estado_inicial[1]
  #Validamos estado final o inicial
  if validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Repollo"):
    return True
  if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Repollo") and validacionExisObjeto(orilla2,"Lobo"):
    return True


  #Validamos si el movimiento fue de ida
  if sentido == True:
    if validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Repollo") and not validacionExisObjeto(orilla1,"Lobo"):
      return False
    if validacionExisObjeto(orilla1,"Obeja") and validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Repollo"):
      return False
  #Validamos si el movimiento fue de regreso      
  if sentido == False:
    if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Repollo") and not validacionExisObjeto(orilla2,"Lobo"):
      return False
    if validacionExisObjeto(orilla2,"Obeja") and validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Repollo"):
      return False
  
  return True

'''
Comenzamos la funcion de profundidad y agregamos el estado inicial a nuestra lista de soluciones
Establecemos en base a la lista de listas cada elemento lista dentro de la lista sera una orilla a ala cual cruzar
establecemos la profundidad 
'''
Prof = 10 #La maxima cantidad de estados aceptar en nuestra cola


'''
Vemos que elementos hay en las orillas que estamos a punto de mandar para que se cumplan las condicionales del juego y la manera en que se trabajo 
la parte de los estados recursivos es que cada vez que realize un m,ovimiento se haga una copia de ese estado y lo mande como el nuevo estado al inicio 
y comienze la verificacion de nuevo del nuevo estado sin haber guardado la lista de posibles caminos por recorrer, solo se va y espera a que encuentre
mientras no llegue al tope
'''

def busquedaProfundidad(estado_inicial):
  List.append(estado_inicial)
  orilla1= estado_inicial[0]
  orilla2= estado_inicial[1]
  
  if EstadoFEncontrado(estado_inicial):
    return True
  else:
    #Verifica si la oveja esta en la orilla
    if  Prof > len(List)-1:
      if len(orilla1) >0:
        if validacionExisObjeto (orilla1, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Oveja")
          copia_orilla2.append("Oveja")
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"Deja la oveja"]):#Aqui se hace la magia de la recursividad 
            return True
    #Vericia si el lobo esta en la orilla
        if validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Lobo") and  validacionExisObjeto(orilla,"Oveja") and not validacionExisObjeto(orilla1,"Coles"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Lobo")
          copia_orilla2.append("Lobo")
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"Deja el lobo"]):#Aqui se hace la magia de la recursividad 
            return True

        if validacionExisObjeto(orilla1,"Coles") and validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Coles") and  validacionExisObjeto(orilla1,"Oveja") and not validacionExisObjeto(orilla1,"Lobo"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Coles")
          copia_orilla2.append("Coles")
          if busquedaProfundidad([copia_orilla1,copia_orilla2, "Deja las coles"]):#Aqui se hace la magia de la recursividad 
            return True

        if validacionExisObjeto(orilla2, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Oveja")
          copia_orilla1.append("Oveja")
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"Regresa a la oveja"]):#Aqui se hace la magia de la recursividad 
            return True

            #Vericia si el lobo esta en la orilla
        if validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Oveja") or validacionExisObjeto(orilla2,"Lobo") and  validacionExisObjeto(orilla2,"Oveja") and not validacionExisObjeto(orilla2,"Coles"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Lobo")
          copia_orilla1.append("Lobo")
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"Regresa al lobo"]):#Aqui se hace la magia de la recursividad 
            return True

        if validacionExisObjeto(orilla2,"Coles") and validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Oveja") or validacionExisObjeto(orilla2,"Coles") and  validacionExisObjeto(orilla2,"Oveja") and not validacionExisObjeto(orilla2,"Lobo"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Coles")
          copia_orilla1.append("Coles")
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"Regresa las coles"]):#Aqui se hace la magia de la recursividad 
            return True

'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
  #Idea: Reestructra lo ya tenido en las reglas para que cada que haga un nodo lo busque implitamente y solo hagamos la busqueda de prof
  #Se va le largo el index
  List.pop()
  return False
profundidad_inicio = time.time()
if busquedaProfundidad(estInicio):
  for i in List:
    print(i)
profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
 