import copy
import time


'''
Mapa con un barquero, 1 barco y 1 oveja, 1 caja de coles, 1 lobo y dos orillas
separadas por un lago
Donde  el barquero y el barco seran el cambio  entre la lista de listas
Cada lista dentro de la listra representa una orilla en donde el objetivo es pasar  todos los objetos de una lista a otra lista dentro de la lista 
siguiendo las reglas que se estreblcerean mas adelantes
'''
estInicio = [["Lobo", "Coles", "Oveja"],[]]
List=[]

def EstadoFEncontrado(estado_inicial)
    if len(estado_inicial[1])>3:
        return False
    elif len(estado_inicial)==3
        return True

def buscaelemento(ar, el):
  for i in ar:
    if i == el:
      return True
  return False

def BEA(ea):

  #print("Estado Actual: ", ea)
  
  lista.append(ea)
  ori = ea[0]
  des = ea[1]

  if solucionEncontrada(ea):
    return True
  else:

    if profundidad > len(lista)-1:

      if len(ori) > 0:

        #Oveja Origen -> destino
        if buscaelemento(ori,"O"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccori.remove("O")
          ccdes.append("O")
          if BEA( [ ccori , ccdes] ):
            return True
        
        #Oveja destino -> origen
        if buscaelemento(des,"O"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccdes.remove("O")
          ccori.append("O")
          if BEA( [ ccori , ccdes] ):
            return True

        #Lobo Origen -> destino
        if buscaelemento(ori,"L") and buscaelemento(ori, "R") and not buscaelemento(ori, "O") or buscaelemento(ori,"L") and buscaelemento(ori, "O") and not buscaelemento(ori, "R"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccori.remove("L")
          ccdes.append("L")
          if BEA( [ ccori , ccdes] ):
            return True
        
        #Lobo destino -> origen
        if buscaelemento(des,"L") and buscaelemento(des, "R") and not buscaelemento(des, "O") or buscaelemento(des,"L") and buscaelemento(des, "O") and not buscaelemento(des, "R"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccdes.remove("L")
          ccori.append("L")
          if BEA( [ ccori , ccdes] ):
            return True

        #Repollo Origen -> destino
        if buscaelemento(ori,"R") and buscaelemento(ori, "L") and not buscaelemento(ori, "O") or buscaelemento(ori,"R") and buscaelemento(ori, "O") and not buscaelemento(ori, "L"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccori.remove("R")
          ccdes.append("R")
          if BEA( [ ccori , ccdes] ):
            return True
        
        #Repollo destino -> origen
        if buscaelemento(des,"R") and buscaelemento(des, "R") and not buscaelemento(des, "O") or buscaelemento(des,"R") and buscaelemento(des, "L") and not buscaelemento(des, "O"):
          ccori = copy.copy(ori)
          ccdes = copy.copy(des)
          ccdes.remove("R")
          ccori.append("R")
          if BEA( [ ccori , ccdes] ):
            return True

    lista.pop()
    return False

if BEA(estadoInicial):
  for i in lista:
    print(i)


