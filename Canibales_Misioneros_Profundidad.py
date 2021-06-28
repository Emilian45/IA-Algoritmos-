import copy
import time

estInicio= [["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero"],[]]
List=[]

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])==6:
        return True
    else:
        return False

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
    orilla1= estado_inicial[0]
    orilla2= estado_inicial[1]

    if EstadoFEncontrado(estado_inicial):
        return True
  
    else:
        if len(List)-1 < Prof and len(orilla1)>0:
            #Ya que se aplicara de nuevo el modo de vuelta ida tendremos que ver de ambos lados 
            if (BusquedaCanibal(orilla1) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0) and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla2) >=2 or BusquedaCanibal(orilla1) >= 2 and miBusquedaMisionerosioneros(orilla1) - BusquedaCanibal(orilla1) >=0 and BusquedaMisionero(orilla2) == 0: 
                copia_orilla1= copy.copy(orilla1)
                copia_orilla2= copy.copy(orilla2)
                copia_orilla1.remove("Canibal")
                copia_orilla1.remove("Canibal")
                copia_orilla2.append("Canibal")
                copia_orilla2.append("Canibal")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 2 canibales" ] ):
                    return True 

          #1 Canibal y 1 Misionero 
            if BusquedaMisionero(orilla1) > 0 and BusquedaCanibal(orilla1) and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0 and BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0: 
              copia_orilla1= copy.copy(orilla1)
              copia_orilla2= copy.copy(orilla2)
              copia_orilla1.remove("Misionero")
              copia_orilla1.remove("Canibal")
              copia_orilla2.append("Misionero")
              copia_orilla2.append("Canibal")
              if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 1 canibal y 1 misionero" ] ):
                return True
            
            #2 Misioneros 
            if BusquedaMisionero(orilla1) >= 2 and BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 2:
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove("Misionero")
                copia_orilla1.remove("Misionero")
                copia_orilla2.append("Misionero")
                copia_orilla2.append("Misionero")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 2 Misioneros" ] ):
                  return True
            #2 canibales que regresan
            if ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla1) >=0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=2)) or ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=0) and (BusquedaMisionero(orilla1) == 0)): 
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla2.remove("Canibal")
                copia_orilla2.remove("Canibal")
                copia_orilla1.append("Canibal")
                copia_orilla1.append("Canibal")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Regresamos 2 canibales" ] ):
                  return True

            #2 Misioneros  que regresan
            if (BusquedaMisionero(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 2):
              copia_orilla1 = copy.copy(orilla1)
              copia_orilla2 = copy.copy(orilla2)
              copia_orilla2.remove("Misionero")
              copia_orilla2.remove("Misionero")
              copia_orilla1.append("Misionero")
              copia_orilla1.append("Misionero")
              if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Regresamos 2 Misioneros" ] ):
                return True

            #1 Canibal y 1 Misionero  que regresan
            if (BusquedaMisionero(orilla2) > 0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0): 
              copia_orilla1 = copy.copy(orilla1)
              copia_orilla2 = copy.copy(orilla2)
              copia_orilla2.remove("Misionero")
              copia_orilla2.remove("Canibal")
              copia_orilla1.append("Misionero")
              copia_orilla1.append("Canibal")
              if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Regresamos 1 canibal y 1 misionero" ] ):
                return True

    List.pop()
    return False

            


            