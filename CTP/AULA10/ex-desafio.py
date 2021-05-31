numero = 1
notaPar = 0
notaImp = 0

print("INICIANDO ALUNOS ÍMPARES \n")

while(numero%2 != 0):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    notaAtual = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} \n--> ".format(numero)))
    print("-"*25)
    while (notaAtual < 0 or notaAtual > 10):
        print("*"*3,"NOTA INVÁLIDA","*"*3)
        notaAtual = float(input("INSIRA NOVAMENTE A NOTA DO ALUNO NÚMERO {} \n--> ".format(numero)))
        print("-"*25)
    notaImp = notaImp + notaAtual
    numero+=2
    if(numero == 51):
        numero = 2
        break

print("\n INICIANDO ALUNOS PARES \n")

while(numero%2 == 0):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notaAtual = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} \n--> ".format(numero)))
    print("-"*25)
    while (notaAtual < 0 or notaAtual > 10):
        print("*"*3,"NOTA INVÁLIDA","*"*3)
        notaAtual = float(input("INSIRA NOVAMENTE A NOTA DO ALUNO NÚMERO {} \n--> ".format(numero)))
        print("-"*25)
    notaPar = notaPar + notaAtual
    numero+=2
    if(numero == 52):
        break

mediaImp = round(notaImp/25, 2)
mediaPar = round(notaPar/25, 2)

print("MÉDIA DOS ALUNOS ÍMPARES: {}".format(mediaImp))
print("MÉDIA DOS ALUNOS PARES: {} \n".format(mediaPar))

if(mediaImp > mediaPar):
    print("OS ALUNOS ÍMPARES TIVERAM A MAIOR NOTA")
elif(mediaPar > mediaImp):
    print("OS ALUNOS PARES TIVERAM A MAIOR NOTA")
else:
    print("AS DUAS TURMAS TIVERAM A MESMA MÉDIA")