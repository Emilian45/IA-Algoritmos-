import copy
import time

estInicio= [["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero",],[]]]
List=[]

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])>6:
        return False
    elif len(estado_inicial)==6:
        return True

def BusquedaCanibal(Orilla):
  Canibal  = 0
  for i in Orilla:
    if i == "Canibal":
      Canibal += 1 
  return Canibal

def BusquedaMisionero(Orilla):
  Misionero = 0
  for i in Orilla:
    if i == "Misionero":
      Misionero += 1
  return Misionero  

Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola

def busquedaProfundidad(estado_inicial):
    List.append(estado_inicial)
    orilla1= List[0]
    orilla2= List[1]

    if EstadoFEncontrado(estado_inicial):
        return True
  
    else:
        if len(List)-1 < Prof and len(orilla2)>0: