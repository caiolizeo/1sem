
/*
        Caio Lizeo Soares - 87809
        Isabela Bianca Correa de Macedo - 88493
        Jonatan Jacó Mascalhusk De Oliveira Souza - 88221
        Lucas Amorim Marques Pereira - 84659
        Rodrigo Gonzalo Barbosa Segura - 83954    
*/ 


function Pessoa(nome,senha){
    this.nome = nome
    this.senha = senha
}

let arrayNome = ["Caio", "Isabela", "Jonatan", "Lucas", "Rodrigo"];
let arraySenha = ["87809", "88493", "88221", "84659", "83954"];
let contAssunto;
let contNome;
let contComent;

const botaoSubmit = document.getElementById('btn_submit');

function pag_login(){
    botaoSubmit.addEventListener('click',function(){
        let userName = nome.value;
        let userPass = senha.value;
        const pessoa = new Pessoa(userName,userPass);
        let verificaNome = arrayNome.includes(pessoa.nome);
        let indexNome = arrayNome.indexOf(pessoa.nome);
    
        if(verificaNome == true){
            console.log("Nome correto");
        } else{
            console.log("Nome incoreto");
        }
    
        if(userPass == arraySenha[indexNome]){
            console.log("Senha correta");
        } else{
            console.log("Senha incorreta");
        }
    
        if(verificaNome == true && userPass == arraySenha[indexNome]){
            window.location.href = "./portal.html";    
        }
    
        
        console.log("Senha do index: "+arraySenha[indexNome]);
        console.log('Nome  : ' + pessoa.nome);
        console.log('Senha : ' + pessoa.senha);
    
    
    });
}

function pag_cadastro(){
    botaoSubmit.addEventListener('click',function(){
        let userName = nome.value;
        let userPass = senha.value;
        let cadastraNome = arrayNome.push(userName);
        let cadastraSenha = arraySenha.push(userPass)

        console.log(arrayNome);
 

        alert("Usuários cadastrados: "+arrayNome)
        window.location.href = "./index.html";
    });
}

function pag_faleconosco(){
    botaoSubmit.addEventListener('click',function(){
        
        contAssunto = assunto.value;
        contNome = nome.value;
        contComent = comentario.value

        if(contAssunto == "" || contNome == "" || contComent == ""){
            alert("Ao menos um dos campos ficaram em branco")
        }
        if(contAssunto != "" && contNome != "" && contComent != ""){
            alert("Todos os campos foram preenchidos, essa página ainda não envia e-mail, mas caso enviasse já estaria garantido que os campos foram preenchidos")
            window.location.href = "./portal.html";
        }


        console.log(contAssunto);
        console.log(contNome);
        console.log(contComent);
    
    });

}






function check_form(){
    var inputs = document.getElementsByClassName('required');
  var len = inputs.length;
  var valid = true;
  for(var i=0; i < len; i++){
     if (!inputs[i].value){ valid = false; }
  }
  if (!valid){
    alert('Por favor preencha todos os campos.');
    return false;
  } else { return true; }
}