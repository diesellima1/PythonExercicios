'''
    #Operadores Aritméticos em Python:
+ : Adição

- : Subtração

* : Multiplicação

/ : Divisão

% : Módulo (resto da divisão)

** : Exponenciação

// : Divisão inteira
------------------------------------------------------------------------------------
    #Ordem de Precedência:
A ordem de precedência dos operadores determina a sequência em que as operações são realizadas. Em Python, a ordem de precedência dos operadores aritméticos, do mais alto para o mais baixo, é:

** (Exponenciação)

*, /, //, % (Multiplicação, Divisão, Divisão inteira, Módulo)

+, - (Adição, Subtração)
------------------------------------------------------------------------------------

    #Exemplos:
3*5+4**2==31
---
3*(5+4)**2==243
---
result = 2 + 3 * 4 ** 2 / 8 - 5
Neste exemplo, as operações são realizadas na seguinte ordem:

4 ** 2 (Exponenciação: 16)

3 * 16 (Multiplicação: 48)

48 / 8 (Divisão: 6)

2 + 6 (Adição: 8)

8 - 5 (Subtração: 3)

Portanto, result será 3.
------------------------------------------------------------------------------------
'''

#soma simplis
'''
n1 = int(input('Um valor:'))
n2 = int(input('Outro Valor:'))
print("Asoma  vale {}".format(n1+n2))
'''

'''
#soma composta
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2     #divisão
di = n1 / n2    #divisão inteira
e= n1 ** n2    #elevado
#print('A soma é {}, o produto é {} e a divisão é {}'.format(s,m,d))
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='>>>')
#end não quebra a linha
#:.3f "limitador de caracteres
#:\n "cria nova linha
#end'>>>' : "pode ser preenchido com qualquer coisa >>>"
'''
#-----------------------------------------------------------------------------------------------------------------------
#Desenvolva um program que leia as duas notas de um aluno, calcúle e mostre a sua média
'''
nota1 = float(input('Digite Sua Nota:'))
nota2 = float(input('Digite Outra Nota:'))
resultado = nota1 + nota2
media = resultado / 2
print("total de pontos {} sua Média é de {} Pontos".format(resultado,media))
'''
#Arendondo a nota {:.1}
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
média = (n1 + n2) / 2 # se não colocar os parenteses o codigo vai rodar mas o resultado vai ser errado, pois ele tem que usar a ordem de precedencia
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média)) #pytohon aceita acentos na var

