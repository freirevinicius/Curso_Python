# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
import math

raio = float(input("QUAL O RAIO DO CÍRCULO? (EM CM) "))

area = math.pi * (raio * raio)
print(round(area, 1))
