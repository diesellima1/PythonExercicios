#Crie um programa que leia um número Ral qualquer pelo teclado e mostre na tela a sua porção inteiro.



#importação Específica
'''
#importanto apénas a função trunk "para quebrar o número"
from math import trunc
from traceback import print_tb
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
'''


#importaçao sem a biblioteca
#nem sempre precisa importar modulos
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))


#Importação completa da biblioteca
'''
#importanto todo o modoluo moelo 1
import math
num  = float(input('Digite um valor:'))
print('O valor digitar foi {} e a sua porção interia é {}'.format(num, math.trunc(num)))
'''

'''
#importando todo o modulo modelo 2
import math
num_real = float(input('Digite um número com vírgula:'))
num_int = num = math.trunc(num_real)
print("O número {} tem a parte intera {}!".format(num_real, num_int))
'''