package gb;

public class LocacaoCarro extends InformacoesGerais {
	private String tipoCarro;

	public LocacaoCarro(String nome, String descricao, String site) {
		setNome(nome);
		setDescricao(descricao);
		setLinkSite(site);
	}
	
	public String getTipoCarro() {
		return tipoCarro;
	}
	public void setTipoCarro(String tipoCarro) {
		this.tipoCarro = tipoCarro;
	}
	
	
}
