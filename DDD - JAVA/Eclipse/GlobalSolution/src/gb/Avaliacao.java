package gb;

import java.text.SimpleDateFormat;
import java.util.Scanner;

public class Avaliacao {
	Scanner input = new Scanner(System.in);
	private long idAvaliacao = randomId();
	private double nota;
	private String comentario;
	
	protected long randomId() {
		SimpleDateFormat dataId = new SimpleDateFormat("SSSSssmmHHddMMyyyy");
		String id = dataId.format(System.currentTimeMillis());
	    long numero = Long.valueOf(id).longValue();
	    return numero;
	}
	
	public double gerarNota() {
		System.out.printf("Nota de 0 a 5 estrelas. \n---> ");
		this.nota = input.nextDouble();
		
		while(this.nota < 0 || this.nota > 5) {
			System.out.printf("Nota de 0 a 5 estrelas. \n---> ");
			this.nota = input.nextDouble();
		}
		
		return nota;
	}
	
	public String gerarComentario() {
		
		input.nextLine();
		System.out.print("Comentário. \n---> ");
		this.comentario = input.nextLine();
		return comentario;
	}
	
	public long getIdAvaliacao() {
		return idAvaliacao;
	}
	
	public double getNota() {
		return nota;
	}
	
	public String getComentario() {
		return comentario;
	}

}
