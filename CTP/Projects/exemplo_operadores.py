numero_1=int(input("Entre com um número: "))
numero_2=int(input("Entre com outro número: "))
numeros = [5,2,3,1]

print("Conjunto de números: ", numeros)

print("\nUsando / para divisão: ",numero_1/numero_2)
print("\nUsando // para divisão: ",numero_1//numero_2)
print("\nUsando % para divisão: ",numero_1%numero_2)
print("\nPrimeiro número é igual ao segundo: ",numero_1 == numero_2)
print("Números identicos: ",numero_1 is numero_2)
print("Números não identicos: ",numero_1 is not numero_2)
print("Primeiro número é membro do conjunto: ",numero_1 in numeros)
print("Segundo número não é membro do conjunto: ",numero_2 not in numeros)

print("\nPrimeiro número é >= a 8 e o segundo < que 10: ",numero_1>=8 and numero_2<10)
print("\nUsando not... Primeiro número é igual a 8: ",not(numero_1==8))