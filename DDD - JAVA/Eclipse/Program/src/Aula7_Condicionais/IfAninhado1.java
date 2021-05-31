package Aula7_Condicionais;

import java.util.Scanner;

public class IfAninhado1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Digite o número: ");
		int numero = input.nextInt();
		
		if(numero < 0) {
			System.out.println("Negativo");
		}else{
			System.out.println("Positivo");
		}
		
		if(numero%2 == 0) {
			System.out.println("Par");
		} else {
			System.out.println("Ímpar");
		}
		
		
	}
}
