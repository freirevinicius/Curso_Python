#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Qual tabuada deseja fazer? '))
print('-' * 12)
for i in range (1, 11):
    tabuada = i * numero
    print('{} x {:2} = {}'.format(numero, i, tabuada))

print('-' * 12)