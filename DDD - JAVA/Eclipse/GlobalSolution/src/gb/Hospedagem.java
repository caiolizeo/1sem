package gb;

public class Hospedagem extends InformacoesGerais{
	private String regiao;
	private double distPaulista;
	private double[] precos;
	
	public Hospedagem(String nome, String descricao, String site) {
		setNome(nome);
		setDescricao(descricao);
		setLinkSite(site);
	}
	
	public String getRegiao() {
		return regiao;
	}
	public void setRegiao(String regiao) {
		this.regiao = regiao;
	}
	public double getDistPaulista() {
		return distPaulista;
	}
	public void setDistPaulista(double distPaulista) {
		this.distPaulista = distPaulista;
	}
	public double[] getPrecos() {
		return precos;
	}
	public void setPrecos(double[] precos) {
		this.precos = precos;
	}
	
	
}
