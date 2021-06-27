import copy
import time

estInicio= [[1,3,6,8,12,],[]]
List=[]
lampara=30

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])==5:
        return True
    else:
        return False

def BuscaExsitenciaSujeto(orlla,sujeto):
    for i in orilla:
        if sujeto ==i:
            return True
    
    return  False

Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola

def busquedaProfundidad(estado_inicial, luz):
    List.append(estado_inicial)
    orilla1= List[0]
    orilla2= List[1]

    if EstadoFEncontrado(estado_inicial):
        return True

    else:

        if len(List)-1 < Prof and len(orilla1)>0 and luz >0:

        



