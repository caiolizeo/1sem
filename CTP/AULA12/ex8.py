soma = 0
for num in range(0, 501, 3):
    
    if(num%2 != 0):
        
        soma+=num

print("Soma de todos os números ímpares múltiplos de 3 entre 1 e 500: {}".format(soma))