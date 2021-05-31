destino=int(input("Digite o destino: 1-Norte | 2-Nordeste | 3-Centro-Oeste  "))
idaVolta=int(input("A passagem é de ida e volta? 1-SIM | 2-NAO  "))
invalida="Resposta inválida"

if(destino == 1):
    if(idaVolta == 1):
        print("Valor da passagem ida e volta para região Norte: R$400,00") 
    elif(idaVolta == 2):
        print("Valor da passagem somente de ida para região Norte: R$280,00")
    else:
        print(invalida)
elif(destino == 2):
    if(idaVolta == 1):
        print("Valor da passagem ida e volta para região Nordeste: R$628,00")
    elif(idaVolta == 2):
        print("Valor da passagem somente de ida para região Nordeste: R$380,00")
    else:
        print(invalida)
elif(destino == 3):
    if(idaVolta == 1):
        print("Valor da passagem ida e volta para região Centro-Oeste: R$1100,00")
    elif(idaVolta == 2):
        print("Valor da passagem somente de ida para região Nordeste: R$620,00")
    else:
        print(invalida)
else:
    print(invalida)
