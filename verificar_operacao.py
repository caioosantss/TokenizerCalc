import re

def verificar_op(texto):

    tipo_op = {
        '+':'soma','mais':'soma','some':'soma','adcione':'soma','adciona':'soma', 'soma':'soma',
        '-':'subtração','subtraia':'subtração','tire':'subtração','tira':'subtração','menos':'subtração',
        '*':'multiplicação','vezes':'multiplicação'
        } 

    texto = texto.split()

    operações = []

    for i in texto:
        if i in tipo_op:
            operações.append(i)

    return operações

def inv (texto):

    preposiçao = {'de':'preposição','do':'preposição'}

    inverter = False

    for i in texto:
        if i in preposiçao:
            inverter = True

        return inverter
