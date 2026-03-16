# video do professor: https://www.youtube.com/watch?v=gZBV7FlHDtg&t=1279s minuto:19:52

# Crie uma variável horário e exiba mensagem de
#  cumprimento relativo ao horário Bom dia boa tarde etc...

horario = float(input("Qaul e o horario? "))

if horario >= 6 and horario < 11:

    print("bom dia!!")

elif horario >= 11 and horario < 18:
    print("boa tarde! ")

elif horario >= 18 and horario < 24:
    print("boa noite!! ")

else:
    print("boa madrugrada! ")


###__________________________________________________________
### tambem pode ser assim ussando o and so que escondido:


# horario = float(input("Qual é o horário? "))

# if 6 <= horario < 11:
#     print("Bom dia!!")

# elif 11 <= horario < 18:
#     print("Boa tarde!")

# elif 18 <= horario < 24:
#     print("Boa noite!!")

# else:
#     print("Boa madrugada!")