nome = str(input("Digite o nome do aluno --> "))
nota1 = float(input("Digite a nota 1 --> "))
nota2 = float(input("Digite a nota 2 --> "))
nota3 = float(input("Digite a nota 3 --> "))
faltas = float(input("Digite a quantidade de faltas do aluno --> "))

media = (nota1+nota2+nota3)/3
aulas = int(80)

if(faltas <= aulas*0.25):
    if(media >=7):
        print("Aluno aprovado!")
    else:
        print("Reprovado por média!")
else:
    print("Reprovado por falta!")