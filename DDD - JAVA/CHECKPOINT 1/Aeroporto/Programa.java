class Programa{
	public static void main(String[] args){
		
		System.out.println("----------------------------------------");
		//inicio do objeto 1
		Aeroporto ar1 = new Aeroporto();
		
		ar1.nome = "Guarulhos";
		ar1.area = 1190000.40;
		ar1.quantHangar = 15;
		ar1.quantPista = 2;
		ar1.quantLoja = 250;
		ar1.vagasEstacionamento = 10000;
		
		System.out.println("Nome: "+ar1.nome);
		System.out.println("Area: "+ar1.area+" m2");
		System.out.println("Hangares: "+ar1.quantHangar);
		System.out.println("Pistas: "+ar1.quantPista);
		System.out.println("Lojas: "+ar1.quantLoja);
		System.out.println("Vagas de estacionamento: "+ar1.vagasEstacionamento);
		//fim do objeto 1

		System.out.println("----------------------------------------");
		//inicio do objeto 2
		Aeroporto ar2 = new Aeroporto();
		
		ar2.nome = "Congonhas";
		ar2.area = 5000000.30;
		ar2.quantHangar = 10;
		ar2.quantPista = 2;
		ar2.quantLoja = 200;
		ar2.vagasEstacionamento = 8500;

		System.out.println("Nome: "+ar2.nome);
		System.out.println("Area: "+ar2.area+" m2");
		System.out.println("Hangares: "+ar2.quantHangar);
		System.out.println("Pistas: "+ar2.quantPista);
		System.out.println("Lojas: "+ar2.quantLoja);
		System.out.println("Vagas de estacionamento: "+ar2.vagasEstacionamento);
		//fim do objeto 2

		System.out.println("----------------------------------------");
		//inicio do objeto 3
		Aeroporto ar3 = new Aeroporto();

		ar3.nome = "Viracopos";
		ar3.area = 350000.25;
		ar3.quantHangar = 12;
		ar3.quantPista = 1;
		ar3.quantLoja = 100;
		ar3.vagasEstacionamento = 5000;
		
		System.out.println("Nome: "+ar3.nome);
		System.out.println("Area: "+ar3.area+" m2");
		System.out.println("Hangares: "+ar3.quantHangar);
		System.out.println("Pistas: "+ar3.quantPista);
		System.out.println("Lojas: "+ar3.quantLoja);
		System.out.println("Vagas de estacionamento: "+ar3.vagasEstacionamento);
		//fim do objeto 3

		System.out.println("----------------------------------------");
	}
}