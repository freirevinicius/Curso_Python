# Faça um programa para uma loja de tintas. O programa deverá pedir
# o tamanho em metros quadrados da área a ser pintada. Considere que
# a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_area = float(input('Tamanho da área (em metros quadrados): '))

cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0

litros = tamanho_area / cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)

if(litros % capacidade_lata != 0):
    latas_inteiras = latas_inteiras + 1

valor_total = latas_inteiras * preco_lata

print("Serão necessários {} litros de tinta" .format(litros))
print("Serão necessárias {} latas inteiras".format(latas_inteiras))
print("Valor da compra R$", valor_total)
