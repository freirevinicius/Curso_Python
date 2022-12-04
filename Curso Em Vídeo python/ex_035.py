#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input('Digite o valor da Reta 1 '))
reta_2 = float(input('Digite o valor da Reta 2 '))
reta_3 = float(input('Digite o valor da Reta 3 '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('PODEM FORMAR UM TRIÂNGULO')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')