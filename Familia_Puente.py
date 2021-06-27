import copy
import time

estInicio= [[1,3,6,8,12,],[]]
List=[]
lampara=30

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])==5:
        return True
    else:
        return False

def BuscaExsitenciaSujeto(orlla,sujeto):
    for i in orilla:
        if sujeto ==i:
            return True
    
    return  False

Prof = 20 #La maxima cantidad de estados aceptar en nuestra cola

def busquedaProfundidad(estado_inicial, luz):
    List.append(estado_inicial)
    orilla1= List[0]
    orilla2= List[1]

    if EstadoFEncontrado(estado_inicial):
        return True

    else:

        if len(List)-1 < Prof and len(orilla1)>0 and luz >0:
            #Movimientos con el 1
            #Velocidad del 3
            if  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,3)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(3)
                copia_orilla2.append(1)
                copia_orilla2.append(3)
                copia_luz= copy.copy(luz)-3
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 3"],copia_luz)
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,6)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(6)
                copia_orilla2.append(1)
                copia_orilla2.append(6)
                copia_luz= copy.copy(luz)-6
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 6"],copia_luz)
                    return True

            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,8)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(8)
                copia_orilla2.append(1)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz)
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,1) and BuscaExsitenciaSujeto(orilla1,12)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(1)
                copia_orilla1.remove(12)
                copia_orilla2.append(1)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz)
                    return True


            #Movimientos  con el 2 mas rapido
            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,6)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(6)
                copia_orilla2.append(3)
                copia_orilla2.append(6)
                copia_luz= copy.copy(luz)-6
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 6"],copia_luz)
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,8)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(8)
                copia_orilla2.append(3)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz)
                    return True

            elif  BuscaExsitenciaSujeto(orilla1,3) and BuscaExsitenciaSujeto(orilla1,12)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(3)
                copia_orilla1.remove(12)
                copia_orilla2.append(3)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz)
                    return True

            #Movimientos con el tercero mas rapido 

            elif  BuscaExsitenciaSujeto(orilla1,6) and BuscaExsitenciaSujeto(orilla1,8)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(6)
                copia_orilla1.remove(8)
                copia_orilla2.append(6)
                copia_orilla2.append(8)
                copia_luz= copy.copy(luz)-8
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 8"],copia_luz)
                    return True
            
            elif  BuscaExsitenciaSujeto(orilla1,6) and BuscaExsitenciaSujeto(orilla1,12)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(6)
                copia_orilla1.remove(12)
                copia_orilla2.append(6)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz)
                    return True
            #Movimientos con el cuarto
            elif  BuscaExsitenciaSujeto(orilla1,8) and BuscaExsitenciaSujeto(orilla1,12)
                copia_orilla1 = copy.copy(orilla1)
                copia_orilla2 = copy.copy(orilla2)
                copia_orilla1.remove(8)
                copia_orilla1.remove(12)
                copia_orilla2.append(8)
                copia_orilla2.append(12)
                copia_luz= copy.copy(luz)-12
                if busquedaProfundidad([copia_orilla1],[copia_orilla2,"Luz menos 12"],copia_luz)
                    return True
                    