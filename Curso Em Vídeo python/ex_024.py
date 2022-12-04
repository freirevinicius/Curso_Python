#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'

nome_cidade =  str(input('Digite o nome da cidade ')).strip()
print(nome_cidade[5].upper == 'SANTO')
