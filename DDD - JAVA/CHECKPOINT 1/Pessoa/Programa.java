class Programa {
	public static void main(String[] args){
		System.out.println("----------------------------------------");
		//inicio do objeto 1
		Pessoa p1 = new Pessoa();
		
		p1.nome = "João";
		p1.sobrenome= "Silva";
		p1.endereco = "Av. Paulista 123";
		p1.rg = 112223334;
		p1.anoNascimento = 1990;
		p1.peso = 90.25;

		
		System.out.println("Nome completo: "+p1.nome+" "+p1.sobrenome);
		System.out.println("Endereço: "+p1.endereco);
		System.out.println("RG: "+p1.rg);
		System.out.println("Ano de nascimento: "+p1.anoNascimento);
		System.out.println("Peso: "+p1.peso);
		//fim do objeto 1
		System.out.println("----------------------------------------");

		//inicio do objeto 2
		Pessoa p2 = new Pessoa();
		
		p2.nome = "Carlos";
		p2.sobrenome = "Santos";
		p2.endereco = "Al. Santos 50";
		p2.rg = 998887776;
		p2.anoNascimento = 1998;
		p2.peso = 80.35;
		

		System.out.println("Nome completo: "+p2.nome+" "+p2.sobrenome);
		System.out.println("Endereço: "+p2.endereco);
		System.out.println("RG: "+p2.rg);
		System.out.println("Ano de nascimento: "+p2.anoNascimento);
		System.out.println("Peso: "+p2.peso);
		//fim do objeto 2
		System.out.println("----------------------------------------");
		
		//inicio do objeto 3
		Pessoa p3 = new Pessoa();
		
		p3.nome = "Ana";
		p3.sobrenome = "Soares";
		p3.endereco = "Av. Marechal Deodoro 300";
		p3.rg = 665554443;
		p3.anoNascimento = 1995;
		p3.peso = 65.5;

		System.out.println("Nome: "+p3.nome+" "+p3.sobrenome);
		System.out.println("Endereço: "+p3.endereco);
		System.out.println("RG: "+p3.rg);
		System.out.println("Ano de nascimento: "+p3.anoNascimento);
		System.out.println("Peso: "+p3.peso);
		//fim do objeto 3
		System.out.println("----------------------------------------");
	}

}