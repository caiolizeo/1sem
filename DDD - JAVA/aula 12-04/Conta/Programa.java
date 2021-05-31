class Programa {
	public static void main(String[] args){
		
		Conta minhaConta = new Conta();

		minhaConta.saldo = 1000.00;

		Conta meuSonho = new Conta();
		meuSonho.saldo = 500000.00;

		System.out.println("Minha conta: "+minhaConta.saldo);
		System.out.println("Meu sonho: "+meuSonho.saldo);



		//if(respostaSaque){
		//	System.out.println("Saque realizado");
		//} else {
		//	System.out.println("Saldo insuficiente");
		//}	

		meuSonho.transferir(minhaConta, 100000);
		
		System.out.println("Minha conta: "+minhaConta.saldo);
		System.out.println("Meu sonho: "+meuSonho.saldo);

	}

}