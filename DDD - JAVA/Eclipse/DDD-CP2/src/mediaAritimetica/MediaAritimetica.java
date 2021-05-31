package mediaAritimetica;

import java.util.Scanner;

public class MediaAritimetica {
	
	Scanner input = new Scanner(System.in);
	
	public void calculaAritimetica() {
		double nota1, nota2, nota3, media;
		
		System.out.printf("Digite a primeira nota \n---> ");
		nota1 = input.nextDouble();
		System.out.printf("Digite a segunda nota \n---> ");
		nota2 = input.nextDouble();
		System.out.printf("Digite a terceira nota \n---> ");
		nota3 = input.nextDouble();
			
		double soma = nota1 + nota2 + nota3;
		media = soma / 3;
		
		System.out.printf("A média é: %.2f \n",media);
		if(media >=6) {
			System.out.println("Aprovado!");
		} else if(media >= 5 && media < 6) {
			System.out.println("Prova Substitutiva!");
		} else if(media < 5) {
			System.out.println("Reprovado!");			
		}
	}
	
	

}
