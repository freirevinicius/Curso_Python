# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
#  número inteiro entre 1 a 10. O usuário deve informar de qual numero
# ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


tabuada = int(input('DESEJA SABER A TABUADA DE QUAL NÚMERO? '))


print('TABUADA DE %d' % tabuada)
contador = 0 
for i in range(contador, 10):
    i += 1
    resultado = tabuada * i  
    print(f'{tabuada} X {i:2} = {resultado:2}')
