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

    if len(orilla1) > 0 and len(orilla2) > 0 or len(orilla1) == 0 and len(orilla2) == totalel:

        if direc == True:
            if orilla2[len(orilla2) - 1] == "Hijo" or orilla2[len(orilla2) - 1] == "Hija" or orilla2[len(orilla2) - 1] == "Cholo":
                return False

        if direc == False:
            if orilla1[len(orilla1) - 1] == "Hijo" or orilla1[len(orilla1) - 1] == "Hija" or orilla1[len(orilla1) - 1] == "Cholo":
                return False
        '''
        Validamos que ningun miembro se quede solo con el orilla2 sin la presencia del policia 
        '''
        if len(orilla1) >= 2 and busca(orilla1,"orilla2") and not busca(orilla1,"Policia") or len(orilla2) >= 2 and busca(orilla2,"orilla2") and not busca(orilla2,"Policia"):
            return False
        '''
        Validamos que ningun hijo se quede solo con la Madre sin la presencia del Padre 
        '''
        if busca(orilla1,"Hijo") and busca(orilla1,"Madre") and not busca(orilla1,"Padre") or busca(orilla2,"Hijo") and busca(orilla2,"Madre") and not busca(orilla2,"Padre"):
            return False
        '''
        Validamos que ninguna Hija se quede solo con el Padre sin la presencia de la Madre 
        '''
        if busca(orilla1,"Hija") and busca(orilla1,"Padre") and not busca(orilla1,"Madre") or busca(orilla2,"Hija") and busca(orilla2,"Padre") and not busca(orilla2,"Madre"):
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
            if direccion==False:
                cambiosentido= True
                for x in orilla1:
                    copia_orilla1= copy.copy(orilla1)
                    copia_orilla1.remove(x)
                    for y in copia_prolla1:
                        copia2_orilla1 = copy.copy(orilla1)
                        copia_orilla2 = copy.copy(orilla1)
                        copia2_orilla1.remove(x)
                        copia2_orilla1.remove(y)
                        copia_orilla2.append(x)
                        copia_orilla2.append(y)
                        if busquedaProfundidad([copia2_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
                            return True
            if direccion==True:
                cambiosentido= False
                for x in orilla1:
                    copia_prolla1 = copy.copy(orilla1)
                    copia_orilla2 = copy.copy(orilla2)
                    copia_prolla1.remove(x)
                    copia_prolla1.append(x)
                    if busquedaProfundidad([copia_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
                        return True
            if direccion==True:
                cambiosentido= False
                for x in orilla1:
                    copia_orilla2= copy.copy(orilla2)
                    copia_orilla2.remove(x)
                    for y in copia_orilla2:
                        copia2_orilla2 = copy.copy(orilla2)
                        copia_orilla1 = copy.copy(orilla1)
                        copia2_orilla2.remove(x)
                        copia_orilla1.remove(y)
                        copia2_orilla2.append(X)
                        copia_orilla1.append(y)
                        if busquedaProfundidad([copia_orilla1,copia_orilla2], estado_final,cambiosentido, copia_profundidad):
            List.pop()
        return False

if  busquedaProfundidad(estInicio, estFinal,Ida, Prof):
    print("Llegaste a Laugh Tale")
    for a in List:
        print(a)
else:
    print("Solucion no encontrada")


            