#Comenzamos con esta wea
import copy
import time

'''
Un mapa con dos orillas, un río con barca 1 ladrón, 1 policía, 1 padre, 1
madre, 2 niñas y 2 niños
'''
estInicio= [["Padre","Hijo","Hijo","Madre","Hija","Hija","Policia","Cholo"],[]]
estFinal=[[],["Padre","Hijo","Hijo","Madre","Hija","Hija","Policia","Cholo"]]
List=[]
Ida= False


def OnePiece(estado_actual, estado_final):
    if len(estado_actual)==estado_final:
        return True
    else:
        return False

def validacionExisObjeto(Orilla, Objeto):
  for i in Orilla:
    if i == Objeto:
      return True
  else:
    return False

def reglas(estado_actual,sentido):
    orilla1=estado_actual[0]
    orilla2=estado_actual[1]
    totalel = len(orilla1) + len(orilla2)

    if len(orilla1) > 0 and len(orilla2) > 0 or len(orilla1) == 0 and len(orilla2) == totalel:

        if sentido == True:
            if orilla2[len(orilla2) - 1] == "Hijo" or orilla2[len(orilla2) - 1] == "Hija" or orilla2[len(orilla2) - 1] == "Cholo":
                return False

        if sentido == False:
            if orilla1[len(orilla1) - 1] == "Hijo" or orilla1[len(orilla1) - 1] == "Hija" or orilla1[len(orilla1) - 1] == "Cholo":
                return False
        '''
        Validamos que ningun miembro se quede solo con el orilla2 sin la presencia del policia 
        '''
        if len(orilla1) >= 2 and validacionExisObjeto(orilla1,"Cholo") and not validacionExisObjeto(orilla1,"Policia") or len(orilla2) >= 2 and validacionExisObjeto(orilla2,"Cholo") and not validacionExisObjeto(orilla2,"Policia"):
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
            return orilla1

    return True

Prof=20

def busquedaProfundidad(estado_actual, estado_final, sentido, abajo):
    if len(List)-1 < Prof and reglas(estado_actual, abajo):
        List.append(estado_actual)
        orilla1= estado_actual[0] 
        orilla2= estado_actual[1]
        copia_profundidad =copy.copy(abajo)

        if OnePiece(orilla2,estado_final):
            return True

        else:
            if sentido==False:
                cambiosentido= True
                for x in orilla1:
                    copia_orilla1= copy.copy(orilla1)
                    copia_orilla1.remove(x)
                    for y in copia_orilla1:
                        copia2_orilla1 = copy.copy(orilla1)
                        copia_orilla2 = copy.copy(orilla1)
                        copia2_orilla1.remove(x)
                        copia2_orilla1.remove(y)
                        copia_orilla2.append(x)
                        copia_orilla2.append(y)
                        if busquedaProfundidad([copia2_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
                            return True
            if sentido==True:
                cambiosentido= False
                for x in orilla1:
                    copia_orilla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_orilla1.remove(x)
                    copia_orilla1.append(x)
                    if busquedaProfundidad([copia_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
                        return True
            if sentido==True:
                cambiosentido= False
                for x in orilla1:
                    copia_orilla2= copy.copy(orilla2)
                    copia_orilla2.remove(x)
                    for y in copia_orilla2:
                        copia2_orilla2 = copy.copy(orilla2)
                        copia_orilla1 = copy.copy(orilla1)
                        copia2_orilla2.remove(x)
                        copia2_orilla2.remove(y)
                        copia_orilla1.append(x)
                        copia_orilla1.append(y)
                        if busquedaProfundidad([copia_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
                          return True

            List.pop()
        return False

if  busquedaProfundidad(estInicio, estFinal,Ida, Prof):
    print("Llegaste a Laugh Tale")
    for a in List:
        print(a)