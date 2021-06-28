package teste;
import gb.Cultura;
import gb.Usuario;

public class TesteCultura {

	public static void main(String[] args){
		Usuario usuario1 = new Usuario("João", "Silva");
		Usuario usuario2 = new Usuario("Maria", "Alves");
		Cultura masp = new Cultura("MASP","descricao", "https://masp.org.br/");
		
		masp.adicionaAvaliacao(usuario1.gerarNota(), usuario1.gerarComentario(), usuario1.getNome(), usuario1.getIdUsuario(), usuario1.getIdAvaliacao());
		masp.mostrarComentario(0);
		masp.adicionaAvaliacao(usuario2.gerarNota(), usuario2.gerarComentario(), usuario2.getNome(), usuario2.getIdUsuario(), usuario2.getIdAvaliacao());
		masp.mostrarComentario(1);
		
		masp.mostrarDados();
		
	}

}
