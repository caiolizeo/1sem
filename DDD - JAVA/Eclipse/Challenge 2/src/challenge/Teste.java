package challenge;

import java.text.SimpleDateFormat;
import java.text.DateFormat;
import java.util.Date;


public class Teste {
	static SimpleDateFormat dataId = new SimpleDateFormat("SSSSssmmHHddMMyyyy");
	static DateFormat dataAtual = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
	static Date data = new Date();
	
	private static String dataStr() {
	    String dataStr = dataAtual.format(data);
		return dataStr;
	}

	private static long randomId() {
	    String id = dataId.format(System.currentTimeMillis());
	    long numero = Long.valueOf(id).longValue();
	    return numero;
	}
	
	public static void main(String[] args) {
		Usuario user1 = new Usuario(randomId(), "email@email.com", "123456", "Jo?o", "Da Silva",
				"31/03/2000", "masculino", "11 99999-4444", "Usu?rio Comum");
		Publicacao publicacao = new Publicacao(user1.getUserId(), randomId(), dataStr(), "relato", "Feliz", "Texto");
		Comentario coment = new Comentario(user1.getUserId(), publicacao.getPubId(), randomId(), dataStr(), "coment?rio");
		Chat chat = new Chat(user1.getUserId(), randomId(), dataStr(), "Mensagem");
		

		System.out.println("*** USU?RIO ***");
		System.out.println("Id do usuario:"+user1.getUserId());
		System.out.println("email: "+user1.getEmail());
		System.out.println("senha: "+user1.getSenha());
		System.out.println("Nome: "+user1.getNome());
		System.out.println("Sobrenome: "+user1.getSobrenome());
		System.out.println("Nascimento: "+user1.getDtNascimento());
		System.out.println("G?nero: "+user1.getGenero());
		System.out.println("Telefone: "+user1.getTelefone());
		System.out.println("Tipo de usu?rio: "+user1.getTipoUsuario()+"\n");
	
		System.out.println("*** PUBLICA??O ***");
		System.out.println("Id do usuario:"+publicacao.getUserId());
		System.out.println("Id da publica??o: "+publicacao.getPubId());
		System.out.println("Data da publica??o: "+publicacao.getData());
		System.out.println("Tema da publica??o: "+publicacao.getTema());
		System.out.println("Status do usu?rio: "+publicacao.getStatus());
		System.out.println("Conte?do da publica??o: "+publicacao.getConteudo()+"\n");
		
		System.out.println("*** COMENTARIO ***");
		System.out.println("Id do usu?rio: "+coment.getUserId());
		System.out.println("Id da publica??o: "+coment.getPubId());
		System.out.println("Id do comentario: "+coment.getComentId());
		System.out.println("Data do comentario: "+coment.getData());
		System.out.println("Conteudo do comentario: "+coment.getConteudo()+"\n");
		
		System.out.println("*** CHAT ***");
		System.out.println("Id do usuario: "+chat.getUserId());
		System.out.println("Id do chat: "+chat.getChatId());
		System.out.println("Data da mensagem: "+chat.getData());
		System.out.println("Conteudo da mensagem: "+chat.getMsg());
	}	
}
