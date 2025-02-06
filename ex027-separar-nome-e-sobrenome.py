#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


n = str(input('Digite seu nome completo: ')).strip() #strip() remove os espaços inúteis no começo e no final
nome = n.split()    #split() separa a string em uma lista de strings
print('Muito prazer em te conhecer!')   #\n pula uma linha
print('Seu primeiro nome é {}'.format(nome[0])) #nome[0] pega o primeiro elemento da lista
print('Seu último nome é {}'.format(nome[len(nome)-1])) #nome[-1] pega o último elemento da lista









#-----------------------------------------------------------------------------------------------------------------------

'''
#-----> Exercício 027 - Aula 9 - Manipulando Texto
nome = input("Digite o nome completo: ").strip()  #strip() remove os espaços antes e depois da string
nome = nome.split()                               #split() separa a string em uma lista de strings
print(f"Primeiro nome: {nome[0]}")                #nome[0] pega o primeiro elemento da lista
print(f"Último nome: {nome[-1]}")                 #nome[-1] pega o último elemento da lista
#fonte:ghc
'''