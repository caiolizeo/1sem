package checkpoint2;

import java.util.Scanner;

public class TesteMenu {

	public static void main(String[] args) {
		Metodos metodos = new Metodos();
		Scanner input = new Scanner(System.in);
		
		metodos.menu();
		
		System.out.printf("Selecione uma fun??o \n---> ");
		int opcao = input.nextInt();
		System.out.println("");
		opcao = metodos.validaOpcao(opcao);
		metodos.escolheOpcao(opcao);
		
		while(opcao != 0) {
			System.out.printf("Selecione outra fun??o \n---> ");
			opcao = input.nextInt();
			opcao = metodos.validaOpcao(opcao);
			System.out.println("");
			metodos.escolheOpcao(opcao);		
		}
	}
}