candidato_a=int(input("Votos do candidato A: "))
candidato_b=int(input("Votos do candidato B: "))
candidato_c=int(input("Votos do candidato C: "))
brancos=int(input("Votos brancos: "))
nulos=int(input("Votos nulos: "))

total=candidato_a+candidato_b+candidato_c+brancos+nulos

porcentagem_a=(candidato_a/total)*100
porcentagem_b=(candidato_b/total)*100
porcentagem_c=(candidato_c/total)*100

porcentagem_brancos=(brancos/total)*100
porcentagem_nulos=(nulos/total)*100

print("")
print("---------------------------")
print("Total: ", total," votos")
print("---------------------------")

print("Candidato A: ",round(porcentagem_a,2),"%")
print("Candidato B: ",round(porcentagem_b,2),"%")
print("Candidato C: ",round(porcentagem_c,2),"%")
print("---------------------------")

print("Brancos: ",round(porcentagem_brancos,2),"%")
print("Nulos: ",round(porcentagem_nulos,2),"%")
print("---------------------------")
print("")

