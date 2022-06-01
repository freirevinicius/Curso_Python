# Altere o programa anterior para que ele aceite
# apenas números entre 0 e 1000.

quantidade = int(input('Quantos Números? '))

i = 1
maior = 0
menor = 0
soma = 0

while quantidade < 0 or quantidade > 1000:
    quantidade = int(input('Quantos Números? '))
    
while i <= quantidade:
    numero = int(input('Digite o número entre (1 e 1000): '))
    if i == 1:
        menor = numero
    if numero>= maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    soma += numero
    i += 1

print('O maior numero é: ', maior)
print('O menor número é: ', menor)
print('A soma é: ', soma)

    