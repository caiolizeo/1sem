salario=float(input("Digite o salario bruto: "))
prestacao=float(input("Digite o valor da prestação: "))
limite = salario*0.3

if(salario and prestacao > 0):
    if(prestacao<=limite):
        print("Empréstimo concedido")
    else:
        print("Empréstimo não pode ser concedido")
    print("Limite:",limite)
else:
    print("Salário e prestação devem ser maior que zero")