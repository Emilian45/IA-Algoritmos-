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