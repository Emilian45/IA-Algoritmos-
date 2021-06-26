import copy
import time

estInicio= [["Canibal","Canibal","Canibal","Misionero","Misionero","Misionero",],[]]]
List=[]

def EstadoFEncontrado(estado_inicial):
    if len(estado_inicial[1])>6:
        return False
    elif len(estado_inicial)==6:
        return True

def