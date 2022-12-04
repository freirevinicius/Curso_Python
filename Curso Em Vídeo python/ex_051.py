#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = termo + (10 - 1) * razao

for contador in range (termo, decimo_termo + razao, razao):
    print('{} '.format(contador), end='-> ')

print('FIM')