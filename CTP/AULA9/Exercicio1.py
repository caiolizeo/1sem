print("-"*25)
laboratorio = float(input("Digie a nota do trabalho de laboratório:"))
if(laboratorio >=0 and laboratorio <=10):
    print("-"*25)
    aval_semestral = float(input("Digite a nota da avaliação semestral:"))
    if(aval_semestral >= 0 and aval_semestral <= 10):
        print("-"*25)
        exame_final = float(input("Digite a nota do exame final:"))
        if(exame_final >=0 and exame_final <= 10):

            
            media = round(laboratorio*0.2+aval_semestral*0.3+exame_final*0.5, 2)

            print("-"*25)
            if(media >= 0 and media <= 4.9):
                print("Média ponderada:",media,"- Conceito E")
            elif(media >= 5 and media <= 5.9):
                print("Média ponderada:",media,"- Conceito D")
            elif(media >= 6 and media <= 6.9):
                print("Média ponderada:",media,"- Conceito C")
            elif(media >= 7 and media <= 7.9):
                print("Média ponderada:",media,"- Conceito B")
            elif(media >= 8 and media <= 10):
                print("Média ponderada:",media,"- Conceito A")
            print("-"*25)
            print()

        else:
            print("Nota do exame final incorreta")
    else:
        print("Nota da avaliação semestral incorreta")
else:
    print("Nota do trabalho de laboratório incorreta")