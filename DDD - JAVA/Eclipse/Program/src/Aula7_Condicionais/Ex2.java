package Aula7_Condicionais;

import java.util.Scanner;

public class Ex2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("N�mero 1: ");
		int numero1 = input.nextInt();
		System.out.println("N�mero 2: ");
		int numero2 = input.nextInt();
		
		
		if(numero1 % numero2 == 0) {
			System.out.println("Divis�o exata");
		}else {
			System.out.println("Divis�o n�o exata");
		}
	}
}
