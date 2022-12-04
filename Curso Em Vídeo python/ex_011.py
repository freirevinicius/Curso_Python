#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area_parede = altura * largura
litros_tinta = area_parede / 2

print('Sua parede tem a dimensao de {}m x {}m. \nA área total é de {}m². \nPara pintar toda a parede você precisará de {}L de tinta'.format(largura, altura, area_parede, litros_tinta))