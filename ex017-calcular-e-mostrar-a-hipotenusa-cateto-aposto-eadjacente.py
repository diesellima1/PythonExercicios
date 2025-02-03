#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa


#como calcula o quadrado da hytonesusa?
#Para calcular o quadrado da hipotenusa, você pode usar o famoso Teorema de Pitágoras, que diz que,
#em um triângulo retângulo, o quadrado da hipotenusa (o lado oposto ao ângulo reto) é igual à soma dos
#quadrados dos outros dois lados. Matematicamente, é representado assim: c²=a²+b²
#hipotenusa é a soma da raiz quadrada dos catetos
#-------------------------------------------------------------------------------------------------------------

#importando modulo math com toda a biblioteca "Assim é mais fácil"
'''
import math
co = float(input('Comprimento do Cateto Oposto(co): '))
ca = float(input('Comprimento do Cateto Adjacente(ca): '))
hi = math.hypot(co, ca) #math.hypot calcula a hypotenusa   #referenciar o modulo math. "math.hypot"
print('A hipotenusa(hi) vai medir: {:.2f}'.format(hi))
'''

#importando apenas o  modulo específico da biblioteca "pesa menos no código"

from math import hypot
co = float(input('Comprimento do Cateto Oposto(co): '))
ca = float(input('Comprimento do Cateto Adjacente(ca): '))
hi = hypot(co, ca) #math.hypot calcula a hypotenusa # math. "não precisa mas funciona junto"
print('A hipotenusa(hi) vai medir: {:.2f}'.format(hi))

#-------------------------------------------------------------------------------------------------------------

#sem importação de modulo forma tradicional (mais difícil de fazer)
'''
co = float(input('Comprimento do Cateto Oposto(co): '))
ca = float(input('Comprimento do Cateto Adjacente(ca): '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa(hi) vai medir {:.2f}'.format(hi))
'''

#-------------------------------------------------------------------------------------------------------------

# Outra forma de inportar
'''
import math
# Ler o comprimento do cateto oposto
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

# Ler o comprimento do cateto adjacente
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcular o comprimento da hipotenusa
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)  #sqrt"Raiz quadrada"

# Mostrar o comprimento da hipotenusa
print(f"O comprimento da hipotenusa é {hipotenusa}.")
'''
