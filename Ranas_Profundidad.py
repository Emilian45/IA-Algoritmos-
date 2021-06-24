import copy


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

'''
Definimos la comparacion que se realizara de los elementos dentro de losa rreglos para ver si se ha llegado al estado final requerido
'''

def EstadoFEncontrado(estado_inicial,estado_final)
    for i in (len(estado_inicial)):
        if estadoinicial[i] == estado_final[i]:
            return true
    return False

def busquedaEspacioVacio(estado_inicial)
    for i in range(len(estado_inicial)):
        if estadoinicial[i] == "V":
            return i
            break
