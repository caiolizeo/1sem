numero = int(input("Digire o npumero --> "))

if(numero >= 0 and numero <= 30):
    print("O número {} está entre 0 e 30".format(numero))
elif(numero >= 40 or numero <= 79):
    print("O número {} está entre 40 e 79".format(numero))
else:
    print("O número {} está fora dos limites estabelecidos".format(numero))
