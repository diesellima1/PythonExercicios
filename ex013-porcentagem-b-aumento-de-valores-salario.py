#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento!!!

#Formula: valor * valor% / 100 "depios subtrai o resultado pelo valor incial
#Exemplo: R$ 1.518*15/100   #R$ 1.518 sálario minimo atual do Brasil 29/01/2025

salario = float(input('Qual o seu sálario? R$ '))
aumento = float(input('Qual foi a porcentagem de aumento?: '))
calculo = salario + (salario * aumento / 100)
novo_salario = salario - calculo
print('salário R${:.2f} + {:.0f}% aumentou para {:.2f} \n Seu salário subiu para +R${:.2f}'.format(salario, aumento, novo_salario, calculo))