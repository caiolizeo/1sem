class Funcionario{
	String nome;
	String departamento;
	double salario;
	String dataCont;
	String rg;

	void recebeAumento(double aumento){
		this.salario = this.salario+aumento;
		System.out.println("Valor do aumento: R$"+aumento);
	}

	double calculaGanhoAnual(){
		double ganhoAnual = this.salario*12;
		//System.out.println("Salario anual: R$"+ganhoAnual);
		return ganhoAnual;
	}

	void mostra(){
		System.out.println("Nome: "+this.nome);
		System.out.println("Departamento: "+this.departamento);
		System.out.println("Salario: "+this.salario);
		System.out.println("Data da contratação: "+ this.dataCont;
		System.out.println("RG: "+ this.rg);
	}
}
