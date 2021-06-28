package teste;
import gb.LocacaoCarro;
import gb.Usuario;

public class TesteLocacaoCarro {

	public static void main(String[] args){
		Usuario usuario1 = new Usuario("João", "Silva");
		Usuario usuario2 = new Usuario("Maria", "Alves");
		LocacaoCarro localiza = new LocacaoCarro("Localiza","descricao", "https://www.localiza.com/");
		
		localiza.adicionaAvaliacao(usuario1.gerarNota(), usuario1.gerarComentario(), usuario1.getNome(), usuario1.getIdUsuario(), usuario1.getIdAvaliacao());
		localiza.mostrarComentario(0);
		localiza.adicionaAvaliacao(usuario2.gerarNota(), usuario2.gerarComentario(), usuario2.getNome(), usuario2.getIdUsuario(), usuario2.getIdAvaliacao());
		localiza.mostrarComentario(1);
		
		localiza.mostrarDados();
		
		
		
	}

}