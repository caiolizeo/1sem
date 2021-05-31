class Programa{
	public static void main(String[] args){
		
		System.out.println("----------------------------------------");
		//inicio do objeto 1
		Carro c1 = new Carro();
	
		c1.marca = "Ferrari";
		c1.modelo = "F40";
		c1.tracao = "Traseira";
		c1.peso = 1110.0;
		c1.potencia = 478;
		c1.aceleracao = 4.1;

		System.out.println("Marca: "+c1.marca);
		System.out.println("Modelo: "+c1.modelo);
		System.out.println("Tração: "+c1.tracao);
		System.out.println("Peso: "+c1.peso+" kg");
		System.out.println("Potência: "+c1.potencia+" cv");
		System.out.println("Aceleração 0-100km/h: "+c1.aceleracao+" segundos");
		//fim do objeto 1

		System.out.println("----------------------------------------");
		//inicio do objeto 2
		Carro c2 = new Carro();
		
		c2.marca = "Fiat";
		c2.modelo = "Uno";
		c2.tracao = "Dianteira";
		c2.peso = 825.0;
		c2.potencia = 71;
		c2.aceleracao = 12.4;

		System.out.println("Marca: "+c2.marca);
		System.out.println("Modelo: "+c2.modelo);
		System.out.println("Tração: "+c2.tracao);
		System.out.println("Peso: "+c2.peso+" kg");
		System.out.println("Potência: "+c2.potencia+" cv");
		System.out.println("Aceleração 0-100km/h: "+c2.aceleracao+" segundos");
		//fim do objeto 2
		
		System.out.println("----------------------------------------");
		//inicio do objeto 3
		Carro c3 = new Carro();
		
		c3.marca = "Chevrolet";
		c3.modelo = "S10";
		c3.tracao = "4x4";
		c3.peso = 1808.0;
		c3.potencia = 200;
		c3.aceleracao = 10.4;

		System.out.println("Marca: "+c3.marca);
		System.out.println("Modelo: "+c3.modelo);
		System.out.println("Tração: "+c3.tracao);
		System.out.println("Peso: "+c3.peso+" kg");
		System.out.println("Potência: "+c3.potencia+" cv");
		System.out.println("Aceleração 0-100km/h: "+c3.aceleracao+" segundos");
		//fim do objeto 3
		System.out.println("----------------------------------------");		
	}
}