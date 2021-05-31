class Programa{
	public static void main(String[] args){
		System.out.println("----------------------------------------");
		//inicio do objeto 1
		Apartamento ap1 = new Apartamento();
		
		ap1.area=100.5;
		ap1.moradores=4;
		ap1.numeroAp=301;
		ap1.quartos=3;
		ap1.banheiros=1;
		ap1.proprietario="Paulo Nascimento";
		
		System.out.println("Area: "+ap1.area+" m2");
		System.out.println("Moradores: "+ap1.moradores);
		System.out.println("Número do Apartamento: "+ap1.numeroAp);
		System.out.println("Quartos: "+ap1.quartos);
		System.out.println("Banheiros: "+ap1.banheiros);
		System.out.println("Proprietário: "+ap1.proprietario);
		//fim do objeto 1

		System.out.println("----------------------------------------");
		//inicio do objeto 2
		Apartamento ap2 = new Apartamento();
		
		ap2.area=65.0;
		ap2.moradores=2;
		ap2.numeroAp=91;
		ap2.quartos=2;
		ap2.banheiros=1;
		ap2.proprietario="Luis dos Santos";

		System.out.println("Area: "+ap2.area+" m2");
		System.out.println("Moradores: "+ap2.moradores);
		System.out.println("Número do Apartamento: "+ap2.numeroAp);
		System.out.println("Quartos: "+ap2.quartos);
		System.out.println("Banheiros: "+ap2.banheiros);
		System.out.println("Proprietário: "+ap2.proprietario);
		//fim do objeto 2

		System.out.println("----------------------------------------");

		//inicio do objeto 3
		Apartamento ap3 = new Apartamento();
		
		ap3.area=140.5;
		ap3.moradores=5;
		ap3.numeroAp=15;
		ap3.quartos=4;
		ap3.banheiros = 2;
		ap3.proprietario = "Silvana Soares";

		System.out.println("Area: "+ap3.area+" m2");
		System.out.println("Moradores: "+ap3.moradores);
		System.out.println("Número do Apartamento: "+ap3.numeroAp);
		System.out.println("Quartos: "+ap3.quartos);
		System.out.println("Banheiros: "+ap3.banheiros);
		System.out.println("Proprietário: "+ap3.proprietario);
		//fim do objeto 3

		System.out.println("----------------------------------------");

	}
}