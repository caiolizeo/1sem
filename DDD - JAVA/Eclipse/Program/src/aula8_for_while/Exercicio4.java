package aula8_for_while;

import java.util.Scanner;

public class Exercicio4 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int numero;
		do {
			System.out.println("Digite um número: ");
			numero = input.nextInt();
		}while(numero < 2 || numero > 1000);
		
		for(int i =1; i <= 10; i++) {
			int result = i*numero;
			System.out.println(i+"x"+numero+"="+result);
		}
	}
}
