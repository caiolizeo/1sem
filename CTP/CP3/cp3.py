import funcoes

cadastrou = True
finalizou = True

while(finalizou):
        if(cadastrou):
                menu = funcoes.menuPrincipal1()
        else:
                menu = funcoes.menuPrincipal2()

        if(menu == 1 and cadastrou == False):
                print("#"*44)
                print("####                                    ####")
                print("####  OS CADASTROS JA FORAM REALIZADOS  ####")
                print("####                                    ####")
                print("#"*44)
        elif(menu == 1 and cadastrou == True):
                funcoes.cadastraAluno()
                cadastrou = False

        elif(menu == 2):
                funcoes.fazerInscricoes()

        elif(menu == 3):
                print("Listar inscrições \n1 - Listar por aluno (ordem alfabética de nome) \n2 - Listar por oficina (ordem alfabética) \n3 - Sair")
                opcao = int(input("---> "))
                while(opcao < 1 or opcao > 3):
                        opcao = int(input("Opção inválida, digite novamente. \n---> "))
                if(opcao == 1):
                       print("\n#### Alunos inscritos – Ordem: Alfabética (nome) ####\n")
                       funcoes.listaAluno(funcoes.ordenaLista(funcoes.nomeAluno))
                if(opcao == 2):
                        print("#### Alunos inscritos – Ordem: Alfabética (Oficinas) ####\n")
                        funcoes.imprimeOficinas(funcoes.listaOficina())
                if(opcao == 3):
                        continue
                
        elif(menu == 4):
                finalizou = False