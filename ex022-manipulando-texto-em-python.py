#-----> Exercício 022 - Aula 9 - Manipulando Texto

#cadeia de texto é uma string, toda cadeia de texto esta em aspas duplas ou simples!

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas
#- O nome com todas as letras minúsculas
#- Quantas letras ao todo (sem considerar espaços)
#- Quantas letras tem o primeiro nome


#-----------------------------------------------------------------------------------------------------------------------

nome = str(input('Digite seu nome completo: ')).strip() #strip() remove os espaços inúteis no começo e no final
print('Analisando seu nome...') #\n pula uma linha
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))  #upper() deixa todas as letras em maiúsculas
print('Seu nome em minúsculas é: {}'.format(nome.lower()))  #lower() deixa todas as letras em minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #len() conta o tamanho da string
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #find() encontra a primeira ocorrência de um caractere


#-----------------------------------------------------------------------------------------------------------------------
#OUTRA FORMA DE RESOLVER O MESMO EXERCÍCIO
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#-----------------------------------------------------------------------------------------------------------------------

