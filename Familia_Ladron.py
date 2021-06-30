#Comenzamos con esta wea
import copy
import time

estInicio= [["Padre","Hijo","Hijo","Madre","Hija","Hija","Policia","Cholo"],[]]
estFinal=[[],["Padre","Hijo","Hijo","Madre","Hija","Hija","Policia","Cholo"]]
List=[]
Ida= False


def OnePiece(estado_actual, estado_final):
    if len(estado_actual)==estado_final:
        return True
    else:
        return False

def validacionExisObjeto(Orilla, Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  else:
    return False