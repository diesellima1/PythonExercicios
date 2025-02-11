#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra "A"
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a última vez

#exercios 026
#forma 1
frase = str(input('Digite uma frase! ')).strip().upper() #strip() remove os espaços inúteis no começo e no final; str() converte o input para string; upper() deixa a string em maiúsculo
print('A letra A aparece {} vezes na frase'. format(frase.count('A'))) #count() conta quantas vezes a letra 'A' aparece na string
print('A primeira letra a apareceu na posição {}'.format(frase.find('A')+1)) #find() encontra a primeira ocorrência de um caractere +1 para não começar do 0
print('A última letra A apareceu na posição {}'.format((frase.rfind('A')+1))) #rfind lado esquerdo encontra a última ocorrência de um caractere +1 para não começar do 0



#-----------------------------------------------------------------------------------------------------------------------

#forma 2
'''
frase = input("Digite uma frase: ").strip().upper() #strip() remove os espaços antes e depois da string
print(f"A letra 'A' aparece {frase.count('A')} vezes.")     #count() conta quantas vezes a letra 'A' aparece na string
print(f"A primeira letra 'A' aparece na posição {frase.find('A')+1}.") #find() retorna a posição da primeira letra 'A' na string
print(f"A última letra 'A' aparece na posição {frase.rfind('A')+1}.") #rfind() retorna a posição da última letra 'A' na string
#fonte:ghc
'''


