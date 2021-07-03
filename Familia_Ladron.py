import copy
import time

estInicio = [["Policia","Ladron","Padre","Hijo","Hijo","Madre","Hija","Hija"],[]]
estFinal   = [[],["Policia","Ladron","Padre","Hijo","Hijo","Madre","Hija","Hija"]]
profundidad = 20
ida = False
List = []

def OnePiece(estado_inicial,estado_final):
  if len(estado_inicial) == len(estado_final):
    return True
  return False

def validacionExisObjeto(Orilla,Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  return False

def reglas(estado_inicial,sentido):
  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]
  NoElementos = len(orilla1) + len(orilla2)
  '''
  Primero guardamos los arreglos orilla1 y orilla2 de nuestro estado actual en  variables,
  Añadimos una variable que va a contener el numero total de elementos que tiene nuestro
  estado actual, despues indicamos que vlide cualquier otro estado que no sea el inicial
  '''
  if len(orilla1) > 0 and len(orilla2) > 0 or len(orilla1) == 0 and len(orilla2) == NoElementos:
    '''
    El valor 1 en direc indica que el movimiento realizado fue orilla1 -> orilla2
    despues validamos que el elemento que el ultimo elemento que paso  fuese un Padre, Madre o Policia,
    de no serlo retornará un False 
    '''
    if sentido == 1:
      if orilla2[len(orilla2) - 1] == "Hijo" or orilla2[len(orilla2) - 1] == "Hija" or orilla2[len(orilla2) - 1] == "Ladron":
        return False

    if sentido == 0:
      if orilla1[len(orilla1) - 1] == "Hijo" or orilla1[len(orilla1) - 1] == "Hija" or orilla1[len(orilla1) - 1] == "Ladron":
        return False
    '''
    Validamos que ningun miembro se quede solo con el ladron sin la presencia del policia 
    '''
    if len(orilla1) >= 2 and validacionExisObjeto(orilla1,"Ladron") and not validacionExisObjeto(orilla1,"Policia") or len(orilla2) >= 2 and validacionExisObjeto(orilla2,"Ladron") and not validacionExisObjeto(orilla2,"Policia"):
      return False
    '''
    Validamos que ningun hijo se quede solo con la Madre sin la presencia del Padre 
    '''
    if validacionExisObjeto(orilla1,"Hijo") and validacionExisObjeto(orilla1,"Madre") and not validacionExisObjeto(orilla1,"Padre") or validacionExisObjeto(orilla2,"Hijo") and validacionExisObjeto(orilla2,"Madre") and not validacionExisObjeto(orilla2,"Padre"):
        return False
    '''
    Validamos que ninguna Hija se quede solo con el Padre sin la presencia de la Madre 
    '''
    if validacionExisObjeto(orilla1,"Hija") and validacionExisObjeto(orilla1,"Padre") and not validacionExisObjeto(orilla1,"Madre") or validacionExisObjeto(orilla2,"Hija") and validacionExisObjeto(orilla2,"Padre") and not validacionExisObjeto(orilla2,"Madre"):
        return False

  return True

Prof=20

def busquedaProfundidad(estado_inicial,estado_final,sentido,prof):
  if len(List)-1 < Prof:
    if reglas(estado_inicial,sentido):
      copia_profundidad = copy.copy(prof)
      copia_profundidad -= 1
      List.append(estado_inicial)
      orilla1  = estado_inicial[0]
      orilla2 = estado_inicial[1]
      ef      = estado_final[1]
      if OnePiece(orilla2,ef):
        return True
      else:
        if sentido == False:
          cambiosentido = True
          for x in orilla1:
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla1.remove(x)
            for y in copia_orilla1:
              copia2_orilla1 = copy.copy(orilla1)
              copia_orilla2 = copy.copy(orilla2)
              copia2_orilla1.remove(x)
              copia2_orilla1.remove(y)
              copia_orilla2.append(x)
              copia_orilla2.append(y)
              if busquedaProfundidad([copia2_orilla1,copia_orilla2,"Enviamos: ",x,y],estado_final,cambiosentido,copia_profundidad):
                return True
        if sentido == True:
          cambiosentido = False
          for x in orilla2:
            copia_orilla1 = copy.copy(orilla1)
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla2.remove(x)
            copia_orilla1.append(x)
            if busquedaProfundidad([copia_orilla1,copia_orilla2,"Regresamos a ",x],estado_final,cambiosentido,copia_profundidad):
              return True
        if sentido == True:
          cambiosentido = False
          for x in orilla2:
            copia_orilla2 = copy.copy(orilla2)
            copia_orilla2.remove(x)
            for y in copia_orilla2:
              copia2_orilla2 = copy.copy(orilla2)
              copia_orilla1 = copy.copy(orilla1)
              copia2_orilla2.remove(x)
              copia2_orilla2.remove(y)
              copia_orilla1.append(x)
              copia_orilla1.append(y)
              if busquedaProfundidad([copia_orilla1,copia2_orilla2,"Regresamos a ",x,y],estado_final,cambiosentido,copia_profundidad):
                return True
        List.pop()      
    return False

'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio  para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()

if busquedaProfundidad(estInicio,estFinal,ida,profundidad):
  print("Llegaste a Laugh Tale")
  for a in List:
    print(a)
else:
  print("Aun esta Barbanegra")  

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
