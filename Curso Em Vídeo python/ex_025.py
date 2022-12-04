#Crie um programa que leia o nome de uma pessoa e diga se ela tem ''SILVA'' no nome.

nome = str(input('Digite o nome completo: ')).strip()

print('O nome tem SILVA? {}'.format('silva' in nome.lower()))