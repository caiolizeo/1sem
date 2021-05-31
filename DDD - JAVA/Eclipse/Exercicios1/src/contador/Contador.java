package contador;

public class Contador {
	
	private int contador;
	
	int zeraContador() {
		contador = 0;
		return contador;
	}
	
	int somaContador() {
		contador++;
		return contador;
	}
	
	int getContador() {
		System.out.println("Valor do contador: "+contador);
		return contador;
	}
	
}



/* Crie  uma  classe Contador  que  encapsule  um  valor  usado  para  a  contagem  de  itens  ou eventos. 
 * A Classe deve conter métodos que devem: 
 * a.Zerar o contador; 
 * b.Incrementar o contador em uma unidade; 
 * c.Retornar o valor do contador; 
 * d.O programa principal deve instanciar objetos da classe Contador e utilizar seus métodos; 
*/





