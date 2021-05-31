package lampada;

public class Lampada {
	private boolean lampada = false;
		
	void estadoLampada() {
		if(lampada == true) {
			System.out.println("L�mpada ligada!");
		} else {
			System.out.println("L�mpada desligada!");
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
 * Crie  uma  classe L�mpada  que  pode  ser  ligada  e  desligada.  
 * Tamb�m  deve  ser  poss�vel observar o estado da l�mpada. 
 * O programa principal deve instanciar objetos da classe Lapada e utilizar seus m�todos. 
 */
