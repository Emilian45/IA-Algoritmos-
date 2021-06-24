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
'''
Definimos una funcion que nos retornasra el valore de i el cual sera el lugar del espacio vacio encontrado (roca vacia)
'''
def busquedaEspacioVacio(estado_inicial)
    for i in range(len(estado_inicial)):
        if estadoinicial[i] == "V":
            return i
            break

def busquedaProfundidad(estado_inicial,estado_final):
    List.append(estado_inicial) #Comenzamos agregando el estado inicial a la lista para tener nuestro primer nodo
    if EstadoFEncontrado(estado_inicial,estado_final):
        return True #Si encuentras la solucion ya salte amigo------------------------------------
    else:
        i=busquedaEspacioVacio(estado_inicial) #Si no haras los siguientes pasos para resolver el problema de la vida----------
        
    '''
    c
    '''
        if i+1 <= len(estado_inicial)-1 and estado_inicial[i+1] == "S":
            

