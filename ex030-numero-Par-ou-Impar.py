# Crie um programa que leia um número inteiro e mostre se ele é par ou impar?
#porcentagem pega o resto de uma operação
#todo múmero par o resto é zero "0"
#exemplo: 4 o resto é 0
#todo número impar o resto é Um "1"
#exemplo: 5 o resto é 1

#O resto da divisão de qualquer número impar dividido por dois é igual a Um
#o resto da divisão de qualquer número par dividido por dois é igual a zero

#>>>>>>>>>>>>>>>>>>>>>>>>>>
# Par = 0                |>
# Impar = 1              |>
#>>>>>>>>>>>>>>>>>>>>>>>>>>
#------------------------------------------------------cores------------------------------------------------------------

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
#modelos:
#print(f'O número {num} é {GREEN}Par{RESET}')
#print(f'{GREEN}Tenha um bom dia! Dirija com segurança!{RESET}')
#print(f'{YELLOW}Você deve pagar uma multa de R$ {multa:.2f}{RESET}')

#------------------------------------------------------Par ou Impar?----------------------------------------------------

num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print(f'O número {num} é {GREEN}Par{RESET}')
else:
    print(f'O número {num} é {RED}Impar!{RESET}')


#-----------------------------------------------------------------------------------------------------------------------













