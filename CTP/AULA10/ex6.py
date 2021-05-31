idade = 0
numero = 1
qtde = 50

while(numero <= qtde):
    idadeAtual = int(input("Digite a idade da {}a pessoa \n--> ".format(numero)))
    while(idadeAtual < 0):
        idadeAtual = int(input("Idade da {}a pessoa inválida, digite novamente \n--> ".format(numero)))
    idade = idade + idadeAtual
    numero+=1

media = idade/qtde

print("Média de idades: {}".format(media))



'''
Faça um programa em Python que leia 50 idades e mostre na tela a media simples das 
idades digitadas. Observações: - Não aceitar idade < 0 - Necessariamente precisa ter 50 
idades válidas
'''