valor_litro=float(input("Informe o valor do combustivel: "))
valor_abastecido=float(input("Informe o valor que se deseja abastecer: "))

resultado=valor_abastecido/valor_litro

print("Serão comprados ",round(resultado, 2)," litros")