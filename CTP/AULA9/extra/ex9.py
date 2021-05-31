produto = float(input("Digite o valor do produto: R$"))

if(produto < 20):
    print("O lucro será de 45%, o valor de venda do produto é de: R${}".format(produto*0.45 + produto))
elif(produto >= 20):
    print("O lucro será de 30%, o valor de venda do produto é de: R${}".format(produto*0.30 + produto))