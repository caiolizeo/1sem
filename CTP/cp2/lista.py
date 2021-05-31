lista_nomes = []
lista_idades = []

for i in range(5):
    lista_nomes.append(input("Digite seu nome: "))
    lista_idades.append(int(input("Digite sua idade: ")))

print("Pessoas com mais de 18 anos: ")

for i in range(5):
    if(lista_idades[i]>18):
        print(lista_nomes[i])
