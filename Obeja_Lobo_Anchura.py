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
    if validacionExisObjeto(orilla1, "Obeja"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Obeja")
        copia_orilla2.append("Obeja")
        ListAux.append([copia_orilla1,copia_orilla2])

    #si quiero  hacer esto acabo de tener en ceunta que tengo un archivo con todo asi



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
 