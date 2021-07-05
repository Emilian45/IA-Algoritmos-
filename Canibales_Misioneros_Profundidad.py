import copy
import time
'''
Mapa con que tiene 1 barca y 3 caníbales y 3 misioneros y dos orillas en donde las orillas seran nuestro elemento de la lista de listas
y los elementos canibales y misioneros estrana dentro de ella, la barca se considera las condciones necesarias para que los movimientos
de los canibales de efectue
List= Sera en donde guardemos nuestros estados 
dir= Al tener problemas con la priorizcion  de la direccion en que se tienen que mover se implemento un cambio de variable
cada que se mueve de una orilla asi alternando las condicionales if y que tenga un libre funcionamiento dentro de la recursividad

'''

estInicio= [["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero"],[]]
List=[]

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 3 objetos que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial):
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

Prof = 15 #La maxima cantidad de estados aceptar en nuestra cola

def busquedaProfundidad(estado_inicial):
    List.append(estado_inicial)
    orilla1= estado_inicial[0]
    orilla2= estado_inicial[1]

    if OnePiece(estado_inicial):
        return True
  
    else:
        if len(List) < Prof and len(orilla1)>0:
            #Ya que se aplicara de nuevo el modo de vuelta ida tendremos que ver de ambos lados

            #Destino Origen

            #2 canibales que regresan
            if ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=2)) or ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=0) and (BusquedaMisionero(orilla1) == 0)): 
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
             #1 canibal va
            if BusquedaCanibal(orilla2)>0:
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla2.remove("Canibal")
                copia_orilla1.append("Canibal")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Regresamos  1 canibal" ] ):
                  return True
            if (BusquedaMisionero(orilla2)>0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=1)  and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1)>=0):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla2.remove("Misionero")
                copia_orilla1.append("Misionero")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Regresamos 1 Misionero" ] ):
                  return True

            #Origen Destino
            #dos canibales van 
            if ((BusquedaCanibal(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=2)) or ((BusquedaCanibal(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0) and (BusquedaMisionero(orilla2) == 0)): 
                copia_orilla1= copy.copy(orilla1)
                copia_orilla2= copy.copy(orilla2)
                copia_orilla1.remove("Canibal")
                copia_orilla1.remove("Canibal")
                copia_orilla2.append("Canibal")
                copia_orilla2.append("Canibal")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 2 canibales" ] ):
                    return True 

          #1 Canibal y 1 Misionero 
            if (BusquedaMisionero(orilla1) > 0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0): 
              copia_orilla1= copy.copy(orilla1)
              copia_orilla2= copy.copy(orilla2)
              copia_orilla1.remove("Misionero")
              copia_orilla1.remove("Canibal")
              copia_orilla2.append("Misionero")
              copia_orilla2.append("Canibal")
              if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 1 canibal y 1 misionero" ] ):
                return True
            
            #2 Misioneros que van
            if (BusquedaMisionero(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 2):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove("Misionero")
                copia_orilla1.remove("Misionero")
                copia_orilla2.append("Misionero")
                copia_orilla2.append("Misionero")
                if busquedaProfundidad( [ copia_orilla1 , copia_orilla2,"Mandamos 2 Misioneros" ] ):
                  return True
             

            

    List.pop()
    return False

'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio  para llegar al estado final
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
  print("Aun esta Barbanegra")  

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")

