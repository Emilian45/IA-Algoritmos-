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
ListAux=[]

def OnePiece(estado_inicial):
    if len(estado_inicial[1])== 3:
        return True
    else:
        return False

def validacionExisObjeto(Orilla, Objeto):
  for x in Orilla:
    if x == Objeto:
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
  '''
  Primero guardamos los arreglos orilla1 y orilla2 de nuestro estado actual en  variables,
  Añadimos una variable que va a contener el numero total de elementos que tiene nuestro
  estado actual, despues indicamos que vlide cualquier otro estado que no sea el inicial
  '''

  
  if OnePiece(estado_inicial):#Haber si esta referencia es de tu nivel
    return True #Si encuentras Rie como Roger
  else:
    
    '''
    La condicional dira si no hemos excedido la profundidad maxima y si la orilla1 (nuestro origen) aun tiene elementos que sigan en ese lugar
    para seguir trabajando con ellos
    
    Aqui vemos que lo que se hace es dadas las vericaciones en cada if que vamos comparando las posibles opciones que tenemos 
    en las orillas,  a, como podria ser el caso de ida y retorno que debemos especificar lo que se hara con
    cada copia de las orillas lo cual me permitira agregar y quitar elementos de las orillas y mandar ese nuevo estado a la recursividad
               
    '''
    if  Prof > len(List)-1:
      if len(orilla1) >0:
        if validacionExisObjeto (orilla1, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla1.remove("Oveja")
          copia_orilla2.append("Oveja")
          if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
            return True
    #Vericia si el lobo esta en la orilla
        if validacionExisObjeto(orilla1,"Lobo"):
          if validacionExisObjeto(orilla1,"Lobo") and validacionExisObjeto(orilla1,"Coles") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Lobo") and  validacionExisObjeto(orilla,"Oveja") and not validacionExisObjeto(orilla1,"Coles"):
            copia_orilla1= copy.copy(orilla1)
            copia_orilla2= copy.copy(orilla2)
            copia_orilla1.remove("Lobo")
            copia_orilla2.append("Lobo")
            if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
              return True

        if validacionExisObjeto(orilla1,"Coles"):
          if validacionExisObjeto(orilla1,"Coles") and validacionExisObjeto(orilla1,"Lobo") and not validacionExisObjeto(orilla1,"Oveja") or validacionExisObjeto(orilla1,"Coles") and  validacionExisObjeto(orilla1,"Oveja") and not validacionExisObjeto(orilla1,"Lobo"):
            copia_orilla1= copy.copy(orilla1)
            copia_orilla2= copy.copy(orilla2)
            copia_orilla1.remove("Coles")
            copia_orilla2.append("Coles")
            if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
              return True

        if validacionExisObjeto(orilla2, "Oveja"):
          copia_orilla1= copy.copy(orilla1)
          copia_orilla2= copy.copy(orilla2)
          copia_orilla2.remove("Oveja")
          copia_orilla1.append("Oveja")
          if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
            return True

            #Vericia si el lobo esta en la orilla
        if validacionExisObjeto(orilla2,"Lobo"):    
          if validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Coles") and not validacionExisObjeto(orilla2,"Oveja") or validacionExisObjeto(orilla2,"Lobo") and  validacionExisObjeto(orilla2,"Oveja") and not validacionExisObjeto(orilla2,"Coles"):
            copia_orilla1= copy.copy(orilla1)
            copia_orilla2= copy.copy(orilla2)
            copia_orilla2.remove("Lobo")
            copia_orilla1.append("Lobo")
            if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
              return True
        if validacionExisObjeto(orilla2,"Coles"):
          if not validacionExisObjeto(orilla2,"Lobo") and validacionExisObjeto(orilla2,"Obeja") or validacionExisObjeto(orilla2,"Lobo") and not validacionExisObjeto(orilla2,"Obeja"):
            copia_orilla1= copy.copy(orilla1)
            copia_orilla2= copy.copy(orilla2)
            copia_orilla2.remove("Coles")
            copia_orilla1.append("Coles")
            if busquedaProfundidad([copia_orilla1,copia_orilla2]):#Aqui se hace la magia de la recursividad 
              return True
  List.pop()#En caso de que no lo encuentre que lo saque de la lista 
  return False


'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()    
if busquedaProfundidad(estInicio):
  print("Llegaste a Laugh Tale")
  print("|")
  print("v")
  for i in List:
    print(i)
else:
  print("Aun no derrotas al goobierno mundial")
profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
 

 