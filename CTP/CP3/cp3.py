#Arrays dos alunos
nomeAluno = ["Joao", "Bruno", "Zé", "Carlos", "Ana", "Maria"]
matricula = [123, 321, 444, 459, 555, 487]
serie = [2, 3, 4, 2, 3, 5]
qtdInscrito = [0, 0, 0, 0, 0, 0]

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

cadastrou = True
executando = True

def menuPrincipal1():
    menu = int(input("\nMenu de opções \n\n1 - Realizar cadastro \n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
    return menu

def menuPrincipal2():
    menu = int(input("\nMenu de opções \n\n1 - #### INDISPONÍVEL ####\n2 - Fazer inscrições \n3 - Listar inscrições \n4 - sair \n---> "))
    return menu

#Função para cadastrar os alunos
def cadastraAluno():
    rm = 1
    while(rm != 0):
            print("#"*22)
            print("####              ####")
            print("####  NOVO ALUNO  ####")
            print("####              ####")
            print("#"*22)
            rm = int(input("Digite o RM do aluno \n---> "))
            while(rm in matricula):
                            print("RM DUPLICADO!")
                            rm = int(input("Digite o RM do aluno \n---> "))
                            if(rm == 0):
                                    break
            if(rm != 0):
                    matricula.append(rm)
                    nome = str(input("Digite o nome do aluno \n---> "))
                    nomeAluno.append(nome)
                    serieAtual = int(input("Digite a série do aluno \n---> "))
                    while(serieAtual < 2 or serieAtual > 5):
                            print("Só são permitidos alunos da 2ª à 5ª série")
                            serieAtual = int(input("Digite a série do aluno \n---> "))
                    serie.append(serieAtual)
                    qtdInscrito.append(0)

#Função para realizar inscrições
def fazerInscricoes():
    rm = int(input("Digite o RM do aluno \n---> "))
    while(rm not in matricula and rm != 0):
            print("Aluno  não  cadastrado. Favor procurar a coordenação do Fundamental I")
            rm = int(input("Digite o RM do aluno \n---> "))
    if(rm != 0):      
            serieAtual = serie[matricula.index(rm)]

            hist = "Criar e contar histórias (Vagas disponíveis: {})".format(10-len(arrHist))
            teatro = "Teatro: Luz, Câmera e Ação (Vagas disponíveis: {})".format(10-len(arrTeatro))
            sinais = "A língua de sinais (Vagas disponíveis: {})".format(10-len(arrSinais))
            expArt = "Expressão Artística (Vagas disponíveis: {})".format(10-len(arrExpArt))
            soletr = "Soletrando (Vagas disponíveis: {})".format(10-len(arrSoletr))
            leitDram = "Leitura dramática - 4ª série (Vagas disponíveis: {})".format(10-len(arrLeitDram))
            corpoFala = "O corpo Fala (Vagas disponíveis: {})".format(10-len(arrCorpoFala))
            mundo = "O mundo da imaginação (Vagas disponíveis: {})".format(10-len(arrMundo))
            leitDin = "Leitura dinâmica (Vagas disponíveis: {})".format(10-len(arrLeitDin))
            emoji = "Criando e recriando com emojis (Vagas disponíveis: {})".format(10-len(arrEmoji))

            if(len(arrHist) == 10):
                    hist = "#### INDISPONIVEL ####"
            if(len(arrTeatro) == 10):
                    teatro = "#### INDISPONIVEL ####"
            if(len(arrSinais) == 10):
                    sinais = "#### INDISPONIVEL ####"
            if(len(arrExpArt) == 10):
                    expArt = "#### INDISPONIVEL ####"
            if(len(arrSoletr) == 10):
                    soletr = "#### INDISPONIVEL ####"
            if(len(arrLeitDram) == 10):
                    leitDram = "#### INDISPONIVEL ####"
            if(len(arrCorpoFala) == 10):
                    corpoFala = "#### INDISPONIVEL ####"
            if(len(arrMundo) == 10):
                    mundo = "#### INDISPONIVEL ####"
            if(len(arrLeitDin) == 10):
                    leitDin = "#### INDISPONIVEL ####"
            if(len(arrEmoji) == 10):
                    emoji = "#### INDISPONIVEL ####"
    
            if(serieAtual == 2):
                    cadastrou = False
                    print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, sinais, mundo, emoji))
                    seleciona = int(input("---> "))

                    if(qtdInscrito[matricula.index(rm)] < 3):
                            if(seleciona == 1 and rm not in arrHist and len(arrHist) < 10):
                                    arrHist.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 2 and rm not in arrSinais and len(arrSinais) < 10):
                                    arrSinais.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 3 and rm not in arrMundo and len(arrMundo) < 10):
                                    arrMundo.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 4 and rm not in arrEmoji and len(arrEmoji) < 10):
                                    arrEmoji.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            else:
                                    print("ALUNO JA FOI CADASTRADO")
                            if(cadastrou):
                                    qtdInscrito[matricula.index(rm)] += 1
                    else:
                            print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
            
            if(serieAtual == 3):
                    cadastrou = False
                    print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, teatro, sinais,corpoFala))
                    seleciona = int(input("---> "))

                    if(qtdInscrito[matricula.index(rm)] < 3):
                            if(seleciona == 1 and rm not in arrHist and len(arrHist) < 10):
                                    arrHist.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 2 and rm not in arrTeatro and len(arrTeatro) < 10):
                                    arrTeatro.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 3 and rm not in arrSinais and len(arrSinais) < 10):
                                    arrSinais.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 4 and rm not in arrCorpoFala and len(arrCorpoFala) < 10):
                                    arrCorpoFala.append(rm)
                                    print("ALUNO CADASTRO")
                                    cadastrou = True
                            else:
                                    print("ALUNO JA FOI CADASTRADO")
                            if(cadastrou):
                                    qtdInscrito[matricula.index(rm)] += 1
                    else:
                            print("APENAS TRÊS INSCRIÇÕES POR ALUNO")

            if(serieAtual == 4):
                    cadastrou = False
                    print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(teatro, sinais, expArt, leitDram))
                    seleciona = int(input("---> "))

                    if(qtdInscrito[matricula.index(rm)] < 3):
                            if(seleciona == 1 and rm not in arrTeatro and len(arrTeatro) < 10):
                                    arrTeatro.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 2 and rm not in arrSinais and len(arrSinais) < 10):
                                    arrSinais.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 3 and rm not in arrExpArt and len(arrExpArt) < 10):
                                    arrExpArt.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 4 and rm not in arrLeitDram and len(arrLeitDram) < 10):
                                    arrLeitDram.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            else:
                                    print("ALUNO JA FOI CADASTRADO")
                            if(cadastrou):
                                    qtdInscrito[matricula.index(rm)] += 1
                    else:
                            print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
            
            if(serieAtual == 5):
                    cadastrou = False
                    print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(sinais, expArt, soletr, leitDin))
                    seleciona = int(input("---> "))
                    if(qtdInscrito[matricula.index(rm)] < 3):
                            if(seleciona == 1 and rm not in arrSinais and len(arrSinais) < 10):
                                    arrSinais.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 2 and rm not in arrExpArt and len(arrExpArt) < 10):
                                    arrExpArt.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 3 and rm not in arrSoletr and len(arrSoletr) < 10):
                                    arrSoletr.append(rm)
                                    print("ALUNO CADASTRADO")
                                    cadastrou = True
                            elif(seleciona == 4 and rm not in arrLeitDin and len(arrLeitDin) < 10):
                                    arrLeitDin.append(rm)
                                    print("ALUNO CADASTRADO") 
                                    cadastrou = True
                            else:
                                    print("ALUNO JA FOI CADASTRADO")
                            if(cadastrou):
                                    qtdInscrito[matricula.index(rm)] += 1
                    else:
                            print("APENAS TRÊS INSCRIÇÕES POR ALUNO")

#Funções da lista por aluno
def formataAluno(nome, numMatricula, serieAluno):
    inscricoes  = []
    aluno = ()
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
    elif(len(inscricoes) == 0):
            aluno = (numMatricula, nome, serieAluno)


    if(len(aluno) == 6):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
    elif(len(aluno) == 5):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4])
    elif(len(aluno) == 4):
            x = "RM: {} - {} - {}ª. série \nOficinas: \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3])
    elif(len(aluno) == 3):
            x = "RM: {} - {} - {}ª. série \nO aluno não está cadastrado em nenhuma oficina\n".format(aluno[0], aluno[1], aluno[2])
    return x

def listaOrdenada(nome):
    cadastro = []
    for i in range(len(nome)):
        list = (nomeAluno[i], matricula[i], serie[i])
        cadastro.append(list)  

    cadastroOrdenado = sorted(cadastro)
    return cadastroOrdenado

#Funções da lista por oficina
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
    for i in range(len(oficinas)):
            ofAtual = oficinas[i]
            print(ofAtual[0])
            alunos = ofAtual[1]
            contAlunos = 0
            for i in range(len(alunos)):
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

while(executando):
        if(cadastrou):
                menu = menuPrincipal1()
        else:
                menu = menuPrincipal2()

        if(menu == 1 and cadastrou == False):
                print("#"*44)
                print("####                                    ####")
                print("####  OS CADASTROS JA FORAM REALIZADOS  ####")
                print("####                                    ####")
                print("#"*44)
        elif(menu == 1 and cadastrou == True):
                cadastraAluno()
                cadastrou = False

        elif(menu == 2):
                fazerInscricoes()

        elif(menu == 3):
                print("Listar inscrições \n1 - Listar por aluno (ordem alfabética de nome) \n2 - Listar por oficina (ordem alfabética) \n3 - Sair")
                opcao = int(input("---> "))
                while(opcao < 1 or opcao > 3):
                        opcao = int(input("Opção inválida, digite novamente. \n---> "))
                if(opcao == 1):
                       print("\n#### Alunos inscritos – Ordem: Alfabética (nome) ####\n")
                       lista = listaOrdenada(nomeAluno)
                       for i in range(len(lista)):
                                tupla = lista[i]
                                print(formataAluno(tupla[0], tupla[1], tupla[2]))                         
                if(opcao == 2):
                        print("#### Alunos inscritos – Ordem: Alfabética (Oficinas) ####\n")
                        imprimeOficinas(listaOficina())
                if(opcao == 3):
                        continue
             
        elif(menu == 4):
                executando = False