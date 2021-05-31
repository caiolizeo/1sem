package Aula7_Condicionais;

import java.util.Scanner;

public class IfAninhado3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Digite o número: ");
		int numero = input.nextInt();
		
		if(numero > 10) {
			System.out.println("O npumero é maior que 10");
		}else if(numero == 10) {
			System.out.println("Você acertou!");
			System.out.println("O número é igual a 10");
		}else if(numero < 10) {
			System.out.println("O número é menor que 10");
		}
		
	}
}
