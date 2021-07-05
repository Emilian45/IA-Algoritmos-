#Se empieza esto con todooooo y ya con la nocion de profundidad

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

estInicio= [[[["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero"],[]]]]
estFinal= ["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero"]
ListaAxiliar=[]
List=[]
Ida=False

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 6 objetos que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial,estado_final):
    if len(estado_inicial[1])==estado_final:
        return True
    else:
        return False

'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de canibales para poder hacer las comparaciones despues
'''
def BusquedaCanibal(Orilla):
  Canibal  = 0
  for x in Orilla:
    if x == "Canibal":
      Canibal += 1 
  return Canibal

'''Pues como se tornaron unos problemas con el metodo que se venia manejando y ahora se esta resolviendo de manera en que
  que para verificar estemos contando el numero de misiones  y canibales en cada orilla pues sera mejor contar la cantidad de cada elemento dentro de cada orilla
  Aqui retornaremos el numero de Misioneros para poder hacer las comparaciones despues
'''
def BusquedaMisionero(Orilla):
  Misionero = 0
  for x in Orilla:
    if x == "Misionero":
      Misionero += 1
  return Misionero  


'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla,Objeto):
  for x in Orilla:
    if x == Objeto:
      Objeto +=1
  return Objeto

  #Aqui ya que tenemos los if solo seria quitar la parte de recursividad porque en si son las reglas 


