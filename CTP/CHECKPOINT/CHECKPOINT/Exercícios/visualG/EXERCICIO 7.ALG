Algoritmo "Exercicio 7"
// Disciplina   : CTP
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Data atual  : 21/03/2021
Var
// Seção de Declarações das variáveis 
 boleto, juros, novo_valor:real
 dias:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite o valor do boleto: ")
leia(boleto)
escreva("Digite o valor dos juros: ")
leia(juros)
escreva("Digite os dias em atraso: ")
leia(dias)

novo_valor:=boleto+(boleto*(juros/100))*dias
escreva("Novo valor do boleto: ",novo_valor)

Fimalgoritmo