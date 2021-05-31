
qtdOtimo = 0
qtdRuim = 0
mediaRuim = 0
porcPessimo = 0
idadePessimo = 0
bomRegular = 0
numeroTeste = 1
totalSpecs = 10

for n in range(1, totalSpecs+1 ):
    resposta = str.upper(input("Pessoa {} Digite sua nota: ".format(numeroTeste)))
    while(resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D" and resposta != "E"):
        resposta = str.upper(input("Nota inválida, digite novamente \n--> "))
    
    idade = int(input("Digite sua idade: "))
    while(idade < 0):
        idade = int(input("Idade inválida, digite novamente \n--> "))
    print("")

    if(resposta == "A"):
        qtdOtimo+=1
    if(resposta == "B" or resposta == "C"):
        bomRegular+=1
    if(resposta == "D"):
        qtdRuim+=1
        mediaRuim+=idade
    if(resposta == "E"):
        porcPessimo+=1
        if(idade > idadePessimo):
            idadePessimo = idade

    numeroTeste+=1



print("Quantida de respostas ótimo: {}".format(qtdOtimo))

if(qtdRuim == 0 or mediaRuim == 0):
    print("Ninguém respondeu Ruim")
elif(qtdRuim != 0 or mediaRuim != 0):
    print("Média de idade das pessoas que responderam Ruim:",(mediaRuim/qtdRuim))

if(porcPessimo == 0):
    print("Ninguém respondeu péssimo")
elif(porcPessimo != 0):
    print("{}% Respondeu péssimo, amaior idade de quem utilizou essa opção foi {} anos".format(round((porcPessimo/totalSpecs)*100), idadePessimo))

print("Quantidade de pessoas que responderam Bom ou Regular: {}".format(bomRegular))




'''
Um cinema possui capacidade de 100 lugares e está sempre com ocupação 
total. Certo dia, cada espectador respondeu a um questionário, no qual constava 
sua idade e sua opinião em relação ao filme, segundo as seguintes notas:
Notas:
A - Ótimo
B – Bom
C – Regular
D – Ruim
E - Péssimo
Elabore um algoritmo que, lendo esses dados, calcule e imprima:
- a quantidade de respostas Ótimo;
- a média de idade das pessoas que responderam Ruim;
- quantos % responderam Péssimo e a maior idade que utilizou essa opção;
- a quantidade de respostas Bom e Regular (juntos).
'''