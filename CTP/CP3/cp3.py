nomeAluno = []
matricula = []
serie = []
qtdInscrito = []

cadastrado = False

vagas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
Posicoes:
0 Historia - 2a e 3a série
1 Teatro - 3a e 4a série
2 Lingua de Sinais - Todos
3 Expressao Artistica - 4a e 5a série
4 Soletrando - 5a série
5 Leitura Dinamica - 4a série
6 O Corpo Fala - 3a série
7 O Mundo da Imaginacao - 2a série
8 Leitura Dinamica - 5a série
9 Criando Emojis - 2a série
'''
arrHist = []       #2a e 3a série
arrTeatro = []         #3a e 4a série
arrSinais = []     #Todos
arrExpArt = []      #4a e 5a série  
arrSoletr = []     #5a série
arrLeitDin4a = [] #4a série     
arrCorpoFala = []      #3a série  
arrMundo = []      #2a série
arrLeitDin5a = [] #5a série
arrEmoji = []   #2a série

menu = int(input("Menu de opções \n\n1 - Realizar cadastro \n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
while(menu != 0):
        if(cadastrado == True):
               menu = int(input("Menu de opções \n\n1 - *** INDISPONÍVEL ***\n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
        if(menu == 1 and cadastrado == False):
                cadastrado = True
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
                leitDin4a = "Leitura dinâmica - 4ª série (Vagas disponíveis: {})".format(10-vagas[5])
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
                        leitDin4a = "*** INDISPONIVEL ***"
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

                        cadastrou = False
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

                        cadastrou = False
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



        elif(menu == 4):
                break



                        

print(nomeAluno)
print(matricula)
print(serie)
print(qtdInscrito)