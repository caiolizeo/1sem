nome=input("Digite o seu nome:")
salario=float(input("Digite o seu salário fixo: "))

vendido_fem=float(input("Digite o valor vendido no setor feminino: "))
vendido_masc=float(input("Digite o valor vendido no setor masculino: "))
vendido_inf=float(input("Digite o valor vendido no setor infantil: "))
vendido_bel=float(input("Digite o valor vendido no setor de beleza: "))


bonus_feminino=(vendido_fem/100)*2
bonus_masculino=(vendido_masc/100)*2
bonus_infantil=(vendido_inf/100)*4
bonus_beleza=(vendido_bel/100)*6

comissao=round(bonus_feminino+bonus_masculino+bonus_infantil+bonus_beleza, 2)

total=round(salario+comissao, 2)
print("")
print("Prezado(a) "+nome+",")
print("Seu salário fixo é de",salario,"reais e sua comissão referente o mês vigente foi calculado em",comissao,"reais.")
print("Total a receber:",total,"reais.")
print("")