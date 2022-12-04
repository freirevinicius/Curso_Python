#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
numero_aleatorio = random.randint(0,5)
numero = int(input('Digite um número de 0 a 5 '))
print('PROCESSANDO...')
sleep(3)

if numero == numero_aleatorio:
    print('Você venceu, o número aleatório era {}. PARABÉNS!!'.format(numero_aleatorio))
else:
    print('Voce perdeu, o número aleatório era {}'.format(numero_aleatorio))
