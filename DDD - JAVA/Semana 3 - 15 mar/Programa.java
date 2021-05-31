class Programa{
	public static void main(String[] args){
		Conta minhaConta;
		minhaConta = new Conta();
		minhaConta.dono = "Caio";
		minhaConta.saldo = 1500;
		minhaConta.numero = 1234;
		minhaConta.limite = 3500;
		System.out.println("Dono: "+minhaConta.dono);
		System.out.println("Saldo: "+minhaConta.saldo);
		System.out.println("Conta: "+minhaConta.numero);
		System.out.println("Limite: "+minhaConta.limite);
	}
}