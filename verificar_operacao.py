import re

def verificar_op(texto):

    tipo_op = {
        '+':'adição','mais':'adição','some':'adição','adcione':'adição','adciona':'adição', 'soma':'adição',
        '-':'subtração','subtraia':'subtração','tire':'subtração','tira':'subtração','menos':'subtração',
        '*':'multiplicação','vezes':'multiplicação','X':'multiplicação',
        '/':'divisão','divid':'divisão'
        } 

    texto = texto.split()

    operações = []

    for i in texto:
        if i in tipo_op:
            operações.append(tipo_op[i])

    return operações



def inv (texto):

    texto = texto.split()

    preposiçao = {'de':'preposição','do':'preposição'}

    inverter = False

    for i in texto:
        if i in preposiçao:
            inverter = True

    return inverter
