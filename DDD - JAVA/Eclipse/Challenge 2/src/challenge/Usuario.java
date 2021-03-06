package challenge;

public class Usuario {    
	private long UserId;
	private String email;
	private String senha;
	private String nome;
	private String sobrenome;
	private String dtNascimento;
	private String genero;
	private String telefone;
	private String tipoUsuario;
	private String especialidade;
	private String tipoDocumento;
	private String numeroDocumento;
	private String foto;
	private String status;
	private String biografia;
	
	public Usuario (long userId,String email, String senha, String nome, String sobrenome,
			String dtNascimento, String genero, String telefone, String tipoUsuario) {
		this.UserId = userId;	
		this.email = email;
		this.senha = senha;
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.dtNascimento = dtNascimento;
		this.genero = genero;
		this.telefone = telefone;
		this.tipoUsuario = tipoUsuario;
	}
	

	public long getUserId() {
		return UserId;
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

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}

	public void setSobrenome(String sobrenome) {
		this.sobrenome = sobrenome;
	}

	public String getDtNascimento() {
		return dtNascimento;
	}

	public void setDtNascimento(String dtNascimento) {
		this.dtNascimento = dtNascimento;
	}

	public String getGenero() {
		return genero;
	}

	public void setGenero(String genero) {
		this.genero = genero;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getTipoUsuario() {
		return tipoUsuario;
	}

	public void setTipoUsuario(String tipoUsuario) {
		this.tipoUsuario = tipoUsuario;
	}

	public String getEspecialidade() {
		return especialidade;
	}

	public void setEspecialidade(String especialidade) {
		this.especialidade = especialidade;
	}

	public String getTipoDocumento() {
		return tipoDocumento;
	}

	public void setTipoDocumento(String tipoDocumento) {
		this.tipoDocumento = tipoDocumento;
	}

	public String getNumeroDocumento() {
		return numeroDocumento;
	}

	public void setNumeroDocumento(String numeroDocumento) {
		this.numeroDocumento = numeroDocumento;
	}

	public String getFoto() {
		return foto;
	}

	public void setFoto(String foto) {
		this.foto = foto;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getBiografia() {
		return biografia;
	}

	public void setBiografia(String biografia) {
		this.biografia = biografia;
	}

}
