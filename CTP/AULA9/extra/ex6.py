lado1 = int(input("Digite o lado 1 --> "))
lado2 = int(input("Digite o lado 2 --> "))
lado3 = int(input("Digite o lado 3 --> "))

if(lado1 == lado2 == lado3):
    print("Triângulo equilátero")
elif(lado1 == lado2):
    print("Triângulo isosceles")
elif(lado1 == lado3):
    print("Triângulo isosceles")
elif(lado2 == lado3):
    print("Triângulo isosceles")
elif(lado1 != lado2 != lado3):
    print("Triângulo escaleno")