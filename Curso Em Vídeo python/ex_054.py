#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual =  date.today().year
maior = 0
menor = 0

for pessoa in range (1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Dentre as {} pessoas, {} são de maior e {} são de menor '.format(pessoa,maior, menor))