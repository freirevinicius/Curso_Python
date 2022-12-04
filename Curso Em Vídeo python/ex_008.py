#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

metros = float(input('Qual a distância em metros?'))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A medida de {}m corresponde a: \n{}Km \n{}Hm \n{}Dam \n{:.0f}Dm \n{:.0f}Cm \n{:.0f}Mm'.format(metros, km, hm, dam, dm, cm, mm))