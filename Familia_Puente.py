import copy
import time

estInicio= [[1,3,6,8,12,],[]]
estFinal=5
List=[]
lampara=30
Ida= False

#Es hora de rehacer esto, tengo todo en el txt y veamos como no meterle mis encrucijadas mentales

'''
La funcion que ayudara a saber si encontramos el estado objetivo, se define afuera de todo ya que al usar la 
recursividad nos ayudara a tener la nocion de cuando acabarla
'''

def OnePiece(estado_actual, estado_final):
    if len(estado_actual)==estado_final:
        return True
    else:
        return False

Prof = 20 #La maxima cantidad de estados aceptar en nuestra lista que trabaja como pila :p

def busquedaProfundidad(estado_actual, estado_final, ):


if busquedaProfundidad(estInicio, lampara,sentido, tiempo):
    