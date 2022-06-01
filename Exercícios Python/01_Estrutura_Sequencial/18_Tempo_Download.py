# Faça um programa que peça o tamanho de um arquivo para download (em MB)
#  e a velocidade de um link de Internet (em Mbps), calcule e informe o
# tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Tamanho do arquivo (MB): "))
velocidade = float(input("Velocidade da Internet (MBps): "))

tempo = (tamanho_arquivo / velocidade) * 60
horas = tempo / 60
dias = horas / 24
print("Tempo Aproximado de Download {} minutos, ou seja {} horas, ou seja {} dias".format(round(tempo,2),round(horas,2),round(dias,2)))
