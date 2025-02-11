#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

#exemplo: 3;7;5


#----------------------------------------------modo simples--------------------------------------------------------------

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))

#-----------------------------------------------------------------------------------------------------------------------