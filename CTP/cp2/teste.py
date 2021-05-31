descontoCupom = 0
cupom=str.upper(input("O Cliente possui cupom valido?\nS = SIM | N = NÃO\n--> "))
valorTotal = 100

while(cupom != "S" and cupom != "N"):
    print("Opção invalida!")
    cupom=str.upper(input("Digite novamente\nS = SIM | N = NÃO\n--> "))


if(cupom == "S"):

    tipoCupom=str.upper(input("Digite o nome do cupom\n--> "))

    while(tipoCupom != "BORALA10" and tipoCupom != "BORALA05" and tipoCupom!="N"):
    
        print("Cupom Invalido!")
        tipoCupom=str.upper(input("Digite novamente o nome do cupom\n--> "))

    if(tipoCupom == "BORALA10" ):
        print("Cupom selecionado: BORALA10")
        descontoCupom = valorTotal * 0.10
    
    elif(tipoCupom == "BORALA05"):
        print("Cupom selecionado: BORALA05")
        descontoCupom = valorTotal * 0.05
    
    elif(tipoCupom == "N"):
        print("Nenhum Cupom Foi Selecionado!")
    else:
        print("ERRO")


elif(cupom == "N"):
    print("Nenhum Cupom Foi Selecionado!")

print(descontoCupom)