#Faça um programa que ligue o ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo
#O seno, cosseno e tangente são funções trigonométricas usadas para relacionar os ângulos de um
# triângulo retângulo com o comprimento de seus lados.

#Seno (sin)"eixo vertical": em um triângulo retângulo, é a razão entre o comprimento do cateto oposto ao ângulo e o
# comprimento da hipotenusa.

#Cosseno (cos)"eixo horizontal": é a razão entre o comprimento do cateto adjacente ao ângulo e o comprimento da hipotenusa.

#Tangente (tan) "é uma linha imaginaria que vai passar tangenciando o ponto escolhido : é a razão entre o comprimento
# do cateto oposto ao ângulo e o comprimento do cateto adjacente.

#-------------------------------------------------------------------------------------------------------------

#importação completa do modulo
'''
import math
#an
angulo = float(input('Digite o ângulo(an) que você deseja?: '))
sin = math.sin(math.radians(angulo)) #sin é o seno
print('O ângulo de {}  tem o SENO(sin) de {:.2f}'.format(angulo, sin))
#COS
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO(cos) de {:.2f}'.format(angulo, cosseno))
#tan
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE(tan) de {:.2f}'.format(angulo, tangente))
'''

# ler o manual pois o medida aqui precisa ser convertida para radianos e nos estamos em graus
# conversor: "math.radians"

#-------------------------------------------------------------------------------------------------------------

#importação especifíca do modulo
from math import radians, sin, cos, tan #importação de mais de uma função separados por virgula
#an
angulo = float(input('Digite o ângulo(an) que você deseja?: '))
sin = sin(radians(angulo)) #sin é o seno
print('O ângulo de {}  tem o SENO(sin) de {:.2f}'.format(angulo, sin))
#COS
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO(cos) de {:.2f}'.format(angulo, cosseno))
#tan
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE(tan) de {:.2f}'.format(angulo, tangente))

#nesse caso não precisa referenciar "math."

#-------------------------------------------------------------------------------------------------------------

#outra forma de fazer
'''
import math
# Ler um ângulo em graus
angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Converter o ângulo para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcular o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostrar os valores na tela
print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
'''

#tipos de importações!!!
#math.radians(): Converte um ângulo em graus para radianos. Funções trigonométricas em
# Python trabalham com radianos, então precisamos converter graus para radianos antes de
# calcular o seno, cosseno e tangente.

#math.sin(): Calcula o seno de um ângulo em radianos.

#math.cos(): Calcula o cosseno de um ângulo em radianos.

#math.tan(): Calcula a tangente de um ângulo em radianos.

#-------------------------------------------------------------------------------------------------------------