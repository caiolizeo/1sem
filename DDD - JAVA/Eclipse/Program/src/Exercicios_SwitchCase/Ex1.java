package Exercicios_SwitchCase;

import java.util.Scanner;

public class Ex1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Digite o m�s: ");
		String mes = input.next();
		
		switch (mes){
		
		case "dezembro", "janeiro", "fevereiro", "junho", "julho":
			System.out.println("alta temporada");
			break;
		default:
			System.out.println("baixa temporada");
			break;
		}
	}
}
