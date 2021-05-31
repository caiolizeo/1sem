numero_1 = float(input("Digite o primeiro número"))
numero_2 = float(input("Digite o segundo número"))
numero_3 = float(input("Digite o terceiro número"))

if(numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3):
    print("Os números digitados não podem ser iguais")
else:


    if(numero_1 < numero_2 and numero_2 < numero_3):
        print(numero_3, numero_2, numero_1)
    elif(numero_1 < numero_3 and numero_3 < numero_2):
        print(numero_2, numero_3, numero_1)
    elif(numero_2 < numero_1 and numero_1 < numero_3):
        print(numero_3, numero_1, numero_2)
    elif(numero_2 < numero_3 and numero_3 < numero_1):
        print(numero_1, numero_3, numero_2)
    elif(numero_3 < numero_2 and numero_2 < numero_1):
        print(numero_1, numero_2, numero_3)
    elif(numero_3 < numero_1 and numero_1 < numero_2):
        print(numero_2, numero_1, numero_3)