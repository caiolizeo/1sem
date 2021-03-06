package challenge;

public class Chat {
	private long chatId;
	private long userId;
	private String foto;
	private String data;
	private String msg;
	
	public Chat(long userId, long chatId, String data, String msg) {
		this.chatId = chatId;
		this.userId = userId;
		this.data = data;
		this.msg = msg;
	}
	
	
	public long getChatId() {
		return chatId;
	}

	public long getUserId() {
		return userId;
	}

	public String getFoto() {
		return foto;
	}

	public String getData() {
		return data;
	}
	
	public String getMsg() {
		return msg;
	}
	

}
