# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
print('''Qual base de conversão deseja? 
[1] Binário 
[2] Octal 
[3] Hexadecimal ''')
opcao = int(input('SELECIONE... '))

if opcao == 1:
    print('{} convertido para BINÁRIO é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida! ENCERRANDO...')