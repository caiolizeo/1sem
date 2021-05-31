
num1 = int(input("Digite o número 1 \n--> "))
num2 = int(input("Digite o número 2 \n--> "))
impar = 0

while(num1 <= num2):
    if(num1%2 != 0):
        print(num1)
        impar+=1
    num1+=1

print("números ímpares: {}".format(impar))











'''
Elabore um programa em Python que seja capaz de contar a quantidade de números 
ímpares existentes entre dois números fornecidos pelo usuário.
'''