Algoritmo "Exercicio 8"
// Disciplina   : CTP
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Data atual  : 21/03/2021
Var
// Seção de Declarações das variáveis 
salario, despesas, sobra, anos, objetivo:real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva("Digite o valor do seu salário: ")
leia(salario)
escreva("Digite o valor de suas despesas: ")
leia(despesas)
objetivo:=1000000
sobra:=salario-despesas
anos:=objetivo/(sobra*12)

escreval(anos:2:2, "para se tornar milionário")

Fimalgoritmo