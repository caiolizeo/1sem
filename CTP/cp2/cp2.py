#   INICIO - Variaveis
descontoQtdPratos = float(0)
descontoValor500 = float(0)
descontoCupom = float(0)
descontoPVez = float(0)
nPessoas = int(1)


#   QUANTIDADE DE PRATOS
qtdPratos=int(input("Digite a quantidade de pratos principais\n--> "))
while(qtdPratos <= 0):
    qtdPratos=int(input("Número de pratos principais inválido. Digite novamente\n--> "))

#   VALOR TOTAL DA NOTA
valorTotal=float(input("Digite o valor Total \n--> "))
while(valorTotal <= 0):
    valorTotal=float(input("Valor inválido. Digite novamente\n--> "))

#   PRIMEIRA VEZ DO CLIENTE?
pVez=str.upper(input("É a primeira vez que o cliente visita o restaurante?\nS = SIM | N = NÃO\n--> "))
while(pVez != "S" and pVez != "N"):
    print("Opção inválida!")
    pVez=str.upper(input("Digite novamente\nS = SIM | N = NÃO\n--> "))  

#   INICIO - VALIDAÇÃO CUPOM
cupom=str.upper(input("O Cliente possui cupom válido?\nS = SIM | N = NÃO\n--> "))
 
while(cupom != "S" and cupom != "N"):
    print("Opção inválida!")
    cupom=str.upper(input("Digite novamente\nS = SIM | N = NÃO\n--> "))

if(cupom == "S"):

    tipoCupom=str.upper(input("Digite o nome do cupom\n--> "))

    while(tipoCupom != "BORALA10" and tipoCupom != "BORALA05"):
    
        print("Cupom Inválido!")
        cupom=str.upper(input("O Cliente possui cupom válido?\nS = SIM | N = NÃO\n--> "))

        while(cupom != "S" and cupom != "N"):
            print("Opção inválida!")
            cupom=str.upper(input("Digite novamente\nS = SIM | N = NÃO\n--> "))

        if(cupom == "S"):
            tipoCupom=str.upper(input("Digite o nome do cupom\n--> "))

        elif(cupom == "N"):
            print("Nenhum Cupom Foi Selecionado!")
            break
            
    if(tipoCupom == "BORALA10" ):
        print("Cupom selecionado: BORALA10")
        descontoCupom = valorTotal * 0.10
    
    elif(tipoCupom == "BORALA05"):
        print("Cupom selecionado: BORALA05")
        descontoCupom = valorTotal * 0.05
    
elif(cupom == "N"):
    print("Nenhum Cupom Foi Selecionado!")


#   VALIDAÇÃO NUMERO DE PESSOAS

nPessoas=int(input("Quantas pessoas vão pagar? \n--> "))
while(nPessoas <= 0 ):
    print("Opção invalida!")
    nPessoas=int(input("Quantas pessoas vão pagar? \n--> "))


#   VALIDAÇÃO QUANTIDADE DE PRATOS  
if(qtdPratos > 3):
    descontoQtdPratos = valorTotal * 0.04

#   VALIDAÇÃO VALOR DA NOTA  
if(valorTotal > 500.0):
    descontoValor500 = valorTotal * 0.06

#   VALIDAÇÃO PRIMEIRA VEZ
if(pVez == "S"):
    descontoPVez = valorTotal * 0.05


#   CALCULOS

totalDesconto = descontoQtdPratos + descontoValor500 + descontoCupom + descontoPVez

valorDesconto = valorTotal - totalDesconto 

valorDividido = valorDesconto / nPessoas


#   SAIDA DE DADOS
print("")
print("-"*25)
print("Valor total da nota fiscal: {:.2f} \nValor total da nota com desconto: {:.2f}\n".format(valorTotal, valorDesconto))

print("\nNúmero de pessoas: {} \nTotal por pessoa: {:.2f}".format(nPessoas, valorDividido))
print("-"*25)

