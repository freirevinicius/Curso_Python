# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

primeiro = 0
segundo = 1
resultado = 0

print(primeiro, end=' ')
print(segundo, end=' ')

while resultado <= 501:
    terceiro = primeiro + segundo
    print(terceiro, end=' ')
    primeiro = segundo
    segundo = terceiro
    resultado = terceiro