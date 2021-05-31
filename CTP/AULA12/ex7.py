tentativa=1
numero=int(input("Digite o número: "))
chute=int(input("Chute número {}: ".format(tentativa)))

while(chute != numero):
    if(chute < numero):
        print("*** CHUTOU BAIXO ***")
        tentativa+=1
        chute=int(input("Chute número {}: ".format(tentativa)))
    
    if(chute > numero):
        print("*** CHUTOU ALTO ***")
        tentativa+=1
        chute=int(input("Chute número {}: ".format(tentativa)))

print("*** ACERTOU! VOCÊ PRECISOU DE {} CHANCES ***".format(tentativa))