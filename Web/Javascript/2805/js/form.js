
function Pessoa(nome,senha){
    this.nome = nome,
    this.senha = senha
}

//ARRAY DE DADOS
//var dados = ['',''];

//RECUPERANDO O BOTAO DO FORM.
const botaoSubmit = document.getElementById('btnEnviar');
botaoSubmit.addEventListener('click',function(){
    
    let userName = idTxtUser.value;
    let userPass = idTxtPass.value;
    const pessoa = new Pessoa(userName,userPass);
    console.log('Nome  : ' + pessoa.nome);
    console.log('Senha : ' + pessoa.senha);
});




//RECUPERANDO O BOTAO DO FORM.
// const botaoSubmit = document.getElementById('btnEnviar');
// botaoSubmit.addEventListener('click',function(){
//     //CRIANDO UM VETOR DE ELMENTOS(inputs)
//     //const listaInputs = document.querySelectorAll('input[type="text"]')
//     const listaInputs = document.getElementsByTagName('input');

//     //ITERAR A LISTA DE INPUTS
//     for (i in listaInputs) {
//         if ((listaInputs[i].value != '') && (listaInputs[i].type != 'checkbox') && (listaInputs[i].type != undefined)) {
//             dados[i] = listaInputs[i].value;
//         }
//     }
    
//     const pessoa = new Pessoa(dados[0],dados[1]);
//     console.log('Nome  : ' + pessoa.nome);
//     console.log('Senha : ' + pessoa.senha);
// });





//VALIDANDO OS CAMPOS
function validaCamposForm(){
    return true;
}
