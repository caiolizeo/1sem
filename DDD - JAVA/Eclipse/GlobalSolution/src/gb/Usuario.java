package gb;

public class Usuario extends Avaliacao {
	private long idUsuario;
	private String nome;
	private String sobrenome;
	private String email;
	private String senha;
	
	public Usuario(String nome, String sobrenome) {
		idUsuario = randomId();
		this.nome = nome;
		this.sobrenome = sobrenome;
		
	}
	
	public long getIdUsuario() {
		return idUsuario;
	}
	public void setIdUsuario(long idUsuario) {
		this.idUsuario = idUsuario;
	}
	public String getNome() {
		return nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}
	
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getSenha() {
		return senha;
	}
	public void setSenha(String senha) {
		this.senha = senha;
	}
}
