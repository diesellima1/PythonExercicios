#Faça um programa que leia um número e mostre na tela a tabuada.


#Ver tabuada de um número!
numero = int(input("digite um número para ver a sua tabuada:"))
print('-' * 12) #replicando strings: Mostrar 12 tracinhos
print('{} x {:2} = {}'.format(numero, 1, numero * 1))         #"{} x {} = {}" é a estrutura da tabuada: "5 x 1 = 5"
print('{} x {:2} = {}'.format(numero, 2, numero * 2))
print('{} x {:2} = {}'.format(numero, 3, numero * 3))
print('{} x {:2} = {}'.format(numero, 4, numero * 4))
print('{} x {:2} = {}'.format(numero, 5, numero * 5))
print('{} x {:2} = {}'.format(numero, 6 ,numero * 6))
print('{} x {:2} = {}'.format(numero, 7 ,numero * 7))
print('{} x {:2} = {}'.format(numero, 8 ,numero * 8))
print('{} x {:2} = {}'.format(numero, 9 ,numero * 9))
print('{} x {:2} = {}'.format(numero, 10,numero * 10))        #{:2} duas casas para os caracteres se organizar
print('-' * 12) #replicando strings: Mostrar 12 tracinhos


'''
# Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada do número de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#font: GHC
'''