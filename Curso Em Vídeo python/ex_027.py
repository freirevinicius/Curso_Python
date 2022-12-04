#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite o nome completo:')).strip().upper()
nome_dividido = nome.split()
print('Seu primeiro nome é {}'.format(nome_dividido[0]))
print('Seu último nome é {}'.format(nome_dividido[len(nome_dividido)-1]))
