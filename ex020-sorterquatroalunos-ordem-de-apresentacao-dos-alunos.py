#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

#função shuffle embaralha a lista randomicamente aleatorio

#-------------------------------------------------------------------------------------------------------------
'''
#importaçào complesta do random
import random
n1 = str(input ('Primenro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)   #comando para embaralhar a lista
print('A ordem de apresentação será: ')
print(lista)
'''
#-------------------------------------------------------------------------------------------------------------

#Importação específica do random
#não precisa de referencia ao modulo random antes de shuffle
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)  #comando para embaralhar a lista
print('A ordem de apresentação será: ')
print(lista)

#-------------------------------------------------------------------------------------------------------------
'''
import random

# Lê os nomes dos alunos
alunos = []
for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)

# Embaralha a lista de alunos
random.shuffle(alunos)

# Mostra a ordem sorteada
print("A ordem de apresentação será:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")
font:GHC
'''
#-------------------------------------------------------------------------------------------------------------
                                                     #DICAS
#-------------------------------------------------------------------------------------------------------------
'''
A função random é um módulo em Python que contém várias funções para gerar números aleatórios e realizar 
operações aleatórias. Algumas das funções mais comuns no módulo random incluem:  
random.random(): Retorna um número de ponto flutuante aleatório entre 0.0 e 1.0.
random.randint(a, b): Retorna um número inteiro aleatório entre a e b (inclusive).
random.choice(seq): Retorna um elemento aleatório de uma sequência (como uma lista).
random.shuffle(seq): Embaralha a sequência (como uma lista) no local.
random.sample(seq, k): Retorna uma lista de k elementos únicos escolhidos de uma sequência.
Aqui está um exemplo de como usar algumas dessas funções:

import random

# Gera um número de ponto flutuante aleatório entre 0.0 e 1.0
print(random.random())

# Gera um número inteiro aleatório entre 1 e 10
print(random.randint(1, 10))

# Escolhe um elemento aleatório de uma lista (sorteio)
lista = ['a', 'b', 'c', 'd']
print(random.choice(lista))

# Embaralha a lista
random.shuffle(lista)
print(lista)

# Retorna uma amostra de 2 elementos únicos da lista
print(random.sample(lista, 2))
'''