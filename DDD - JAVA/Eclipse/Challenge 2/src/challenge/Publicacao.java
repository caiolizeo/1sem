package challenge;

public class Publicacao {
	private long pubId;
	private long userId;
	private String data;
	private String tema;
	private String status;
	private String conteudo;
	private String video;
	private String img;
	
	public Publicacao(long userId, long pubId, String data, String tema, String status, String conteudo) {
		this.pubId = pubId;
		this.userId = userId;
		this.data = data;
		this.tema = tema;
		this.status = status;
		this.conteudo = conteudo;
	}
	
	
	public long getPubId() {
		return pubId;
	}

	public void setPubId(long pubId) {
		this.pubId = pubId;
	}

	public long getUserId() {
		return userId;
	}

	public void setUserId(long userId) {
		this.userId = userId;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public String getTema() {
		return tema;
	}

	public void setTema(String tema) {
		this.tema = tema;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getConteudo() {
		return conteudo;
	}

	public void setConteudo(String conteudo) {
		this.conteudo = conteudo;
	}

	public String getVideo() {
		return video;
	}

	public void setVideo(String video) {
		this.video = video;
	}

	public String getImg() {
		return img;
	}

	public void setImg(String img) {
		this.img = img;
	}
}
