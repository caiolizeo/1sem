package gb;

public class Parques extends InformacoesGerais {
	private String horarioFunc;
	
	public Parques(String nome, String descricao, String site) {
		setNome(nome);
		setDescricao(descricao);
		setLinkSite(site);
	}

	public String getHorarioFunc() {
		return horarioFunc;
	}

	public void setHorarioFunc(String horarioFunc) {
		this.horarioFunc = horarioFunc;
	}
	
}
