idade = 0
peso  = 0
horas = 0

idade = (int(input("Insira a sua idade: ")))
peso  = (float(input("Insira o seu peso: ")))
horas = (int(input("Insira quantas horas de sono tiveste na ultima noite: ")))

if idade >= 16 and idade <= 69:
    idade += 1
else:
    print("Idade fora dos requisitos!")
if peso > 50:
    peso += 1
else:
    print("Peso fora dos requisitos!")
if horas >= 6:
    horas += 1
else:
    print("Horas de sono fora dos requisitos!")
if idade == 1 and peso == 1 and horas == 1:
    print("Você pode ser um doador!")
else:
    print("Você não pode ser um doador.")