class Conta {
	int numero;
	String dono;
	double saldo;
	double limite;

	boolean sacar(double valor){
		if(this.saldo < valor){
			return false;
		} else {
			this.saldo = this.saldo - valor;
			return true;
		}
	}
	
	void depositar(double valor){

		this.saldo = this.saldo + valor;
		System.out.println("Deposito realizado: R$" + valor);
	}

	void transferir(Conta destino, double valor) {
	
		this.saldo = this.saldo - valor;
		destino.saldo = destino.saldo + valor;
	}


}