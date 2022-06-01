# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
#  que calcule e escreva o número de anos necessários para que a população do país
#  A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Altere o programa anterior permitindo ao usuário informar as
# populações e as taxas de crescimento iniciais. Valide a entrada
#  e permita repetir a operação.

populacao_a = float(input('População do país A: '))
tx_cresc_a = float(input('Taxa de crescimento do país A [%]: '))
populacao_b = float(input('População do país B: '))
tx_cresc_b = float(input('Taxa de crescimento do país B [%]: '))
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * tx_cresc_a / 100
    populacao_b += populacao_b * tx_cresc_b / 100
    anos += 1

print("A iguala ou ultrapassa B em %d anos" % anos)

