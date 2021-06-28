package gb;

public class Gastronomia extends InformacoesGerais{
	
	private String regiao;
	private String indPreco;
	private String tipoCozinha;
	private String horarioFunc;
	private boolean estacionamento;
	
	public Gastronomia(String nome, String descricao, String site) {
		setNome(nome);
		setDescricao(descricao);
		setLinkSite(site);
	}
	
	public String getGastronomia() {
		return regiao;
	}
	public void setGastronomia(String gastronomia) {
		this.regiao = gastronomia;
	}
	public String getIndPreco() {
		return indPreco;
	}
	public void setIndPreco(String indPreco) {
		this.indPreco = indPreco;
	}
	public String getTipoCozinha() {
		return tipoCozinha;
	}
	public void setTipoCozinha(String tipoCozinha) {
		this.tipoCozinha = tipoCozinha;
	}
	public String getHorarioFunc() {
		return horarioFunc;
	}
	public void setHorarioFunc(String horarioFunc) {
		this.horarioFunc = horarioFunc;
	}
	public boolean isEstacionamento() {
		return estacionamento;
	}
	public void setEstacionamento(boolean estacionamento) {
		this.estacionamento = estacionamento;
	}
		
}
