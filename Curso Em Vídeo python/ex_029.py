#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do carro? (km/h)'))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Velocidade permitida')