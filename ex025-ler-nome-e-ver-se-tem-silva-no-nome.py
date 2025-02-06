#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.



nome = str(input(('Qual é o seu nome completo? '))).strip().upper() #strip() remove os espaços inúteis no começo e no final; str() converte o input para string; upper() deixa a string em maiúsculo
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) #in verifica se "SILVA" está na string nome


#-----------------------------------------------------------------------------------------------------------------------

'''
#forma 2
nome = input("Digite o nome completo: ").strip().upper() #strip() remove os espaços antes e depois da string
print("SILVA" in nome.split())  #split() separa a string em uma lista de palavras in verifica se "SILVA" está na lista
#fonte:ghc
'''