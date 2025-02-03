#Um professor quer sortear um dos seus alunos para pagar o quadro faça o programa que ajude ele,
# lendo o nome deles escrevendo o nome do escolhido.
#O módulo random em Python é uma ferramenta poderosa para gerar números aleatórios e fazer escolhas aleatórias.

#importar randarizador de elementos:
'''
import random
name1= input('Primeiro aluno:')
name2= input('Segundo aluno:')
name3= input('Terceiro aluno:')
name4= input('Quarto aluno:')
lista = [name1, name2, name3, name4]
escolhido = random.choice(lista)    #choice: "escolha" ou seja uma escolha dentro da lista!
print('O aluno escolhido foi {} \n Parabéns {} !!!'.format(escolhido, escolhido))
'''

#-------------------------------------------------------------------------------------------------------------

#importaçao especifíca
from random import choice
name1= input('Primeiro aluno:')
name2= input('Segundo aluno:')
name3= input('Terceiro aluno:')
name4= input('Quarto aluno:')
lista = [name1, name2, name3, name4]
escolhido = choice(lista)    #choice: "escolha" ou seja uma escolha dentro da lista!
print('O aluno escolhido foi {} \n Parabéns {} !!!'.format(escolhido, escolhido))

#aqui não precisa referencia o modulo random.antes de choice mas ele funciona igual