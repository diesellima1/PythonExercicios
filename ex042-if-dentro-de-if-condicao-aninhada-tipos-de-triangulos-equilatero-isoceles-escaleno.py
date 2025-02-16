#Refaço o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado

#Equilatero: todos os lados

#Isóceles:dois lados iguais

#Escaleno: todos os lados diferentes

#------------------------------------------------------if dentro de if--------------------------------------------------
#-----------------------------------------------------condição aninhada-------------------------------------------------


r1 = float(input('Primeiro segment: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulos!', end='')  #- `print("Texto", end='')` → Não adiciona uma nova linha (mantém o cursor na mesma linha).
    if r1 == r2 == r3: #não precisa usar and nessa condição o python permite dessa maneira
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1: #Se o que você quer é garantir que **todas as variáveis sejam diferentes entre si**, você deve checar cada condição diretamente, assim
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar triângulos')