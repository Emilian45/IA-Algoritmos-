#Si dios quiere acabo osi osi o no duermo pero si saleeee como que no
import copy
import time

estInicio = [[  [["Policia","Ladron","Padre","Hijo","Hijo","Madre","Hija","Hija"],[]]   ]]
estFinal   = ["Policia","Ladron","Padre","Hijo","Hijo","Madre","Hija","Hija"]
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
Tomamos la validaciones echas en profundidad que nos ayudaran a hacer la lista de movmientos para ´poder solo madnar la lista a la anchura
'''

def OpcionesVal(estado_inicial):

  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]

  if len(orilla1) > 1 and validacionExisObjeto(orilla1,"Ladron") and not validacionExisObjeto(orilla1,"Policia"):
     return False

  if len(orilla2) > 1 and validacionExisObjeto(orilla2,"Ladron") and not validacionExisObjeto(orilla2,"Policia"):
    return False

  if validacionExisObjeto(orilla1,"Madre") and validacionExisObjeto(orilla1,"Hijo") and not validacionExisObjeto(orilla1,"Padre"):
    return False
  
  if validacionExisObjeto(orilla2,"Madre") and validacionExisObjeto(orilla2,"Hijo") and not validacionExisObjeto(orilla2,"Padre"):
    return False
  
  if validacionExisObjeto(orilla1,"Padre") and validacionExisObjeto(orilla1,"Hija") and not validacionExisObjeto(orilla1,"Madre"):
    return False
  
  if validacionExisObjeto(orilla2,"Padre") and validacionExisObjeto(orilla2,"Hija") and not validacionExisObjeto(orilla2,"Madre"):
    return False

  return True 