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

    cadastro = (int(input("Gostaria de se cadastrar? Digite 1-Sim ou 2-Não:")))
    if cadastro == 1:
        pessoa1 = {"Nome Completo:":"","CPF:":"","Senha:":"", "Apto para doar sangue:":""}
        pessoa2 = {"Nome Completo:":"","CPF:":"","Senha:":"", "Apto para doar sangue:":""}
        pessoa3 = {"Nome Completo:":"","CPF:":"","Senha:":"", "Apto para doar sangue:":""}
        pessoa4 = {"Nome Completo:":"","CPF:":"","Senha:":"", "Apto para doar sangue:":""}
        pessoa5 = {"Nome Completo:":"","CPF:":"","Senha:":"", "Apto para doar sangue:":""}
       
        pessoa1["Nome Completo:"] = "Ana Carolina Machado"
        pessoa1["CPF:"] = "834.304.060-05"
        pessoa1["Senha:"] = "m7fXYu4B"
        pessoa1["Apto para doar sangue:"] = "Sim"


        pessoa2["Nome Completo:"] = "Leonardo Vargas"
        pessoa2["CPF:"] = "621.512.330-73"
        pessoa2["Senha:"] = "r57wBRcd"
        pessoa2["Apto para doar sangue:"] = "Não"

        pessoa3["Nome Completo:"] = "Catarina Souza"
        pessoa3["CPF:"] = "690.537.410-54"
        pessoa3["Senha:"] = "M0fdGhfn"
        pessoa3["Apto para doar sangue:"] = "Sim"

        pessoa4["Nome Completo:"] = "André Rodrigues"
        pessoa4["CPF:"] = "612.916.930-25"
        pessoa4["Senha:"] = "5QPiq4sE"
        pessoa4["Apto para doar sangue:"] = "Sim"

        pessoa5["Nome Completo:"] = "Lilian Amaro"
        pessoa5["CPF:"] = "546.862.610-15"
        pessoa5["Senha:"] = "DqU4dXGX"
        pessoa5["Apto para doar sangue:"] = "Não"

        for x in pessoa1:
            print(x, pessoa1[x])
            print("Cadastro efetuado!")

        for x in pessoa2:
            print(x, pessoa2[x])
            print("Cadastro efetuado!")

        for x in pessoa3:
            print(x, pessoa3[x])
            print("Cadastro efetuado!")

        for x in pessoa4:
            print(x, pessoa4[x])
            print("Cadastro efetuado!")

        for x in pessoa5:
            print(x, pessoa5[x])
            print("Cadastro efetuado!")

    if cadastro == 2:
        print("Cadastro negado!")

else:
    print("Você não pode ser um doador.")