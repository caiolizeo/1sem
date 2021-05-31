package aula8_for_while;

import java.util.Scanner;

public class Exercicio3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int senhaPadrao = 1234, senha;
		
		for(int i = 1; i <= 3; i++) {
			System.out.printf("Senha \n--> ");
			senha = input.nextInt();
			if(senha == senhaPadrao){
				System.out.println("Senha Válida!");
			}else {
				System.out.println("Senha inválida");
			}
		}
		
	}
}
