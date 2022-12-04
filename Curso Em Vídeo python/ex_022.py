#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem no nome, sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = str(input('Qual o nome completo?')).strip() 
nome_dividido = nome.split()

print('Analisando o nome...')
print('{} em maiúsculo fica {}'.format(nome, nome.upper()))
print('{} em minúsculo fica {}'.format(nome, nome.lower()))
print('O nome {} tem {} letras'.format(nome, len(nome) - nome.count(' ')))
print('Primeiro nome é {} e tem {} letras'.format(nome_dividido[0], len(nome_dividido[0])))
