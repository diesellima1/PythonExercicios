#crie um algoritimo que leia um número e mostre a seu dobro, triplo e a raiz quadrada
'''
import math #O módulo math é muito útil quando você precisa realizar operações matemáticas
numero = float(input("Digite um Número:"))
dobro = numero *2
triplo = numero *3
raiz_quadrada = math.sqrt(numero)
print('o Dobro é {} o Triplo é {} e a Raiz Quadrada é {:.3}'.format(dobro,triplo,raiz_quadrada))
#:.3 limita caracteras
'''

'''
n = int(input('Digite um valor:'))
d = n * 2
t = n * 3
r = n ** (1/2)    #RAIZ QUADRADA também pode usar pow()
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))
'''
#outra maneira de fazer a mesma coisa
n = int(input('Digite um valor:'))
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n,(n*3), n, (n**(1/2))))

'''
#outro modelo mais simples de raiz quadrada
# Recebe um número do usuário
numero = float(input("Digite um número: "))

# Calcula a raiz quadrada do número
raiz_quadrada = numero ** 0.5

# Exibe o resultado
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
'''