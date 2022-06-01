# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("QUAL A ALTURA? \n "))
sexo = int(input("Homem [1] Mulher [2] \n"))

if sexo == 1:
    p_ideal_homem = (72.7 * altura) - 58
    print("O pesso ideal de um homem com {}m é: {}".format(
        altura, round(p_ideal_homem, 1)))
elif sexo == 2:
    p_ideal_mulher = (62.1*altura) - 44.7
    print("O pesso ideal de uma mulher com {}m é: {}".format(
        altura, round(p_ideal_mulher, 1)))
