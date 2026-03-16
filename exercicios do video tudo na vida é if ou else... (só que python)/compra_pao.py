# video do professor: https://www.youtube.com/watch?v=gZBV7FlHDtg&t=1279s minuto:19:20

# objetivo 1: Crie crie um programa onde o preço do pão será aguardado em uma variável
# após isso o usuário digitará quanto dinheiro ele tem Caso ele tenha dinheiro suficiente uma mensagem será exibida 
# informando que ele comprou o pão Caso contrário sei lá evento uma mensagem aí KKKKK


preço_pao = float(3.99)

dinheiro_clinte = float(input("Quanto dinheiro vocer tem? "))

if dinheiro_clinte >= preço_pao:
    print("Voce comprou po pao👌 ")
    dinheiro_clinte -= preço_pao
    print(f"dinherio restante: {dinheiro_clinte}")
else:
    print("Voce nao tem dinheiro suficiente seu pobre🥱: ")


