nomeAluno = []
matricula = []
serie = []
qtdInscrito = []

cadastrado = False

vagas = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
arrHistoria = []       #2a e 3a série
arrTeatro = []         #3a e 4a série
arrLingSinais = []     #Todos
arrExpArtist = []      #4a e 5a série  
arrSoletrando = []     #5a série
arrLeitDinamica4a = [] #4a série     
arrCorpoFala = []      #3a série  
arrMundoImag = []      #2a série
arrLeitDinamica5a = [] #5a série
arrCriandoEmoji = []   #2a série


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

                hist = "1 - Criar e contar histórias(Vagas disponiveis: {})".format(10-vagas[0])
                sinais = "2 - A língua de sinais (Vagas disponiveis: {})".format(10-vagas[2])
                mundo = "3 - O mundo da imaginação (Vagas disponiveis: {})".format(10-vagas[7])
                emoji = "4 - Criando e recriando com emojis (Vagas disponiveis: {})".format(10-vagas[9])

                if(vagas[0] == 10):
                        hist = "*** INDISPONIVEL ***"
                if(vagas[1] == 10):
                        hist = "*** INDISPONIVEL ***"
                if(vagas[2] == 10):
                        sinais = "*** INDISPONIVEL ***"
                if(vagas[7] == 10):
                        mundo = "*** INDISPONIVEL ***"
                if(vagas[9] == 10):
                        emoji = "*** INDISPONIVEL ***"
                
                if(serieAtual == 2):
                        print("Escolha um evento \n{} \n{} \n{} \n{}".format(hist, sinais, mundo, emoji))
                        seleciona = int(input("---> "))

                        cadastrou = False
                        if(qtdInscrito[matricula.index(rm)] < 3):
                                print(qtdInscrito[matricula.index(rm)])
                                if(seleciona == 1 and rm not in arrHistoria and vagas[0] < 10):
                                        valor = vagas[0] + 1
                                        vagas[0] = valor
                                        arrHistoria.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 2 and rm not in arrLingSinais):
                                        valor = vagas[2] + 1
                                        vagas[2] = valor
                                        arrLingSinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 3 and rm not in arrMundoImag):
                                        valor = vagas[7] + 1
                                        vagas[7] = valor
                                        arrMundoImag.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(seleciona == 4 and rm not in arrCriandoEmoji):
                                        valor = vagas[9] + 1
                                        vagas[9] = valor
                                        arrCriandoEmoji.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrou = True
                                elif(rm in arrHistoria or rm in arrLingSinais or rm in arrMundoImag or rm in arrMundoImag):
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrou):
                                        valor = qtdInscrito[matricula.index(rm)] + 1
                                        qtdInscrito[matricula.index(rm)] = valor
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
                
                if(serieAtual == 3):
                         print("Escolha um evento \n{} \n{} \n{} \n{}".format(hist, sinais, mundo, emoji))
                         seleciona = int(input("---> "))


        elif(menu == 4):
                break



                        

print(nomeAluno)
print(matricula)
print(serie)
print(qtdInscrito)