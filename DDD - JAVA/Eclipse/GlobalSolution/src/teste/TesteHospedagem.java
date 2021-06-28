package teste;
import gb.Hospedagem;
import gb.Usuario;

public class TesteHospedagem {

	public static void main(String[] args){
		Usuario usuario1 = new Usuario("João", "Silva");
		Usuario usuario2 = new Usuario("Maria", "Alves");
		Hospedagem renaissance = new Hospedagem("Renaissance São Paulo Hotel","descricao", "https://www.renaissancesaopaulohotel.com/");
		
		renaissance.adicionaAvaliacao(usuario1.gerarNota(), usuario1.gerarComentario(), usuario1.getNome(), usuario1.getIdUsuario(), usuario1.getIdAvaliacao());
		renaissance.mostrarComentario(0);
		renaissance.adicionaAvaliacao(usuario2.gerarNota(), usuario2.gerarComentario(), usuario2.getNome(), usuario2.getIdUsuario(), usuario2.getIdAvaliacao());
		renaissance.mostrarComentario(1);
		
		renaissance.mostrarDados();
		
		
	}

}