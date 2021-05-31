package lampada;

public class Lampada {
	private boolean lampada = false;
		
	void estadoLampada() {
		if(lampada == true) {
			System.out.println("Lâmpada ligada!");
		} else {
			System.out.println("Lâmpada desligada!");
		}
	}
	
	boolean ligaLampada() {
		this.lampada = true;
		return lampada;
	}
	
	boolean desligaLampada() {
		this.lampada = false;
		return lampada;
	}

}



/*
 * Crie  uma  classe Lâmpada  que  pode  ser  ligada  e  desligada.  
 * Também  deve  ser  possível observar o estado da lâmpada. 
 * O programa principal deve instanciar objetos da classe Lapada e utilizar seus métodos. 
 */
