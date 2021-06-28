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
List=[]

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])== 3:
        return True
    else:
        return False

def validacionExisObjeto(Orilla, Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  return False

'''
Comenzamos la funcion de profundidad y agregamos el estado inicial a nuestra lista de soluciones
Establecemos en base a la lista de listas cada elemento lista dentro de la lista sera una orilla a ala cual cruzar
establecemos la profundidad 
'''
Prof = 10 #La maxima cantidad de estados aceptar en nuestra cola

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
          if busquedaProfundidad([copia_orilla1,copia_orilla2,"regresa las coles"]):#Aqui se hace la magia de la recursividad 
            return True

  
  #Se va le largo el index
  List.pop()
  return False

if busquedaProfundidad(estInicio):
  for i in List:
    print(i)
 