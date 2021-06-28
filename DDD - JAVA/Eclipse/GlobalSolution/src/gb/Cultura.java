package gb;

public class Cultura extends InformacoesGerais {
	
	private String tipoLocal;
	private String horarioFunc;
	public String melhorDia;
	private double[] precos;
	
	public Cultura(String nome, String descricao, String link) {
		setNome(nome);
		setDescricao(descricao);
		setLinkSite(link);
	}
	
	public String getTipoLocal() {
		return tipoLocal;
	}
	public void setTipoLocal(String tipoLocal) {
		this.tipoLocal = tipoLocal;
	}
	public String getHorarioFunc() {
		return horarioFunc;
	}
	public void setHorarioFunc(String horarioFunc) {
		this.horarioFunc = horarioFunc;
	}
	public String getMelhorDia() {
		return melhorDia;
	}
	public void setMelhorDia(String melhorDia) {
		this.melhorDia = melhorDia;
	}
	public double[] getPrecos() {
		return precos;
	}
	public void setPrecos(double precos[]) {
		this.precos = precos;
	}	
}
