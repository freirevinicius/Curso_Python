#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint  
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogada_computador = randint(0,2)

jogada_usuario = int(input('''SELECIONE UMA OPÇÃO
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
QUAL É SUA JOGADA? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(itens[jogada_computador]))
print('Jogador jogou {}'.format(itens[jogada_usuario]))
print('-='*11)

if jogada_computador == 0:
    if jogada_usuario == 0:
        print('EMPATOU')
    elif jogada_usuario == 1:
        print('VOCÊ VENCEU')
    elif jogada_usuario == 2:
        print('VOCÊ PERDEU')
    else:
        print('OPÇÃO INVÁLIDA. ENCERRANDO...')
elif jogada_computador == 1:
    if jogada_usuario == 0:
        print('VOCÊ PERDEU') 
    elif jogada_usuario == 1:
        print('EMPATOU')
    elif jogada_usuario == 2:
        print('VOCÊ VENCEU')
    else:
        print('OPÇÃO INVÁLIDA. ENCERRANDO...')
elif jogada_computador == 2:
    if jogada_usuario == 0:
        print('VOCÊ VENCEU')
    elif jogada_usuario == 1:
        print('VOCÊ PERDEU') 
    elif jogada_usuario == 2:
        print('EMPATOU')
    else:
        print('OPÇÃO INVÁLIDA. ENCERRANDO...')
        