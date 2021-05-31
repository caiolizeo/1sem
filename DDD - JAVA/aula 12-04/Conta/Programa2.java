class Programa2 {
	public static void main(String[] args){
		
		Funcionario novoFuncionario =  new Funcionario();
		
		novoFuncionario.salario = 750.0;
		

		novoFuncionario.recebeAumento(250.0);

		double ganhoAnual = novoFuncionario.calculaGanhoAnual();
		System.out.println("Ganho Anual: R$"+ ganhoAnual);
				
	}

}