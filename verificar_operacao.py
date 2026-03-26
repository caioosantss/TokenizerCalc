def verificar_op(texto):

    tipo_op = {
        '+':'adição','mais':'adição','some':'adição','adcione':'adição','adciona':'adição', 'soma':'adição',
        '-':'subtração','subtraia':'subtração','tire':'subtração','tira':'subtração','menos':'subtração',
        '*':'multiplicação','vezes':'multiplicação','X':'multiplicação','multiplique':'multiplicação',
        '/':'divisão','divida':'divisão', 'dividido':"divisão"
        } 

    texto = texto.split()

    operações = []

    for i in texto:
        if i in tipo_op:
            operações.append(tipo_op[i])

    return operações
