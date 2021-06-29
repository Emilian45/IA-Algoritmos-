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

def busquedaProfundidad(estado_actual, estado_final, sentido, tiempo ):
    if len(List)-1 < Prof and tiempo >0:
        List.append(estado_actual)
        orilla1 = estado_actual[0]
        orilla2= estado_actual[1]

        if OnePiece(orilla2, estado_final):
            return True
        else:

            if sentido == False:
                cambiosentido= True
                
                for x in orilla1:
                    copia_orilla1= copy.copy(orilla1)
                    copia_orilla1.remove(x)

                    if len(copia_orilla1) > 0:
                        for y in copia_orilla1:

                            copia2_orilla1= copy.copy(orilla1)
                            copia_orilla2= copy.copy(orilla2)
                            copia2_orilla1.remove(x)
                            copia2_orilla1.remove(y)
                            copia_orilla2.append(x)
                            copia_orilla2.append(y)
                            copia_tiempo = copy.copy(tiempo)
                            if x-y > 0:
                                copia_tiempo = copia_tiempo - x
                                if busquedaProfundidad([copia2_orilla1,copia_orilla2, "Tiempo Restante: ", copia_tiempo], estado_final, cambiosentido, copia_tiempo):
                                  return True
                            else:
                                copia_tiempo = copia_tiempo - y
                                if busquedaProfundidad([copia2_orilla1,copia_orilla2, "Tiempo Restante: ", copia_tiempo], estado_final, cambiosentido, copia_tiempo):
                                  return True

            if sentido == True:
                cambiosentido= False
                for x in orilla2:
                    copia_orilla1=copy.copy(orilla1)
                    copia_orilla2=copy.copy(orilla2)
                    copia_orilla2.remove(x)
                    copia_orilla1.append(x)
                    copia_tiempo = copy.copy(tiempo)
                    copia_tiempo= copia_tiempo - x
                    if busquedaProfundidad ([copia_orilla1,copia_orilla2, "Tiempo Restante: ", copia_tiempo], estado_final, cambiosentido, copia_tiempo):
                        return True
                    
            List.pop()
            return False
    return False
if busquedaProfundidad(estInicio, estFinal,Ida, lampara):
    print("Llegaste a Laugh Tale")
    for i in List:
        print(i)










    
    