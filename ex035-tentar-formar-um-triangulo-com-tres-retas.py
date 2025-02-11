#Desenvolva um programa que leia o cumprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

#r1 reta 1 azul
#r2 reta 2 laranja
#r3 reta 3 amarela

print('-='*20)
print('Analisador de Trinangulos')
print('-='*20)
r1 = float(input("Primeiro segmento (r1): "))
r2 = float(input("Segundo segmento (r2): "))
r3 = float(input("Terceiro segmento (r3): "))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo.")

#-----------------------------------------------------------------------------------------------------------------------
'''
# Desenvolva um programa que leia o comprimento de 3 retas
# e diga ao usuário se elas podem ou  segmento
# Solicitar entrada do usuário para as três retas
r1 = float(input("Digite o comprimento da primeira reta (r1): "))
r2 = float(input("Digite o comprimento da segunda reta (r2): "))
r3 = float(input("Digite o comprimento da terceira reta (r3): "))

# Verificar a condição da desigualdade triangular
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo.")
font:JB
'''
#-----------------------------------------------------------------------------------------------------------------------