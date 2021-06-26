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
            #Ya que se aplicara de nuevo el modo de vuelta ida tendremos que ver de ambos lados 
            if BusquedaCanibal(orilla1) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla2) >=2 or BusquedaCanibal(orilla1) >= 2 and miBusquedaMisionerosioneros(orilla1) - BusquedaCanibal(orilla1) >=0 and BusquedaMisionero(orilla2) == 0: 
                copia_orilla1= copy.copy(orilla1)
                copia_orilla2= copy.copy(orilla2)
                copia_orilla1.remove("Canibal")
                copia_orilla1.remove("Canibal")
                copia_orilla2.remove("Canibal")
                copia_orilla2.remove("Canibal")
                if busquedaProfundidad( [ orilla1 , orilla2,"Mandamos 2 canibales" ] ):
                    return True 
                    
        if len(List)-1 < Prof and len(orilla2)>0:
            #Ya que se aplicara de nuevo el modo de vuelta ida tendremos que ver de ambos lados 
            if BusquedaCanibal(orilla1) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla2) >=2 or BusquedaCanibal(orilla1) >= 2 and miBusquedaMisionerosioneros(orilla1) - BusquedaCanibal(orilla1) >=0 and BusquedaMisionero(orilla2) == 0: 
                copia_orilla1= copy.copy(orilla1)
                copia_orilla2= copy.copy(orilla2)
                copia_orilla1.remove("Canibal")
                copia_orilla1.remove("Canibal")
                copia_orilla2.remove("Canibal")
                copia_orilla2.remove("Canibal")
                if busquedaProfundidad( [ orilla1 , orilla2,"Mandamos 2 canibales" ] ):
                    return True 