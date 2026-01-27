import re
import verificar_operacao as vo
import calculadora as cal 

texto = input('insira a conta que deseja fazer ')

valores = re.findall(r'\d+',texto)


