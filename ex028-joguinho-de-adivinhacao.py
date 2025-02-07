#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever natela se o usuário venceu our perdeu !!!


#-----------------------------------------------Game-on!----------------------------------------------------------------

from random import randint #carrega a biblioteca random e importa a função randint que gera números aleatórios inteiros
from time import sleep # sleep é uma função que faz o computador esperar um tempo em segundos "processando"
computador = randint(0, 5) #faz o computador "pensar" "sortear" em um número inteiro entre 0 e 5
print('-=-' * 20)   #decoração superior
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)   #decoração inferior
jogador = int(input('Em que número eu pense? ')) #jogador tenta adivinhar
#-------------------------------------------------Processando-------------
print('PROCESSANDO.') #processando a resposta
sleep(1) #computador espera 5 segundos
print('PROCESSANDO..') #processando a resposta
sleep(1) #computador espera 5 segundos
print('PROCESSANDO...') #processando a resposta
sleep(1) #computador espera 5 segundos
#-------------------------------------------------Resultado----------------
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))


#-----------------------------------------------Fim do Programa---------------------------------------------------------

