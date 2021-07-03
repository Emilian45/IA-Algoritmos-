import copy
import time



'''
Mapa con un barquero, 1 barco y 1 oveja, 1 caja de coles, 1 lobo y dos orillas
separadas por un lago
Donde  el barquero y el barco seran el cambio  entre la lista de listas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
'''
estInicio = [[[["Lobo", "Obeja", "Coles"],[]]]]
estFinal=["Lobo","Obeja","Coles"]
List=[]
ListAux = []
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

  if sentido=True
    
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

#Quite la recursividad de este archivo que tenia y agrege la parte del agrega a la lista
 