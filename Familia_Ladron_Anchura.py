import copy

estInicio = [[  [["Policia","Cholo","Papa","Hijo","Hijo","Mama","Hija","Hija"],[]]   ]]
estFinal   = ["Policia","Cholo","Papa","Hijo","Hijo","Mama","Hija","Hija"]
numero = 0
Ida=False
List = []
'''
Si la orilla destino, el elemento 2 de nuestra lista de listas tiene el estado final, que diga  con un true que  se ha completado todos los
objetivos, solo con una pequeña modificacion agregando nuestro toque personal en cuanto a referencias otakus[Nota no servira esto para anchura]
'''
def OnePiece(estado_inicial,estado_final):
  if len(estado_inicial[1]) == len(estado_final):
    return True
  return False

'''Que retorne  un True si en la orilla que digamos exista el objeto que igual digamos para estar viendo asi hacer las reglas
'''
def validacionExisObjeto(Orilla,Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  return False


def OpcionesVal(estado_inicial):

  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]

  if len(orilla1) > 1 and validacionExisObjeto(orilla1,"Cholo") and not validacionExisObjeto(orilla1,"Policia"):
     return False

  if len(orilla2) > 1 and validacionExisObjeto(orilla2,"Cholo") and not validacionExisObjeto(orilla2,"Policia"):
    return False

  if validacionExisObjeto(orilla1,"Mama") and validacionExisObjeto(orilla1,"Hijo") and not validacionExisObjeto(orilla1,"Papa"):
    return False
  
  if validacionExisObjeto(orilla2,"Mama") and validacionExisObjeto(orilla2,"Hijo") and not validacionExisObjeto(orilla2,"Papa"):
    return False
  
  if validacionExisObjeto(orilla1,"Papa") and validacionExisObjeto(orilla1,"Hija") and not validacionExisObjeto(orilla1,"Mama"):
    return False
  
  if validacionExisObjeto(orilla2,"Papa") and validacionExisObjeto(orilla2,"Hija") and not validacionExisObjeto(orilla2,"Mama"):
    return False

  return True 


def reglas(estado_inicial,sentido):
  orilla1  = estado_inicial[0]
  orilla2 = estado_inicial[1]
  lista = []
  if sentido == False:      
    if validacionExisObjeto(orilla1,"Policia"):
      if validacionExisObjeto(orilla1,"Cholo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Cholo")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Cholo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])
            
      if validacionExisObjeto(orilla1,"Hijo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Hijo")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Hijo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Hija"):  
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Policia")
        copia_orilla1.remove("Hija")
        copia_orilla2.append("Policia")
        copia_orilla2.append("Hija")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla1,"Papa"):
      if validacionExisObjeto(orilla1,"Hijo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Papa")
        copia_orilla1.remove("Hijo")
        copia_orilla2.append("Papa")
        copia_orilla2.append("Hijo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Mama"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Papa")
        copia_orilla1.remove("Mama")
        copia_orilla2.append("Papa")
        copia_orilla2.append("Mama")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla1,"Mama"):
      if validacionExisObjeto(orilla1,"Hija"): 
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla1.remove("Mama")
        copia_orilla1.remove("Hija")
        copia_orilla2.append("Mama")
        copia_orilla2.append("Hija")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

      if validacionExisObjeto(orilla1,"Papa"):
        if validacionExisObjeto(orilla1,"Mama"):
          copia_orilla1 = copy.copy(orilla1)
          copia_orilla2 = copy.copy(orilla2)
          copia_orilla1.remove("Mama")
          copia_orilla1.remove("Papa")
          copia_orilla2.append("Mama")
          copia_orilla2.append("Papa")
          if OpcionesVal([copia_orilla1,copia_orilla2]):
            lista.append([copia_orilla1,copia_orilla2])
    return lista

  if sentido == True:  
    if validacionExisObjeto(orilla2,"Policia"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Policia")
      copia_orilla1.append("Policia")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Policia"):
      if validacionExisObjeto(orilla2,"Cholo"):
        copia_orilla1 = copy.copy(orilla1)
        copia_orilla2 = copy.copy(orilla2)
        copia_orilla2.remove("Policia")
        copia_orilla2.remove("Cholo")
        copia_orilla1.append("Policia")
        copia_orilla1.append("Cholo")
        if OpcionesVal([copia_orilla1,copia_orilla2]):
          lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Papa"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Papa")
      copia_orilla1.append("Papa")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    if validacionExisObjeto(orilla2,"Mama"):
      copia_orilla1 = copy.copy(orilla1)
      copia_orilla2 = copy.copy(orilla2)
      copia_orilla2.remove("Mama")
      copia_orilla1.append("Mama")
      if OpcionesVal([copia_orilla1,copia_orilla2]):
        lista.append([copia_orilla1,copia_orilla2])

    return lista



'''
Iniciamos el tiempo, y despues ejecutamos elalgoritmo de busqueda en donde si sale retornara un True, imprimara el texto y 
dara inicio al ciclo for que imprimira toda la lista donde se encuentra los pasos que siguio (todo el contenido de nuestra
 pila  recorriendolo con un for) para llegar al estado final
Iniciamos el segundo estado de tiempo y restamos el tiempo final menos eltiempo inicial para poder ver el tiempo final 
'''
profundidad_inicio = time.time()
if busquedaAnchura(estInicio,estFinal,Ida):
  print("Llegaste a Laugh Tale")
  print("Nota: Obvia el estado donde regresa solo y no lo agrega a ls List de estados")
  print("|")
  print("v")
  for i in List:
    print(i)

profundidad_final= time.time()
print("\nBúsqueda finalizada en",profundidad_final - profundidad_inicio,"segundos\n")
          