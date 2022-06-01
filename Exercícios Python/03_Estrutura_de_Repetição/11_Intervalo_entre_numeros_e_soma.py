# Faça um programa que receba dois números inteiros e gere os números inteiros
#  que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o último número: '))

soma = 0

for i in range(num1, (num2 + 1)):
    print(i)
    soma += i
    
print('A soma dos números é %d' % soma)