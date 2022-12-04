#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
reta_1 = float(input('Digite o valor da Reta 1 '))
reta_2 = float(input('Digite o valor da Reta 2 '))
reta_3 = float(input('Digite o valor da Reta 3 '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    if reta_1 == reta_2 and reta_1 == reta_3 and reta_2 == reta_3:
        print('TRIÂNGULO EQUILÁTERO.')
    elif reta_1 == reta_2 or reta_2 == reta_3 or reta_1 == reta_3:
        print('TRIÂNGULO ISÓCELES')
    elif reta_1 != reta_2 and reta_1 != reta_3 and reta_2 != reta_3:
        print('ESCALENO')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')