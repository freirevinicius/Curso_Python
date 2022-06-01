# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if ((l1 + l2) <= l3) or ((l2 + l3) <= l1) or ((l1 + l3) <= l2):
    print("Não é um Triângulo.")
elif (l1 == l2) and (l1 == l3) and (l1 == l3):
    print("Triângulo Isóceles.")
elif (l1 != l2) and (l1 != l3) and (l2 != l3):
    print("Triângulo Escaleno.")
