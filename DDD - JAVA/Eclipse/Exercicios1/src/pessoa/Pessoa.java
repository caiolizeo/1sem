package pessoa;

import java.util.Scanner;

public class Pessoa {
	
	Scanner input = new Scanner(System.in);
	
	private String nome;
	private int nasc;
	private double altura;
	private double imc;
	
	public Pessoa(String nome, int nasc, double altura) {
		this.nome = nome;
		this.nasc = nasc;
		this.altura = altura;
	}

	public String getNome() {
		return nome;
	}
	public int getNasc() {
		return nasc;
	}
	public double getAltura() {
		return altura;
	}
	
	
	public void imprimeDados() {
		System.out.println("Nome: "+this.nome);
		System.out.println("Nascimento: "+this.nasc);
		System.out.println("Altura: "+this.altura);
	}
	
	public void calculaIdade() {
		int idade = 2021 - nasc;
		System.out.println("Sua idade é: "+idade);
	}
	
	public void calculaImc() {
		System.out.println("*** CALCULAR IMC ***");
		System.out.printf("Digite o peso \n---> ");
		int peso = input.nextInt();
		
		this.imc = peso / (altura * altura);
		
		System.out.println("Seu imc é: "+ Math.round(imc));
	}
	
}


/**
 * Exercício Pessoa 
 * 4.Crie  uma  classe  para  representar  uma Pessoa,  com  os  atributos  privados  de  nome,  data  de nascimento e altura. 
 * a.Considere os métodos públicos necessários para getters e setters. 
 * b.Crie um método para imprimir todos os dados de uma pessoa.  
 * c.Crie um método para calcular a idade da pessoa. 
 * d.Crie um método (livre escolha) para realizar alguma ação específica na classe Pessoa. 
 */