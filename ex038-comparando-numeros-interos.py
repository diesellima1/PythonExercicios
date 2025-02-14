#Escrsó que eu tô com preguiça de escrever eva um programa que leia 2 números inteiros e compare os
# mostrando na tela uma mensagem
# -o primeiro valor é maior
# -o segundo valor é maior
# -não existe valor
# maior os 2 são iguais


#-------------------------------------------------compare---------------------------------------------------------------
# Solicita os dois números inteiros
num1 = int(input('Primeiro número? :'))
num2 = int(input('Segundo número? :'))
# Compara os números e exibe a mensagem correspondente
if num1 > num2:
    print('O PRIMEIRO valor é MAIOR.')
elif num1 < num2:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Não existe valor maior, os dois são IGUAIS.')

#-----------------------------------------------------------------------------------------------------------------------

