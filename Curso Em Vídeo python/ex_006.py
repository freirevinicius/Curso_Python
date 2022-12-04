#Crie um algorimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número Inteiro >>>> '))

print('O dobro de {} vale {} \nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}.'.format(numero,(numero * 2), numero, (numero * 3), numero, (numero ** (1/2))))