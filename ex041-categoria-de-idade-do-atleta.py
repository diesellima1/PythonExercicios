#A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria de acordo com sua idade
#1978 idade do professor guanabara hoje ele tem Idade 47 categoria MASTER aposentada

#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: Sênior
#acima: MASTER

from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print('Idade {} categoria Mirim'.format(idade))
elif idade <= 14:
    print('Idade {} categoria Infantil'.format(idade))
elif idade <= 19:
    print('Idade {} categoria Junior'.format(idade))
elif idade <= 20:
    print('Idade {} categoria Sênior'.format(idade))
else:
    print('Idade {} categoria MASTER'.format(idade))

#-------------------------------------------------------outra forma de fazer--------------------------------------------
'''
from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

# Define a categoria com base na idade
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênior'
else:
    categoria = 'MASTER'

# Exibe o resultado num único print
print(f'Idade {idade} categoria {categoria}')
'''
#-----------------------------------------------------------------------------------------------------------------------


