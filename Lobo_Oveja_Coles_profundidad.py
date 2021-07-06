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
estFinal=6
ListaAxiliar=[]
List=[]
Ida=False

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 6 objetos que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial):
    if len(estado_inicial[1])==estFinal:
        return True
    else:
        return False

'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de canibales para poder hacer las comparaciones despues
'''
def BusquedaCanibal(Orilla):
  Canibal  = 0
  for i in Orilla:
    if i == "Canibal":
      Canibal += 1 
  return Canibal

'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de Misioneros para poder hacer las comparaciones despues
'''
def BusquedaMisionero(Orilla):
  Misionero = 0
  for i in Orilla:
    if i == "Misionero":
      Misionero += 1
  return Misionero  


'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla,Objeto):
  for i in Orilla:
    if i == Objeto:
      Objeto +=1
  return Objeto

Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola

def busquedaProfundidad(estado_inicial):
    List.append(estado_inicial)
    orilla1= estado_inicial[0]
    orilla2= estado_inicial[1]
    '''
    Primero guardamos los arreglos orilla1 y orilla2 de nuestro estado actual en  variables,
    Añadimos una variable que va a contener el numero total de elementos que tiene nuestro
    estado actual, despues indicamos que vlide cualquier otro estado que no sea el inicial
    '''

    if OnePiece(estado_inicial):#Haber si esta referencia es de tu nivel
        return True #Si encuentras Rie como Roger
    else:
        if len(List) < Prof and len(orilla1)>0:#Vemos que nuestra lista no supere el maximo de profundidad en caso de que entre en un bucle
          #Ya que se aplicara de nuevo el modo de vuelta ida tendremos que ver de ambos lados
                '''
                Aqui vemos que lo que se hace es dadas las vericaciones en cada if que vamos comparando con el numero de canibales o misioneros
                en las orillas establecemos los momientos que se hara, como podria ser el caso de ida y retorno que debemos especificar lo que se hara con
                cada copia de las orillas lo cual me permitira agregar y quitar elementos de las orillas y mandar ese estado nuevo de vuelta a la recursion
                '''
          #if sentido==False:
                #cambiosentido=True
                if ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=2)) or ((BusquedaCanibal(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=0) and (BusquedaMisionero(orilla1) == 0)): 
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla2.remove("Canibal")
                    copia_orilla2.remove("Canibal")
                    copia_orilla1.append("Canibal")
                    copia_orilla1.append("Canibal")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2]):#MagiaRecursiva retornando un nuevo estado para verificar
                      return True
                if (BusquedaMisionero(orilla2) >= 2) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 2):
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla2.remove("Misionero")
                    copia_orilla2.remove("Misionero")
                    copia_orilla1.append("Misionero")
                    copia_orilla1.append("Misionero")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ):#MagiaRecursiva retornando un nuevo estado para verificar
                        return True
                if (BusquedaMisionero(orilla2) > 0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0): 
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla2.remove("Misionero")
                    copia_orilla2.remove("Canibal")
                    copia_orilla1.append("Misionero")
                    copia_orilla1.append("Canibal")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ):#MagiaRecursiva retornando un nuevo estado para verificar
                        return True
                if BusquedaCanibal(orilla2)>0:
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla2.remove("Canibal")
                    copia_orilla1.append("Canibal")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2]):#MagiaRecursiva retornando un nuevo estado para verificar
                      return True
                if (BusquedaMisionero(orilla2)>0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=1)  and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1)>=0):
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla2.remove("Misionero")
                    copia_orilla1.append("Misionero")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ):#MagiaRecursiva retornando un nuevo estado para verificar
                      return True
          #if sentido==True:
                #cambiosentido=False        

                if ((BusquedaCanibal(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >=2)) or ((BusquedaCanibal(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >=0) and (BusquedaMisionero(orilla2) == 0)): 
                    copia_orilla1= copy.copy(orilla1)
                    copia_orilla2= copy.copy(orilla2)
                    copia_orilla1.remove("Canibal")
                    copia_orilla1.remove("Canibal")
                    copia_orilla2.append("Canibal")
                    copia_orilla2.append("Canibal")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ):#MagiaRecursiva retornando un nuevo estado para verificar
                        return True 

                if (BusquedaMisionero(orilla1) > 0) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 0) and (BusquedaMisionero(orilla2) - BusquedaCanibal(orilla2) >= 0): 
                    copia_orilla1= copy.copy(orilla1)
                    copia_orilla2= copy.copy(orilla2)
                    copia_orilla1.remove("Misionero")
                    copia_orilla1.remove("Canibal")
                    copia_orilla2.append("Misionero")
                    copia_orilla2.append("Canibal")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ):#MagiaRecursiva retornando un nuevo estado para verificar
                        return True

                if (BusquedaMisionero(orilla1) >= 2) and (BusquedaMisionero(orilla1) - BusquedaCanibal(orilla1) >= 2):
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla1.remove("Misionero")
                    copia_orilla1.remove("Misionero")
                    copia_orilla2.append("Misionero")
                    copia_orilla2.append("Misionero")
                    if busquedaProfundidad( [ copia_orilla1 , copia_orilla2] ): #MagiaRecursiva retornando un nuevo estado para verificar
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


