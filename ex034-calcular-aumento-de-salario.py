#Escreva um programa que pergunte o salário de um funcionário e calcula o valor do seu aumento para salários superiores a
# 1250 calcule um aumento de 10% para os
# inferiores ou iguais o aumento é de 15%



#-----------------------------------------------------------------------------------------------------------------------
# Ask for the employee's salary
# Ask for the employee's salary
salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print('O aumento será de R${:.2f} O novo salário será de R${:.2f}'.format(novo - salario, novo))


#-----------------------------------------------------------------------------------------------------------------------
'''
# Ask for the employee's salary
salario = float(input('Qual é o salário do funcionário? R$'))

# Calculate the increase based on the salary
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

# Print the new salary after the increase
novo_salario = salario + aumento
print(f'O aumento será de R${aumento:.2f}')
print(f'O novo salário será de R${novo_salario:.2f}')
#fonte:ghc
'''