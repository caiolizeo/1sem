package teste;
import gb.Parques;
import gb.Usuario;

public class TesteParques {

	public static void main(String[] args){
		Usuario usuario1 = new Usuario("João", "Silva");
		Usuario usuario2 = new Usuario("Maria", "Alves");
		Parques jdBotanico = new Parques("Jardim Botânico de São Paulo","descricao", "https://jardimbotanico.sp.gov.br/");
		
		jdBotanico.adicionaAvaliacao(usuario1.gerarNota(), usuario1.gerarComentario(), usuario1.getNome(), usuario1.getIdUsuario(), usuario1.getIdAvaliacao());
		jdBotanico.mostrarComentario(0);
		jdBotanico.adicionaAvaliacao(usuario2.gerarNota(), usuario2.gerarComentario(), usuario2.getNome(), usuario2.getIdUsuario(), usuario2.getIdAvaliacao());
		jdBotanico.mostrarComentario(1);
		
		jdBotanico.mostrarDados();
		
		
	}

}