#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

celsius = float(input('Informe a temperatura em °C'))
fahrenheit = celsius * 1.8 + 32

print('A temperatura de {}°C corresponde a {}°F'.format(celsius, fahrenheit))