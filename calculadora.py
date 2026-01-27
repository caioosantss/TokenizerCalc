def calculadora(a,b,op,inv):
    if 'adição' in op :
        resultado = a + b
        return resultado
    
    if inv==False and 'subtração' in op:
        resultado = a - b
        return resultado
    
    elif inv==True and 'subtração' in op:
        resultado = b - a
        return resultado   
    
    elif 'multiplicação' in op:
        resultado = a*b
        return resultado
     
    elif inv==False and 'divisão' in op:
        resultado = a/b
        return resultado
    
    elif inv==True and 'divisão' in op:
        resultado = b/a
        return resultado
    
    else:
        print('conta inconclusiva')
    