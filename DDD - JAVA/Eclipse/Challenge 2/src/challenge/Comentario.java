package challenge;

public class Comentario {
	private long userId;
	private long pubId;
	private long comentId;
	private String data;
	private String conteudo;
	
	public Comentario(long userId, long pubId, long comentId, String data, String conteudo) {
			this.userId = userId;
			this.pubId = pubId;
			this.comentId = comentId;
			this.data = data;
			this.conteudo = conteudo;
			
	}

	
	public long getUserId() {
		return userId;
	}

	public long getPubId() {
		return pubId;
	}

	public long getComentId() {
		return comentId;
	}

	public String getData() {
		return data;
	}

	public String getConteudo() {
		return conteudo;
	}
	
}
