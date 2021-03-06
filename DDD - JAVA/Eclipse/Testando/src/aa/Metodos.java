package aa;


import java.util.Scanner;

public class Metodos {

	Scanner input = new Scanner(System.in);

	//Opera??es b?sicas
	public double calculaOpBasica(int opcao, double num1, double num2) {
		double resultado = 0;
		
		if(opcao == 1) {
			resultado = num1 + num2;
		} else if(opcao == 2) {
			resultado = num1 - num2;
		}else if(opcao == 3) {
			resultado = num1 * num2;
		}else if(opcao == 4) {
			resultado = num1 / num2;
		}
		return resultado;
	}
		
	//Media ponderada
	public String calculaMediaPonderada(double nota1, double nota2) {
		
		double media;
		String result = null;
		
		
		media = (nota1*0.4)+(nota2*0.6);
		System.out.println(media);
		
	
		System.out.printf("A m?dia ?: %.2f \n",media);
		if(media >=6) {
			result ="Aprovado";
		} else if(media >= 5 && media < 6) {
			result = "Prova Substitutiva";
		} else if(media < 5) {
			result = "Reprovado";			
		}
		return result;
	}
	
	//Media aritimetica
	public String calculaMediaAritimetica(double nota1, double nota2, double nota3) {
			double media;
			String result = null;
			double soma = nota1 + nota2 + nota3;
			media = soma / 3;
			
			System.out.printf("A m?dia ?: %.2f \n",media);
			if(media >=6) {
				result = "Aprovado";
			} else if(media >= 5 && media < 6) {
				result = "Prova Substitutiva";
			} else if(media < 5) {
				result = "Reprovado";			
			}
			return result;
		}
	
	//?rea do c?rculo
	public double calculaAreaCirc(double raio) {					
		double r = Math.PI * (raio * raio);			
		return r;		
	}
	
	//?rea do ret?ngulo
	public double calculaAreaRetangulo(double base, double altura) {					
		double a = base*altura;			
		return a;		
	}
	
	//Velocidade m?dia
	public double calculaVelocidadeMedia(double dist, double tempo) {
        double resultado = dist/tempo;
        return resultado;
    }
	
	//Soma todos os valores
	public int somaTodos(int numero) {
        int soma=0;

        for (int i=1; i<=numero; i++) {
            soma = soma + i;
        }

        return soma;
    }
	
	//Celsius para Fahrenheit
	public double converteCelsParaFah(double celsius) {
		double fahr = celsius * 1.8 + 32;
		return fahr;
	}
	
	//Fahrenheit para Celsius
	public double converteFahParaCels(double fahr) {
		double cels = (fahr-32)/1.8;
		return cels;
	}
	
	//Raiz quadrada (Livre escolha)
	public double calculaRaizQuadrada(double numero) {
	    double resultado = 0;
	    resultado = Math.sqrt(numero);
	    return resultado;
	}
    
	//Op??es do Menu
	public void escolheOpcao(int opcao) {
		if(opcao == 1 || opcao == 2 || opcao == 3 || opcao == 4) {
			//Opera??es b?sicas
			System.out.printf("Digite o primeiro n?mero \n---> ");
			double num1 = input.nextDouble();
			System.out.printf("Digite o segundo n?mero \n---> ");
			double num2 = input.nextDouble();
			System.out.printf("O resultado da opera??o ?: %.2f",calculaOpBasica(opcao, num1, num2));
		} else if(opcao == 5) {
			//M?dia ponderada
			System.out.printf("Digite a primeira nota \n---> ");
			double nota1 = input.nextDouble();
			System.out.printf("Digite a segunda nota \n---> ");
			double nota2 = input.nextDouble();
			String media = calculaMediaPonderada(nota1, nota2);
			System.out.println(media);
			if(media == "Prova Substitutiva") {
				System.out.printf("Digite a nota da prova substitutiva \n---> ");
				double nota3 = input.nextDouble();
				media = calculaMediaPonderada(nota1, nota3);
				if(media == "Prova Substitutiva") {
					media = "Reprovado";
				}
				System.out.println(media);
			}
		} else if(opcao == 6) {
			//M?dia aritim?tica
			System.out.printf("Digite a primeira nota \n---> ");
			double nota1 = input.nextDouble();
			System.out.printf("Digite a segunda nota \n---> ");
			double nota2 = input.nextDouble();
			System.out.printf("Digite a terceira nota \n---> ");
			double nota3 = input.nextDouble();
			
			String media = calculaMediaAritimetica(nota1, nota2, nota3);
			System.out.println(media);
			if(media == "Prova Substitutiva") {
				System.out.printf("Digite a nota da prova substitutiva \n---> ");
				double nota4 = input.nextDouble();
				if(nota1 < nota2 && nota1 < nota3) {
					media = calculaMediaAritimetica(nota4, nota2, nota3);
				} else if(nota2 < nota1 && nota2 < nota3) {
					media = calculaMediaAritimetica(nota4, nota1, nota3);
				} else {
					media = calculaMediaAritimetica(nota4, nota1, nota2);
				}
				if(media == "Prova Substitutiva") {
					media = "Reprovado";
				}
				System.out.println(media);
			}
		} else if(opcao == 7) {
			//?rea do c?rculo
			System.out.printf("Digite valor do raio \n---> ");
			double raio = input.nextInt();
			System.out.printf("A ?rea do c?rculo ?: %.2f", calculaAreaCirc(raio));
		} else if(opcao == 8) {
			//?rea do ret?ngulo
			System.out.printf("Digite valor a base \n---> ");
			double base = input.nextInt();
			System.out.printf("Digite valor a altura \n---> ");
			double altura = input.nextInt();
			System.out.printf("A ?rea do ret?ngulo ?: %.2f", calculaAreaRetangulo(base, altura));
		} else if(opcao == 9) {
			//Velocidade m?dia
		    System.out.printf("Digite a dist?ncia em Km \n---> ");
		    double dist = input.nextDouble();
		    System.out.printf("Digite o tempo de dura??o da viagem em horas \n--->");
		    double tempo = input.nextDouble();
		    System.out.printf("A velocidade m?dia da viagem ? de %.2f Km/h.", calculaVelocidadeMedia(dist, tempo));
		} else if(opcao == 10) {
			//Soma todos os valores
			System.out.printf("Digite um n?mero inteiro \n---> ");
		    int num = input.nextInt();
		    System.out.printf("A soma de todos os valores entre 1 e %d ? %d. ", num, somaTodos(num)); 
		} else if(opcao == 11) {
			//Celsius para Fahrenheit
			System.out.printf("Digite um valor Celsius \n---> ");
			int celsius = input.nextInt();
			System.out.printf("A temperatura em Fahrenheit ?: %.2f", converteCelsParaFah(celsius));
		} else if(opcao == 12) {
			//Fahrenheit para Celsius
			System.out.printf("Digite um valor Fahrenheit \n---> ");
			int fahr = input.nextInt();
			System.out.printf("A temperatura em Celsius ?: %.2f", converteFahParaCels(fahr));
		} else if(opcao == 13) {
			//Raiz quadrada (Livre escolha)
			System.out.printf("Digite o n?mero desejado \n---> ");
			double num = input.nextDouble();
			System.out.printf("A raiz quadrada de %.2f ? %.2f", num, calculaRaizQuadrada(num));
		}
		
		if(opcao != 0) {
			System.out.println("\n\n# # # # # # # # # # # # # # # #");
			System.out.println("# #      FIM DA FUN??O      # #");
			System.out.println("# # # # # # # # # # # # # # # #\n");
		}
		
	}

	//Menu
	public void menu() {
		System.out.println("");
		System.out.println("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #");
		System.out.println("# #                                                     # #");
		System.out.println("# #                        MENU                         # #");
		System.out.println("# #                                                     # #");
		System.out.println("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #");
		System.out.println("# #                                                     # #");
		System.out.println("# #      1 - SOMA                                       # #");
		System.out.println("# #      2 - SUBTRA??O                                  # #");
		System.out.println("# #      3 - MULTIPLICA??O                              # #");
		System.out.println("# #      4 - DIVIS?O                                    # #");
		System.out.println("# #      5 - M?DIA PONDERADA                            # #");
		System.out.println("# #      6 - M?DIA ARITIM?TICA                          # #");
		System.out.println("# #      7 - ?REA DO C?RCULO                            # #");
		System.out.println("# #      8 - ?REA DO RET?NGULO                          # #");
		System.out.println("# #      9 - VELOCIDADE M?DIA                           # #");
		System.out.println("# #     10 - SOMA DE TODOS OS VALORES ENTRE 1 E X       # #");
		System.out.println("# #     11 - CELSIUS PARA FAHRENHEIT                    # #");
		System.out.println("# #     12 - FAHRENHEIT PARA CELSIUS                    # #");
		System.out.println("# #     13 - RAIZ QUADRADA (ESCOLHA LIVRE)              # #");
		System.out.println("# #                                                     # #");
		System.out.println("# #      0 - ENCERRAR                                   # #");
		System.out.println("# #                                                     # #");
		System.out.println("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #");
		System.out.println("");
	}

	public int validaOpcao(int opcao) {
		while(opcao < 0 || opcao > 13) {
			System.out.printf("Op??o inv?lida! Digite novamente \n---> ");	
			opcao = input.nextInt();
		}
		return opcao;
	}
}