package Aula7_Condicionais;

import java.util.Scanner;

public class Exemplo1 {
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int numeroFinal = 0; 
		
		System.out.print("Digite o numero: ");
		int teste = input.nextInt();
		
		if(teste == 15) {
			numeroFinal = 12;
		}
		
		System.out.println(numeroFinal);
	}
}
