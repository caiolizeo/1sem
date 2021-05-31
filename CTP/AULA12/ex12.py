n = int(input("Digite o número desejado: "))
continua = "S"

while(continua == "S"):

    while(n < 0):
        print("número inválido")
        n = int(input("Digite o número desejado novamente: "))

    for tab in range(1, 11):
        print(n,"x",tab,"=",(n*tab))
    
    continua = str.upper(input("\nDigitar outro número? \nS = Sim | N = Não --> "))
    if(continua == "S"):
        n = int(input("Digite o número desejado: "))
        print("")

print("*** FIM ***")
