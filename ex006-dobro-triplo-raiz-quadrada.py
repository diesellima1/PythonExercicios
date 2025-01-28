#crie um algoritimo que leia um número e mostre a seu dobro, triplo e a raiz quadrada

import math #O módulo math é muito útil quando você precisa realizar operações matemáticas
numero = float(input("Digite um Número:"))
dobro = numero *2
triplo = numero *3
raiz_quadrada = math.sqrt(numero)
print('o Dobro é {} o Triplo é {} e a Raiz Quadrada é {:.3}'.format(dobro,triplo,raiz_quadrada))
#:.3 limita caracteras

'''
#outro modelo mais simples de raiz quadrada
# Recebe um número do usuário
numero = float(input("Digite um número: "))

# Calcula a raiz quadrada do número
raiz_quadrada = numero ** 0.5

# Exibe o resultado
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
'''