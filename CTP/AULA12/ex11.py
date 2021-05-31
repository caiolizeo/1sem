maior = -999999
menor = 999999

for cont in range(1, 5):
    num = int(input("digite o número: "))
    
    if(menor > num):
        menor = num
    elif(maior < num):
        maior = num

print("maior número: {} \nmenor número: {}".format(maior, menor))







'''
Escreva um algoritmo em Python que leia 20 números inteiros e mostre qual foi o maior e o menor valor fornecido.
'''