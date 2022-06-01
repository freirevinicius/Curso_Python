# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#  Faça um programa capaz de gerar a série até o n−ésimo termo.


final = int(input('Até qual termo deseja imprimir? '))

primeiro = 0
segundo = 1

print(primeiro, end = ' ')
print(segundo, end = ' ')

for i in range (3, (final + 1)):
    terceiro = primeiro + segundo
    print(terceiro, end = ' ')
    primeiro = segundo
    segundo = terceiro