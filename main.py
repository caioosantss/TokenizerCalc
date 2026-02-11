import re
import verificar_operacao as vo
import calculadora as cal 
from verificar_operacao import inv

texto = input('insira a conta que deseja fazer: ').lower()

valores = re.findall(r'\d+',texto)



conta = []

inverter = inv(texto)


operacao = vo.verificar_op(texto)

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


