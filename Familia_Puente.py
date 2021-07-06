import copy
import time
'''
Un mapa donde dos orillas se unen por un puente y se encuentran 6 personas
con una lámpara
Donde  el puente  seran el cambio  entre la lista de listas que trabajan con pilas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
la lampara sera un condicional dentro de nuestra busqueda ya que no tiene que exeder los 30 segundos
'''
estInicio= [[1,3,6,8,12,],[]]
estFinal=5
List=[]
lampara=30
Ida= False

#Es hora de rehacer esto, tengo todo en el txt y veamos como no meterle mis encrucijadas mentales

'''
La funcion que ayudara a saber si encontramos el estado objetivo, se define afuera de todo ya que al usar la 
recursividad nos ayudara a tener la nocion de cuando acabarla, agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''

def OnePiece(estado_actual, estado_final):
    if len(estado_actual)==estado_final:
        return True
    else:
        return False

Prof = 20 #La maxima cantidad de estados aceptar en nuestra lista que trabaja como pila :p
'''
La busqueda comenzarea verificando el tamaño de la pila para que cumpla junto con que el tiempo tiene que ser menor al dicho por eso en cada recurtsion mandamos
la copia del tiempo menos el elemeto de mayor tamaño que seria lo que tardo en pasar el puente. Nota 1
Al estar trabajando con una lista de lista que trabaja como pila :v(phyton..), cada lsita dentro de la lista es una orilla
por consecuente tenemos dos asi que  el[0] sera la orilla de partida y la [1] sera la orilla final u objetivo
'''
'''
Lo que no funciono en condiciones extendidad que me ayudaran a la anchura


if len(List)-1 < Prof and len(orilla1)>0 and luz >0:
            #Movimientos con el 1
            #Velocidad del 3
            if  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,3):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(3)
                copia_orilla2.append(1)
                copia_orilla2.append(3)
                copia_luz= copy.copy(luz)-3
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 3"],copia_luz):
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,6):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(6)
                copia_orilla2.append(1)
                copia_orilla2.append(6)
                copia_luz= copy.copy(luz)-6
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 6"],copia_luz):
                    return True

            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,8):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(8)
                copia_orilla2.append(1)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz):
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,12):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(12)
                copia_orilla2.append(1)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz):
                    return True


            #Movimientos  con el 2 mas rapido
            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,6):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(6)
                copia_orilla2.append(3)
                copia_orilla2.append(6)
                copia_luz= copy.copy(luz)-6
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 6"],copia_luz):
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,8):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(8)
                copia_orilla2.append(3)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz):
                    return True

            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,12):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(12)
                copia_orilla2.append(3)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz):
                    return True

            #Movimientos con el tercero mas rapido 

            elif  BuscaExsitenciaSujeto(orilla1,6) and BuscaExsitenciaSujeto(orilla1,8):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(6)
                copia_orilla1.remove(8)
                copia_orilla2.append(6)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz):
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,6) and BuscaExsitenciaSujeto(orilla1,12):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(6)
                copia_orilla1.remove(12)
                copia_orilla2.append(6)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz):
                    return True
            #Movimientos con el cuarto
            elif  BuscaExsitenciaSujeto(orilla1,8) and BuscaExsitenciaSujeto(orilla1,12):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(8)
                copia_orilla1.remove(12)
                copia_orilla2.append(8)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz):
                    return True
        #Regreso

            elif  BuscaExsitenciaSujeto(orilla2,1):
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla2.append(1)
                copia_luz= copy.copy(luz)-1
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 1"],copia_luz):
                    return True

            elif  BuscaExsitenciaSujeto(orilla2,3): 
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla2.append(3)
                copia_luz= copy.copy(luz)-3
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 3"],copia_luz):
                    return True

            elif  BuscaExsitenciaSujeto(orilla2,6): 
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(6)
                copia_orilla2.append(6)
                copia_luz= copy.copy(luz)-6
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 6"],copia_luz):
                    return True

            elif  BuscaExsitenciaSujeto(orilla2,8): 
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(8)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz):
                    return True

'''


def busquedaProfundidad(estado_actual, estado_final, sentido, tiempo ):
    if len(List)-1 < Prof and tiempo >0:#Vemos que nuestra lista no supere el maximo de profundidad en caso de que entre en un bucle
        List.append(estado_actual)  #Comenzamos agregando el estado inicial a la lista para tener nuestro primer nodo
        orilla1 = estado_actual[0]
        orilla2= estado_actual[1]

        if OnePiece(orilla2, estado_final): #Haber si esta referencia es de tu nivel
            return True #Si encuentras Rie como Roger
    else:
        else:

            if sentido == False:
                cambiosentido= True
                ''' Iteramos que el elemento x este dentro de nuestra orilla1 pero se ira acompañado del eleemnto y que contemple abajo,¿Cuales? eso lo vera el programa
                Para poder trabajar los nodos primero hacemos una copia de la orilla1 en donde estan nuestro elementos, a esa copia le quitaremos el elemento x y mientras tenga elementos
                nuestra orilla 1 significa que tenemos elementos que tienen que ir al otro lado aun  entonces al hacer esa verificacion izi, hacemos el movminento de
                quitar los lementos de las copias y agregarlos a la orilla2 asi generenando un nuevo estado que mandaremos a la recursividad con el estado final
                , el cambio de sentido para que nuestras condicionales trabajen correctamente y el tiempo que verificara en la primera condicional de la busqueda
                
                '''
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
                            #Nota 1 Arriba
                            if x-y > 0:
                                copia_tiempo = copia_tiempo - x
                                if busquedaProfundidad([copia2_orilla1,copia_orilla2], estado_final, cambiosentido, copia_tiempo):
                                  return True
                            else:
                                copia_tiempo = copia_tiempo - y
                                if busquedaProfundidad([copia2_orilla1,copia_orilla2], estado_final, cambiosentido, copia_tiempo):
                                  return True
#Si va de regreso hacemos lo mismo que arriba pero ahora se copia en la orilla1  el elemento
            if sentido == True:
                cambiosentido= False
                for x in orilla2:
                    copia_orilla1=copy.copy(orilla1)
                    copia_orilla2=copy.copy(orilla2)
                    copia_orilla2.remove(x)
                    copia_orilla1.append(x)
                    copia_tiempo = copy.copy(tiempo)
                    copia_tiempo= copia_tiempo - x
                    if busquedaProfundidad ([copia_orilla1,copia_orilla2], estado_final, cambiosentido, copia_tiempo):
                        return True
                    
            List.pop()
            return False
    return False


'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()    
if busquedaProfundidad(estInicio, estFinal,Ida, lampara):
  print("Llegaste a Laugh Tale")
  print("|")
  print("v")
  for i in List:
    print(i)
profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
 











    
    