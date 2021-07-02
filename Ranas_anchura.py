import copy
import time


'''
Siendo el estado: 7 piedras en un estanque donde se encuentran 3 sapos y 3 ranas sobre las
piedras, en donde tomaremos las piedras como espacios dentro del arreglo  y los sapos y ranos los elementos que entan dentro de este de definen
los siguientes espacios inciales y finales de la sigueinte manera 
R= Rana
V=Espacio vacio
S= Sapos
List= Sera en donde guardemos nuestros estados 
'''

estInicio = ["R","R","R","V","S","S","S"]  
estFinal  = ["S","S","S","V","R","R","R"]
List = []

def OnePiece(estado_inicial,estado_final):
    for i in range(len(estado_inicial)):
        if estado_inicial[i] != estado_final[i]:
          return False
    return True

'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial):
    for i in range(len(estado_inicial)):
        if estado_inicial[i] == "V":
            return i
            break

def reglas(estado_inicial):
    listaAux= []
    i= busquedaEspacioVacio(estado_inicial)

        #Movimiento Rana Marrón 1
    if i+1 <= len(estado_inicial)-1 and estado_inicial[i+1] == "S":
        aux = copy.copy(estado_inicial)
        aux[i] = "S"
        aux[i+1] = "V"
        lista.append(aux)

    #Movimiento Rana verde 2
    if i-2 >= 0 and estado_inicial[i-2] == "R":
        aux = copy.copy(estado_inicial)
        aux[i] = "R"
        aux[i-2] = "V"
        lista.append(aux)  
    
    #Movimiento Rana Marrón 2
    if i+2 <= len(estado_inicial)-1 and estado_inicial[i+2] == "S":
        aux = copy.copy(estado_inicial)
        aux[i] = "S"
        aux[i+2] = "V"
        lista.append(aux)
    
    #Movimiento Rana verde 1
    if i-1 >= 0 and estado_inicial[i-1] == "R":
        aux = copy.copy(estado_inicial)
        aux[i] = "R"
        aux[i-1] = "V"
        lista.append(aux)
    
    return lista  



