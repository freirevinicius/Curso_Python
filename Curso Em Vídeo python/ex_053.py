#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

entrada = str(input('Digite uma frase: ')).upper().replace(" ", '')
total = len(entrada)
inverso = ''
for c in range(total, 0, -1):
    inverso += entrada[c - 1]
print('O inverso de {} é {}'.format(entrada, inverso))

if inverso == entrada:
    print('Sua frase é considerada um palíndromo !')
else:
    print('Sua frase NÃO é considerada um palíndromo')