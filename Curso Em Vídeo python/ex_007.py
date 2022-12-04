#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

n1 = int(input('Digite a nota 1 >> '))
n2 = int(input('Digite a nota 1 >> '))
media = (n1 + n2) / 2

print('A média entre {} e {} é {:.1f}'.format(n1, n2, media))