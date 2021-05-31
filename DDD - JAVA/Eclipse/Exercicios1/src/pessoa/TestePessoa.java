package pessoa;

public class TestePessoa {

	public static void main(String[] args) {
		Pessoa usuario = new Pessoa("Caio", 1995, 1.97);
		
		System.out.println(usuario.getNome());
		System.out.println(usuario.getNasc());
		System.out.println(usuario.getAltura());
		
		
		usuario.imprimeDados();
		usuario.calculaIdade();
		usuario.calculaImc();
	}

}
