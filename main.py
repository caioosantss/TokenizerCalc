import re
import verificar_operacao as vo
import calculadora as cal 
from verificar_operacao import inv

texto = input('insira a conta que deseja fazer ')

valores = re.findall(r'\d+',texto)

total = []

conta = []

inverter = inv(texto)

operacao = vo.verificar_op(texto)

for i in range(0,len(valores)):
    conta.append(valores[i])
    if len(conta) == 2:
        calculo = cal.calculadora(int(conta[0]),int(conta[1]),operacao[i],inverter)
        total.append(int(calculo))
        conta = []
    elif len(valores) - i == 1:
        resultado = sum(total)
        op_atual = i - 1
        calculo = cal.calculadora(int(resultado),int(valores[0],operacao[op_atual]),inverter)
        print(op_atual)
print(calculo)




