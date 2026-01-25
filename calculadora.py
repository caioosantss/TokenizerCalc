def calculadora(a,b,op):
    if 'som' in op :
        resultado = a + b
        return resultado
    elif 'menos' in op:
        resultado = a - b
        return resultado
    elif 'subt' in op:
        resultado = b - a
        return resultado
    elif 'vezes' in op:
        resultado = a*b
        return resultado
    elif 'multipl' in op:
        resultado = b*a
        return resultado
    elif 'divid' in op:
        resultado = a/b
        return resultado
    else:
        print('conta inconclusiva')
    