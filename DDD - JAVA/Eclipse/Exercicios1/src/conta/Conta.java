package conta;

import java.util.Scanner;

public class Conta {

	Scanner input = new Scanner(System.in);	
	
	private String nome;
	private int numero;
	private double saldo;
	
	public Conta(String nome, int numero, double saldo) {
		this.nome = nome;
		this.numero = numero;
		this.saldo = saldo;
	}
	
	double depositar() {
		System.out.printf("Digite o valor a ser depositado: \n ---> ");
		double valorDeposito = input.nextDouble();
		if(valorDeposito > 0) {
			this.saldo = saldo + valorDeposito;
		} else {
			System.out.println("Valor inv�lido!");
		}
		
		return saldo;
	}
	
	double sacar() {
		System.out.printf("Digite o valor a ser sacado \n ---> ");
		double valorSaque = input.nextDouble();
		
		if(valorSaque <= saldo && valorSaque > 0 ) {
			this.saldo = saldo - valorSaque;
			System.out.println("Saque realizado no valor de R$"+valorSaque);
			
		} else if(valorSaque <= 0) {
			System.out.println("Valor inv�lido!");
		} else {
			System.out.println("Saldo insuficiente!");
		}
		
		return saldo;
	}
	
	

	public String getNome() {
		return nome;
	}
	public int getNumero() {
		return numero;
	}
	public double getSaldo() {
		return saldo;
	}
	
}



/*
 * Exerc�cio Conta 3.Cria uma classe Conta que contenha o nome do cliente, o n�mero da conta e o saldo. 
 * Estes valores dever�o ser informador no construtor da classe. 
 * O programa deve ter: 
 * 1. Um m�todo para depositar (para realizar o dep�sito) 
 * 2. Um m�todo para sacar (para realizar o saque de valores da conta) 
 * 3. Crie os m�todos getters e setters para cada atributo da classe 
 * 4. O programa principal deve instanciar objetos da classe Conta e utilizar seus m�todos. 
 */