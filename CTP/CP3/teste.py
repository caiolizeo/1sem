nomeAluno = ["João", "Maria", "Marcos", "Zico", "Antonio"]
numMatricula = [111, 222, 333, 444, 555]
serie = [2, 3, 4, 2, 5]
qtdInscrito = [0, 0, 0, 0, 0]

cadastrado = False

vagas = [0]*10

arrSinais = [111, 222, 555, 333, 444]          #1
arrEmoji = [111, 333, 444, 555]           #2
arrHist = [333, 444, 555]            #3
arrExpArt = [222, 555]          #4
arrLeitDin = [333, 555]         #5
arrLeitDram = [111,333]        #6
arrCorpoFala = [222, 333]       #7
arrMundo = [111]           #8
arrSoletr = []          #9
arrTeatro = []          #10


oficinas = (arrHist, arrTeatro, arrSinais)




def listaOficina():
       
        of1 = ("A língua de sinais - 4ª. feira - Matutino", arrSinais)
        of2 = ("Criando e recriando com emojis - 6ª. feira - Vespertino", arrEmoji)
        of3 = ("Criar e contar histórias - 2ª. feira - Matutino", arrHist)
        of4 = ("Expressão Artística - 5ª. feira - Matutino", arrExpArt)
        of5 = ("Leitura dinâmica - 5ª. feira - Vespertino", arrLeitDin)
        of6 = ("Leitura dramática - 2ª. feira - Vespertino",arrLeitDram)
        of7 = ("O corpo fala - 3ª. feira - Vespertino", arrCorpoFala)
        of8 = ("O mundo da imaginação - 4ª. feira - Vespertino", arrMundo)
        of9 = ("Soletrando - 6ª. feira - Matutino", arrSoletr)
        of10 = ("Teatro: Luz, Câmera e Ação - 3ª. feira – Matutino", arrTeatro)
        
        oficinas = [of1, of2, of3, of4, of5, of6, of7, of8, of9, of10]

        return oficinas       


def imprimeOficinas(oficinas):
        cont = 0
        for x in range(len(oficinas)):
                ofAtual = oficinas[cont]
                alunos = ofAtual[1]
                contAlunos = 0
                print(ofAtual[0])
                for x in range(len(alunos)):
                        rm = alunos[contAlunos]
                        nomeAtual = nomeAluno[contAlunos]
                        serieAtual = serie[contAlunos]
                        print("RM: {} - {} - {}ª. série".format(rm, nomeAtual, serieAtual))
                        contAlunos += 1
                if(len(alunos) > 1):
                        print("\nTotal: {} alunos".format(len(alunos)))
                elif(len(alunos) == 1):
                        print("\nTotal: {} aluno".format(len(alunos)))
                else:
                        print("Nenhum aluno cadastrado")
                print("\n"+"-"*60+"\n")
                cont += 1


imprimeOficinas(listaOficina())











def formataAluno(nome, numMatricula, serieAluno):
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
        cont = 0
        cadastro = []
        for x in range(len(nome)):
            list = (nomeAluno[cont], numMatricula[cont], serie[cont])
            cadastro.append(list)  
            cont+=1 
        cadastroOrdenado = sorted(cadastro)
        return cadastroOrdenado


def listaAluno(tuplaAlunos):
        cont = 0
        for x in range(len(tuplaAlunos)):
                tupla = tuplaAlunos[cont]
                print(formataAluno(tupla[0], tupla[1], tupla[2]))
                cont+=1


#listaAluno(ordenaLista(nomeAluno))
