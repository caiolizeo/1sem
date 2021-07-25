nomeAluno = ["João", "Maria", "Marcos", "Zico", "Antonio"]
numMatricula = [111, 222, 333, 444, 555]
serie = [2, 3, 4, 2, 5]
qtdInscrito = [0, 0, 0, 0, 0]

cadastrado = False

vagas = [0]*10

arrHist = [111, 222, 333]           
arrTeatro = [111, 333, 555]          
arrSinais = [111, 444, 555] 

oficinas = (arrHist, arrTeatro, arrSinais)


def listaAluno(nome, numMatricula, serieAluno):
    inscricoes  = []
    if(numMatricula in arrHist):
            inscricoes.append("Criar e contar histórias - 2ª. feira - Matutino")
    if(numMatricula in arrTeatro):
            inscricoes.append("Teatro: Luz, Câmera e Ação - 3ª. feira – Matutino")
    if(numMatricula in arrSinais):
            inscricoes.append("A língua de sinais - 4ª. feira - Matutino")

    if(len(inscricoes) == 3):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0], inscricoes[1], inscricoes[2])
    elif(len(inscricoes) == 2):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0], inscricoes[1])
    elif(len(inscricoes) == 1):
            aluno = (numMatricula, nome, serieAluno, inscricoes[0])

    if(len(aluno) == 6):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
    elif(len(aluno) == 5):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4])
    elif(len(aluno) == 4):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3])

    return x


def ordenaLista(nome):
        qtdAlunos = len(nome)
        cont = 0
        cadastro = []
        while(cont < qtdAlunos):
            list = (nomeAluno[cont], numMatricula[cont], serie[cont])
            cadastro.append(list)  
            cont+=1 
        cadastroOrdenado = sorted(cadastro)
        return cadastroOrdenado


#x = ordenaLista(nomeAluno)
#tupla = x[0]



#print(listaAluno(tupla[0], tupla[1],tupla[2]))

'''
def imprimeLista(nome):
    qtdAlunos = len(nome)
    cont = 0
    while(cont < qtdAlunos):
        list = listaAluno(numMatricula[cont], nomeAluno[cont], serie[cont])
        print(list)
        cont+=1
'''

'''
aluno = (nomeAluno[0], matricula[0], serie[0], qtdInscrito[0])
aluno2 = (nomeAluno[1], matricula[1], serie[1], qtdInscrito[1])
print(aluno)
print(aluno2)


print(matricula)
print(serie)
print(qtdInscrito)
'''


