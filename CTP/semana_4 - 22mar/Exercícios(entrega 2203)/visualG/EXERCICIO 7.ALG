Algoritmo "Exercicio 7"
// Disciplina   : CTP
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Data atual  : 21/03/2021
Var
// Se��o de Declara��es das vari�veis 
 boleto, juros, novo_valor:real
 dias:inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Digite o valor do boleto: ")
leia(boleto)
escreva("Digite o valor dos juros: ")
leia(juros)
escreva("Digite os dias em atraso: ")
leia(dias)

novo_valor:=boleto+(boleto*(juros/100))*dias
escreva("Novo valor do boleto: ",novo_valor)

Fimalgoritmo