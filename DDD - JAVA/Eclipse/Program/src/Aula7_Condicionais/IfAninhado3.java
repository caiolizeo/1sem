package Aula7_Condicionais;

import java.util.Scanner;

public class IfAninhado3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Digite o n�mero: ");
		int numero = input.nextInt();
		
		if(numero > 10) {
			System.out.println("O npumero � maior que 10");
		}else if(numero == 10) {
			System.out.println("Voc� acertou!");
			System.out.println("O n�mero � igual a 10");
		}else if(numero < 10) {
			System.out.println("O n�mero � menor que 10");
		}
		
	}
}
