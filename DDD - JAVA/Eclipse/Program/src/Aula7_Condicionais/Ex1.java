package Aula7_Condicionais;

import java.util.Scanner;

public class Ex1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int numero;
		
		System.out.print("Digite o numero: ");
		numero = input.nextInt();
		
		if(numero > 100) {
			numero = numero + 150;
		}
	
		System.out.println("numero: "+numero);
	}

}
