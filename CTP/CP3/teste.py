nomeAluno = ["João", "Maria", "Marcos"]
matricula = [111, 222, 333]
serie = [2, 2, 2]
qtdInscrito = [0, 0, 0]

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

cadastrou = True



rm = int(input("Digite o rm: "))
while(rm != 0):
    if(qtdInscrito[matricula.index(rm)] < 3):
        valor = qtdInscrito[matricula.index(rm)] + 1
        qtdInscrito[matricula.index(rm)] = valor
    else:
        print("LIMITE DE 3")
    rm = int(input("Digite o rm: "))



print(nomeAluno)
print(matricula)
print(serie)
print(qtdInscrito)
