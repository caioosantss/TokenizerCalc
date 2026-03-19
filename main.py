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

Conectivos = {
        "Com","de",
}

#com os dados tratados e identificados começamos a elaborar a lógica da calculadora      

tokens = []

for palavra in texto.split():

    
    if palavra in valores:

        tokens.append({'tipo': 'NUM', 'val': float(palavra)})

    elif vo.verificar_op(palavra):

        tokens.append({'tipo': 'OP', 'val': vo.verificar_op(palavra)[0]})
        
    elif palavra in Conectivos:

        tokens.append({'tipo': 'CON', 'val': palavra})

# 2. Processar a lógica com a consciência do "de"
# Vamos supor que queremos resolver a primeira conta encontrada

num1 = None
num2 = None
inverter = False
op = 0


for i in range(len(tokens)):

    t = tokens[i]

    print(f'rodou {i} vezes')

    if t['tipo'] == 'CON' and t['val'] == 'de':

        inverter = True
   

    if t['tipo'] == 'OP':
        op += 1

    if t['tipo'] == 'NUM':

        if num1 is None:

            num1 = t['val']

        else:

            num2 = t['val']

            if inverter:

                if resultado:

                    num1 = resultado
        
            swap = num1
            num1 = num2
            num2 = swap
            print(num1,num2)
            break
        
    print(num1,num2)        


resultado = cal.calculadora(num1, num2, operacao[0])

print(resultado)