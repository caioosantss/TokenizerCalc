import re

def verificar_op(texto):

    tipo_op = {
        '+':'soma','mais':'soma','some':'soma','adcione':'soma','adciona':'soma',
        '-':'subtração','subtraia':'subtração','tire':'subtração','tira':'subtração','menos':'subtração',
        '*':'multiplicação','vezes':'multiplicação'
        } 

