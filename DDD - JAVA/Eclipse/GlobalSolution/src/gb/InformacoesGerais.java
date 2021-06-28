package gb;
import java.util.*;
	
public class InformacoesGerais {
	private long id;
	private String nome;
	private String imagem;
	private String legenda;
	private double mediaAvaliacao;
	private String descricao;
	private String localizacao;
	private String linkSite;
	private List<Double> arrayNotas = new ArrayList<Double>();
	private List<String> arrayComents = new ArrayList<String>();
	private List<String> arrayNomes = new ArrayList<String>();
	private List<Long> arrayIdUser = new ArrayList<Long>();
	private List<Long> arrayIdComent = new ArrayList<Long>();

	public void adicionaAvaliacao(double nota, String comentario, String nome, long idUser, long idComent) {
		arrayComents.add(comentario);
		arrayNotas.add(nota);
		arrayIdUser.add(idUser);
		arrayNomes.add(nome);
		arrayIdComent.add(idComent);
	
		double soma = 0;
		for(int i = 0; i < arrayNotas.size(); i++) {
			Double notaAtual = arrayNotas.get(i); 
			soma += notaAtual;
		}
		mediaAvaliacao = soma/arrayNotas.size();
	}

	public void mostrarComentario(int index) {
		System.out.println("Nota: "+arrayNotas.get(index));
		System.out.println("Comentario: "+arrayComents.get(index));
		System.out.println("Nome: "+ arrayNomes.get(index));
		System.out.println("ID Usuário: "+arrayIdUser.get(index));
		System.out.println("ID Comentário: "+arrayIdComent.get(index));
	}
	
	public void mostrarDados() {
		System.out.println("Nome do local: " + nome);
		System.out.println("Descrição: " + descricao);
		System.out.println("Nota: " + mediaAvaliacao);
		System.out.println("Link para o site: "+ linkSite);
	}

	public long getId() {
		return id;
	}

	public String getNome() {
		return nome;
	}

	public String getImagem() {
		return imagem;
	}

	public String getLegenda() {
		return legenda;
	}

	public double getMediaAvaliacao() {
		return mediaAvaliacao;
	}

	public String getDescricao() {
		return descricao;
	}

	public String getLocalizacao() {
		return localizacao;
	}

	public String getLinkSite() {
		return linkSite;
	}

	public List<Double> getArrayNotas() {
		return arrayNotas;
	}

	public List<String> getArrayComents() {
		return arrayComents;
	}

	public List<Long> getArrayIdUser() {
		return arrayIdUser;
	}

	public List<String> getArrayNomes() {
		return arrayNomes;
	}
	
	public List<Long> getArrayIdNomes() {
		return arrayIdUser;
	}

	protected void setNome(String nome) {
		this.nome = nome;
	}

	protected void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public void setImagem(String imagem) {
		this.imagem = imagem;
	}

	public void setLegenda(String legenda) {
		this.legenda = legenda;
	}

	public void setMediaAvaliacao(double mediaAvaliacao) {
		this.mediaAvaliacao = mediaAvaliacao;
	}

	public void setLocalizacao(String localizacao) {
		this.localizacao = localizacao;
	}

	public void setLinkSite(String linkSite) {
		this.linkSite = linkSite;
	}

}
