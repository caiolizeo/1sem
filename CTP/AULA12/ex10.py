numero=int(input("Digite o número: "))

if(numero%1 == 0 and numero%numero == 0):
    print("É número primo")
else:
    print("Não é primo")