#Arrays dos alunos
nomeAluno = []
matricula = []
serie = []
qtdInscrito = []

#Arrays das oficinas
arrSinais = []          #1
arrEmoji = []           #2
arrHist = []            #3
arrExpArt = []          #4
arrLeitDin = []         #5
arrLeitDram = []        #6
arrCorpoFala = []       #7
arrMundo = []           #8
arrSoletr = []          #9
arrTeatro = []          #10

vagas = [0]*10

'''
Posicoes:
3 - 0 Historia - 2a e 3a série
1 Teatro - 3a e 4a série
1 - 2 Lingua de Sinais - Todos
3 Expressao Artistica - 4a e 5a série
4 Soletrando - 5a série
5 Leitura Dinamica - 4a série
6 O Corpo Fala - 3a série
7 O Mundo da Imaginacao - 2a série
8 Leitura Dinamica - 5a série
2 - 9 Criando Emojis - 2a série
'''

cadastrou = False
finalizou = False

def formataAluno(nome, numMatricula, serieAluno):
        inscricoes  = []
        if(numMatricula in arrHist):
                inscricoes.append("Criar e contar histórias - 2ª. feira - Matutino")
        if(numMatricula in arrTeatro):
                inscricoes.append("Teatro: Luz, Câmera e Ação - 3ª. feira – Matutino")
        if(numMatricula in arrSinais):
                inscricoes.append("A língua de sinais - 4ª. feira - Matutino")
        if(numMatricula in arrExpArt):
                inscricoes.append("Expressão Artística - 5ª. feira - Matutino")
        if(numMatricula in arrSoletr):
                inscricoes.append("Soletrando - 6ª. feira - Matutino")
        if(numMatricula in arrLeitDram):
                inscricoes.append("Leitura dramática - 2ª. feira - Vespertino")
        if(numMatricula in arrCorpoFala):
                inscricoes.append("O corpo fala - 3ª. feira - Vespertino")
        if(numMatricula in arrMundo):
                inscricoes.append("O mundo da imaginação - 4ª. feira - Vespertino")
        if(numMatricula in arrLeitDin):
                inscricoes.append("Leitura dinâmica - 5ª. feira - Vespertino")
        if(numMatricula in arrEmoji):
                inscricoes.append("Criando e recriando com emojis - 6ª. feira - Vespertino")

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
            list = (nomeAluno[cont], matricula[cont], serie[cont])
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


menu = int(input("Menu de opções \n\n1 - Realizar cadastro \n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
while(menu != 0):
        if(finalizou == True):
               menu = int(input("Menu de opções \n\n1 - *** INDISPONÍVEL ***\n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
        if(menu == 1 and finalizou == True):
                print("*** OS CADASTROS JA FORAM REALIZADOS ***")
        if(menu == 1 and finalizou == False):
                finalizou = True
                rm = 1
                while(rm != 0):
                        print("*"*10)
                        print("NOVO ALUNO")
                        print("*"*10)
                        rm = int(input("Digite o RM do aluno \n---> "))
                        if(rm != 0):
                                while(rm in matricula):
                                        print("RM DUPLICADO!")
                                        rm = int(input("Digite o RM do aluno \n---> "))
                                matricula.append(rm)
                                nome = str(input("Digite o nome do aluno \n---> "))
                                nomeAluno.append(nome)
                                serieAtual = int(input("Digite a série do aluno \n---> "))
                                while(serieAtual < 2 or serieAtual > 5):
                                        print("Só são permitidos alunos da 2ª à 5ª série")
                                        serieAtual = int(input("Digite a série do aluno \n---> "))
                                serie.append(serieAtual)
                                qtdInscrito.append(0)
                        
        elif(menu == 2):
                rm = int(input("Digite o RM do aluno \n---> "))
                while(rm not in matricula):
                        print("Aluno  não  cadastrado. Favor procurar a coordenação do Fundamental I")
                        rm = int(input("Digite o RM do aluno \n---> "))
                serieAtual = serie[matricula.index(rm)]

                hist = "Criar e contar histórias (Vagas disponíveis: {})".format(10-vagas[0])
                teatro = "Teatro: Luz, Câmera e Ação (Vagas disponíveis: {})".format(10-vagas[1])
                sinais = "A língua de sinais (Vagas disponíveis: {})".format(10-vagas[2])
                expArt = "Expressão Artística (Vagas disponíveis: {})".format(10-vagas[3])
                soletr = "Soletrando (Vagas disponíveis: {})".format(10-vagas[4])
                leitDram = "Leitura dramática - 4ª série (Vagas disponíveis: {})".format(10-vagas[5])
                corpoFala = "O corpo Fala (Vagas disponíveis: {})".format(10-vagas[6])
                mundo = "O mundo da imaginação (Vagas disponíveis: {})".format(10-vagas[7])
                leitDin5a = "Leitura dinâmica - 5ª série (Vagas disponíveis: {})".format(10-vagas[8])
                emoji = "Criando e recriando com emojis (Vagas disponíveis: {})".format(10-vagas[9])

                if(vagas[0] == 10):
                        hist = "*** INDISPONIVEL ***"
                if(vagas[1] == 10):
                        teatro = "*** INDISPONIVEL ***"
                if(vagas[2] == 10):
                        sinais = "*** INDISPONIVEL ***"
                if(vagas[3] == 10):
                        expArt = "*** INDISPONIVEL ***"
                if(vagas[4] == 10):
                        soletr = "*** INDISPONIVEL ***"
                if(vagas[5] == 10):
                        leitDram = "*** INDISPONIVEL ***"
                if(vagas[6] == 10):
                        corpoFala = "*** INDISPONIVEL ***"
                if(vagas[7] == 10):
                        mundo = "*** INDISPONIVEL ***"
                if(vagas[8] == 10):
                        leitDin5a = "*** INDISPONIVEL ***"
                if(vagas[9] == 10):
                        emoji = "*** INDISPONIVEL ***"
                
                if(serieAtual == 2):
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, sinais, mundo, emoji))
                        seleciona = int(input("---> "))

                        if(qtdInscrito[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in arrHist and vagas[0] < 10):
                                        valor = vagas[0] + 1
                                        vagas[0] = valor
                                        arrHist.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 2 and rm not in arrSinais and vagas[2] < 10):
                                        valor = vagas[2] + 1
                                        vagas[2] = valor
                                        arrSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 3 and rm not in arrMundo and vagas[7] < 10):
                                        valor = vagas[7] + 1
                                        vagas[7] = valor
                                        arrMundo.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 4 and rm not in arrEmoji and vagas[9] < 10):
                                        valor = vagas[9] + 1
                                        vagas[9] = valor
                                        arrEmoji.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrou):
                                        valor = qtdInscrito[matricula.index(rm)] + 1
                                        qtdInscrito[matricula.index(rm)] = valor
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
                
                if(serieAtual == 3):
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, teatro, sinais,corpoFala))
                        seleciona = int(input("---> "))

                        if(qtdInscrito[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in arrHist and vagas[0] < 10):
                                        valor = vagas[0] + 1
                                        vagas[0] = valor
                                        arrHist.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 2 and rm not in arrTeatro and vagas[1] < 10):
                                        valor = vagas[1] + 1
                                        vagas[1] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 3 and rm not in arrSinais and vagas[2] < 10):
                                        valor = vagas[2] + 1
                                        vagas[2] = valor
                                        arrSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 4 and rm not in arrCorpoFala and valor[6] < 10):
                                        valor = vagas[6] + 1
                                        vagas[6] = valor
                                        arrCorpoFala.append(rm)
                                        print("ALUNO CADASTRO")
                                        cadastrou = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrou):
                                        valor = qtdInscrito[matricula.index(rm)] + 1
                                        qtdInscrito[matricula.index(rm)] = valor
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")

                if(serieAtual == 4):
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(teatro, sinais, expArt, leitDram))
                        seleciona = int(input("---> "))

                        if(qtdInscrito[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in arrTeatro and vagas[1] < 10):
                                        valor = vagas[1] + 1
                                        vagas[1] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 2 and rm not in arrSinais and vagas[2] < 10):
                                        valor = vagas[2] + 1
                                        vagas[2] = valor
                                        arrSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 3 and rm not in arrExpArt and vagas[3] < 10):
                                        valor = vagas[3] + 1
                                        vagas[3] = valor
                                        arrSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 4 and rm not in arrLeitDram and vagas[5] < 10):
                                        valor = vagas[5] + 1
                                        vagas[5] = valor
                                        arrSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrou):
                                        valor = qtdInscrito[matricula.index(rm)] + 1
                                        qtdInscrito[matricula.index(rm)] = valor
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
                
                if(serieAtual == 5):
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(sinais, expArt, soletr, leitDin5a))
                        seleciona = int(input("---> "))
                        if(qtdInscrito[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in arrSinais and vagas[2] < 10):
                                        valor = vagas[2] + 1
                                        vagas[2] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 2 and rm not in arrExpArt and vagas[3] < 10):
                                        valor = vagas[3] + 1
                                        vagas[3] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 3 and rm not in arrSoletr and vagas[4] < 10):
                                        valor = vagas[4] + 1
                                        vagas[4] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 4 and rm not in arrLeitDin and vagas[8] < 10):
                                        valor = vagas[8] + 1
                                        vagas[8] = valor
                                        arrTeatro.append(rm)
                                        print("ALUNO CADASTRADO") 
                                        cadastrou = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrou):
                                        valor = qtdInscrito[matricula.index(rm)] + 1
                                        qtdInscrito[matricula.index(rm)] = valor
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
        elif(menu == 3):
                print("Listar inscrições \n1 - Listar por aluno (ordem alfabética de nome) \n2 - Listar por oficina (ordem alfabética)")
                opcao = int(input("---> "))
                while(opcao < 1 or opcao > 2):
                        opcao = int(input("Opção inválida, digite novamente. \n---> "))
                if(opcao == 1):
                       print("\n***** Alunos inscritos – Ordem: Alfabética (nome) *****\n")
                       listaAluno(ordenaLista(nomeAluno))
                
        elif(menu == 4):
                break

print(nomeAluno)
print(matricula)
print(serie)
print(qtdInscrito)
print(vagas)