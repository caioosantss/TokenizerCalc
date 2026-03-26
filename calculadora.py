def calculadora(a,b,op):
    
    if 'adição' in op :
        resultado = a + b
        return resultado
    
    elif 'subtração' in op:
        resultado = a - b
        return resultado   
    
    elif 'multiplicação' in op:
        resultado = a*b
        return resultado
     
    elif 'divisão' in op:
        resultado = a/b
        return resultado

    
    else:
        print('conta inconclusiva')
    