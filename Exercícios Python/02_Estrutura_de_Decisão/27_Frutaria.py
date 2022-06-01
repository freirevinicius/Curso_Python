# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
#  para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
#  e escreva o valor a ser pago pelo cliente.


morangos = int(input("Quantos Kg de morango? "))
macas = int(input("Qunatos Kg de maçã? "))

if morangos > 0 and morangos <= 5:
    preco_morangos_ate_5 = morangos * 2.5
else:
    preco_morangos_mais_5 = morangos * 2.2

if macas > 0 and macas <= 5:
    preco_macas_ate_5 = macas * 1.8
else:
    preco_macas_mais_5 = macas * 1.5

if morangos > 0 and morangos <= 5:
    preco_final_morangos = preco_morangos_ate_5
else:
    preco_final_morangos = preco_morangos_mais_5

if macas > 0 and macas <= 5:
    preco_final_macas = preco_macas_ate_5
else:
    preco_final_macas = preco_macas_mais_5

total = preco_final_macas + preco_final_morangos

desconto = total * 0.10

if total >= 25 or ((morangos + macas) >= 8):
    total = total - desconto

print('Valor da compra R$', total)
