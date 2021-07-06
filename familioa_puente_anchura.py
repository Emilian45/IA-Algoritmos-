
#IMPORTAIONES
import copy

estadoInicial = [[[[1,3,6,8,12],[]]]]
linterna = [1,3,6,8,12]
List = []
Ida=False

'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene los 3 objetos que diga  con un true que  se ha completado todos los
objetivos
'''
def OnePiece(estado_inicial, estado_final):
  if len(estado_inicial[1]) == len(estado_final):
    return True
  else:
    return False
'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''

def validacionExisObjeto(Orilla, objeto):
  for x in Orilla:
    if x == objeto:
      return True
  return False