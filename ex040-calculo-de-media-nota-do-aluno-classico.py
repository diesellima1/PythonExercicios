#Crie um programa que leia 2 notas de um aluno e calcule sua média mostrando uma mensagem no final de
# acordo com a média atingida

#-Média abaixo de 5.0:
#Reprovado

#-Média entre 5.0 e 6.9:
#Recuperação

#-Média 7.0 ou superior:
#Aprovado


nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
resultado = (nota1 + nota2) / 2
if resultado < 5.0:
    print('\033[1;31mReprovado\033[0m: Média {}'.format(resultado)) #escrito em vermelho
elif resultado >= 5.0 and resultado <= 6.9:     #O resultado deve estar entre elas usa "and" ambas verdadeires "or"uma ou outra verdadeira
    print('\033[33mRecuperação\033[0m: Média {}'.format(resultado)) #escrito em amarelo
else:
    print('✔ \033[32mAprovado\033[0m: Média {}'.format(resultado)) #escrito em verde
    print("   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
    print("         ✨ PARABÉNS!!! ✨")
    print("   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")

