nomeAluno = ["João", "Maria", "Marcos", "Zico", "Antonio"]
numMatricula = [111, 222, 333, 559, 668]
serie = [2, 2, 2]
qtdInscrito = [0, 0, 0]

cadastrado = False

vagas = [0]*10

arrHist = [111, 559, 668]            #2a e 3a série
arrTeatro = [111, 354, 475]          #3a e 4a série
arrSinais = [111, 559, 668] 

oficinas = (arrHist, arrTeatro, arrSinais)


def verificaInscricao(numMatricula, nome, serieAluno):
        
        inscricoes  = []
        if(numMatricula in arrHist):
                inscricoes.append("Criar e contar histórias – 2ª. feira - Matutino")
        if(numMatricula in arrTeatro):
                inscricoes.append("Teatro: Luz, Câmera e Ação – 3ª. feira – Matutino")
        if(numMatricula in arrSinais):
                inscricoes.append("A língua de sinais – 4ª. feira - Matutino")

    

        if(len(inscricoes) == 3):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0], inscricoes[1], inscricoes[2])
        elif(len(inscricoes) == 2):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0], inscricoes[1])
        elif(len(inscricoes) == 1):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0])
        

        return aluno


aluno = verificaInscricao(numMatricula[0], nomeAluno[0], serie[0])

print(len(aluno))
'''
aluno = (nomeAluno[0], matricula[0], serie[0], qtdInscrito[0])
aluno2 = (nomeAluno[1], matricula[1], serie[1], qtdInscrito[1])
print(aluno)
print(aluno2)


print(matricula)
print(serie)
print(qtdInscrito)
'''


