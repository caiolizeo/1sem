package conta;

public class TesteConta {

	public static void main(String[] args) {
		
	
		Conta conta = new Conta("Caio", 987321, 5000.00);
		
		System.out.println(conta.getNome());
		System.out.println(conta.getNumero());
		System.out.println(conta.getSaldo());
		
		conta.depositar();
		System.out.println(conta.getSaldo());

		conta.sacar();
		System.out.println(conta.getSaldo());
		
		
	}

}


/*
 * Exerc?cio Conta 3.Cria uma classe Conta que contenha o nome do cliente, o n?mero da conta e o saldo. 
 * Estes valores dever?o ser informador no construtor da classe. 
 * O programa deve ter: 
 * 1. Um m?todo para depositar (para realizar o dep?sito) 
 * 2. Um m?todo para sacar (para realizar o saque de valores da conta) 
 * 3. Crie os m?todos getters e setters para cada atributo da classe 
 * 4. O programa principal deve instanciar objetos da classe Conta e utilizar seus m?todos. 
 */
