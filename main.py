import re
import verificar_operacao as vo
import calculadora as cal 
from verificar_operacao import inv

identificadores = {}

while True:

    texto = input('Insira a conta que deseja fazer: ').lower()

    valores = re.findall(r'-?\d+[.,]?\d*', texto)
    
    operacao = vo.verificar_op(texto)

    for id, palavra in enumerate(texto.split()):
        
        identificadores[id] = palavra   

    if len(valores) >= 2 and operacao is not None:
        break 
    
    if len(valores) < 2:

        print("-> Erro: Digite ao menos dois números (ex: 5 + 10).")

    elif operacao is None:

        print("-> Erro: Não encontrei uma operação válida (+, -, *, /).")


inverter = inv(texto)

conta = []

i = 0

resultado = None


#a partir daqui serão montadas as contas

for op in range(0,len(operacao)):

    for i in range(i,len(valores)):

        conta.append(valores[i])

        if resultado is None and len(conta) == 2:

            resultado = cal.calculadora(int(conta[0]),int(conta[1]),operacao[op],inverter)
            conta = []
            break
#caso o numero de operações nao aborde todos os valores, o seguinte loop se inicia

        elif len(conta) == 2:

            resultado = cal.calculadora(int(resultado),int(valores[i]),operacao[op],inverter)

print(resultado)