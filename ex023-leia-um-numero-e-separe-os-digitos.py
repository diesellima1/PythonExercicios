#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
#fazer com matemática e com string

#-----------------------------------------------------------------------------------------------------------------------
#minha solução com unidades de milhar, centena, dezena e unidade
#12 não tem centena, então o resultado é 0
num = int(input('Informe um Número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#-----------------------------------------------------------------------------------------------------------------------

# minha solução matemáticamente
'''
num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
#font:ghc
'''
#-----------------------------------------------------------------------------------------------------------------------

#minha solução com string
'''
num = input("Digite um número de 0 a 9999: ")
print(f"Unidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
#fonte:ghc
'''

