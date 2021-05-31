package mediaPonderada;

import java.util.Scanner;

public class MediaPonderada {
	
	Scanner input = new Scanner(System.in);
	
	public void calculaMediaPonderada() {
		double nota1, nota2, media;
		
		System.out.printf("Digite a primeira nota \n---> ");
		nota1 = input.nextDouble();
		System.out.printf("Digite a segunda nota \n---> ");
		nota2 = input.nextDouble();
		
		media = (nota1*0.4)+(nota2*0.6);
		System.out.println(media);
		
	
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
