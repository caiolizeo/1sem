package Aula7_Condicionais;

import java.util.Scanner;

public class IfAninhado2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int numero1, numero2, numero3;
		
		System.out.println("Digite n�mero 1: ");
		numero1 = input.nextInt();
		System.out.println("Digite o n�mero 2: ");
		numero2 = input.nextInt();
		System.out.println("Digite o n�mero 3: ");
		numero3 = input.nextInt();
		
		
		if(numero1 > numero2 && numero1 > numero3) {
			System.out.println("Maior n�mero: "+numero1);
		}else if(numero2 > numero1 && numero2 > numero3) {
			System.out.println("Maior n�mero: "+numero2);
		}else if(numero3 > numero1 && numero3 > numero2) {
			System.out.println("Maior n�mero: "+numero3);
		}
		
		
	}
}