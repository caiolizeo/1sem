package teste;
import gb.Gastronomia;
import gb.Usuario;

public class TesteGastronomia {

	public static void main(String[] args){
		Usuario usuario1 = new Usuario("João", "Silva");
		Usuario usuario2 = new Usuario("Maria", "Alves");
		Gastronomia terrItalia = new Gastronomia("Terraço Itália","descricao", "https://www.terracoitalia.com.br/");
		
		terrItalia.adicionaAvaliacao(usuario1.gerarNota(), usuario1.gerarComentario(), usuario1.getNome(), usuario1.getIdUsuario(), usuario1.getIdAvaliacao());
		terrItalia.mostrarComentario(0);
		terrItalia.adicionaAvaliacao(usuario2.gerarNota(), usuario2.gerarComentario(), usuario2.getNome(), usuario2.getIdUsuario(), usuario2.getIdAvaliacao());
		terrItalia.mostrarComentario(1);
		
		terrItalia.mostrarDados();
		
		
	}

}
