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
		System.out.println("Sua idade �: "+idade);
	}
	
	public void calculaImc() {
		System.out.println("*** CALCULAR IMC ***");
		System.out.printf("Digite o peso \n---> ");
		int peso = input.nextInt();
		
		this.imc = peso / (altura * altura);
		
		System.out.println("Seu imc �: "+ Math.round(imc));
	}
	
}


/**
 * Exerc�cio Pessoa 
 * 4.Crie  uma  classe  para  representar  uma Pessoa,  com  os  atributos  privados  de  nome,  data  de nascimento e altura. 
 * a.Considere os m�todos p�blicos necess�rios para getters e setters. 
 * b.Crie um m�todo para imprimir todos os dados de uma pessoa.  
 * c.Crie um m�todo para calcular a idade da pessoa. 
 * d.Crie um m�todo (livre escolha) para realizar alguma a��o espec�fica na classe Pessoa. 
 */