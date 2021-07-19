nomeAluno = []
matricula = []
serie = []
qtdInscrito = []
cadastrado = False

inscHistoria = 0        #2a e 3a série
arrHistoria = []

inscTeatro = 0          #3a e 4a série
arrTeatro = []

inscLingSinais = 0      #Todos
arrLingSinais = []

inscExpArtist = 0       #4a e 5a série
arrExpArtist = []

inscSoletrando = 0      #5a série
arrSoletrando = []

inscLeitDinamica4a = 0  #4a série
arrLeitDinamica4a = []

inscCorpoFala = 0       #3a série
arrCorpoFala = []

inscMundoImag = 0       #2a série
arrMundoImag = []

inscLeitDinamica5a = 0  #5a série
arrLeitDinamica5a = []

inscCriandoEmoji = 0    #2a série
arrCriandoEmoji = []

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
        
        elif(menu == 2):
                rm = int(input("Digite o RM do aluno \n---> "))
                while(rm not in matricula):
                        print("Aluno  não  cadastrado. Favor procurar a coordenação do Fundamental I")
                        rm = int(input("Digite o RM do aluno \n---> "))
                serieAtual = serie[matricula.index(rm)]
                print(serieAtual)

                
                hist = "1 - Criar e contar histórias(Vagas disponiveis: {})".format(10-inscHistoria)
                sinais = "2 - A língua de sinais (Vagas disponiveis: {})".format(10-inscLingSinais)
                mundo = "3 - O mundo da imaginação (Vagas disponiveis: {})".format(10-inscMundoImag)
                emoji = "4 - Criando e recriando com emojis (Vagas disponiveis: {})".format(10-inscCriandoEmoji)

                if(inscHistoria == 10):
                        hist = "1 - INDISPONIVEL"
                if(inscLingSinais == 10):
                        sinais = "2 - INDISPONIVEL"
                if(inscMundoImag == 10):
                        mundo = "3 - INDISPONIVEL"
                if(inscCriandoEmoji == 10):
                        emoji = "4 - INDISPONIVEL"
                
                if(serieAtual == 2):
                        print("Escolha um evento \n{} \n{} \n{} \n{}".format(hist, sinais, mundo, emoji))
                        seleciona = int(input("---> "))

                        if(seleciona == 1 and rm not in arrHistoria):
                                inscHistoria += 1
                                arrHistoria.append(rm)
                                print("ALUNO CADASTRADO")
                        elif(seleciona == 2):
                                inscLingSinais += 1
                        elif(seleciona == 3):
                                inscMundoImag += 1
                        elif(seleciona == 4):
                                inscCriandoEmoji += 1
                        elif(rm in arrHistoria):
                                print("ALUNO JA FOI CADASTRADO")




                        

print(nomeAluno)
print(matricula)
print(serie)