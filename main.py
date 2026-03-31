import re
import verificar_operacao as vo
import calculadora as cal 

#começamos o código definindo a entrada e validação de dados

while True:

    texto = input('Insira a conta que deseja fazer: ').lower()

    valores = re.findall(r'-?\d+[.,]?\d*', texto)
    
    operacao = vo.verificar_op(texto)


    if len(valores) >= 2 and operacao is not None:
        break 
    
    if len(valores) < 2:

        print("-> Erro: Digite ao menos dois números")

    elif operacao is None:

        print("-> Erro: Não encontrei uma operação válida")


resultado = None

#este trecho serve para limpar os valores de entrada e criar ID's aos dados

conectivos = {
        "com","de",
}

#com os dados tratados e identificados começamos a elaborar a lógica da calculadora      

tokens = []

for palavra in texto.split():

    
    if palavra in valores:

        val_normalizado = palavra.replace(',', '.')
        tokens.append({'tipo': 'NUM', 'val': float(val_normalizado)})
        
    elif palavra in conectivos:

        tokens.append({'tipo': 'CON', 'val': palavra})

# 2. Processar a lógica com a consciência do "de"

num1 = None
num2 = None
inverter = False
op = 0
ops = []

for i in range(len(tokens)):

    t = tokens[i]


    if t['tipo'] == 'CON' and t['val'] == 'de':

        inverter = True
   
    if t['tipo'] == 'NUM':

        if num1 is None:

            num1 = t['val']

        else:

            num2 = t['val']


        if inverter and num2 is not None:
        
            num1, num2 = num2, num1
            inverter = False

        
    if num1 is not None and num2 is not None:
        
       
        resultado = cal.calculadora(num1,num2,operacao[op])
        op += 1          
        num1 = resultado  
        num2 = None

print(resultado)
print(num1)