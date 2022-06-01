# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input("QUANTOS GRAUS (EM CELSIUS)?"))

f = c * 9/5 + 32

print("{} GRAUS CELSIUS SÃO {} GRAUS FAHRENHEIT".format(c, round(f, 2)))
