boleto=float(input("valor do boleto: "))
juros=float(input("percentual de juros: "))
dias=int(input("dias em atraso: "))

novo_valor=boleto+(boleto*(juros/100))*dias

print("Novo valor: ", novo_valor)