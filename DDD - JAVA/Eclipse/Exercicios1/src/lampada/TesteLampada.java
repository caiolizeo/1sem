package lampada;

public class TesteLampada {

	public static void main(String[] args) {
		Lampada lamp = new Lampada();
		
		lamp.estadoLampada();
		
		lamp.ligaLampada();
		
		lamp.estadoLampada();
		
		lamp.desligaLampada();
		
		lamp.estadoLampada();
	}

}
