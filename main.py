import re
import verificar_operacao as vo
import calculadora as cal 
from verificar_operacao import inv

texto = input('insira a conta que deseja fazer ')

valores = re.findall(r'\d+',texto)

inverter = inv(texto)

operacao = vo.verificar_op(texto)

print(cal.calculadora(int(valores[0]),int(valores[1]),operacao[0],inverter))


