# Faça um programa que leia um ano qualquer e mostre se ele é BISSESTO
# 1700 não é bissexto
# 2017 É BISSEXTO?
# Se o ano é dividido por 4 ele é BISSEXTO
# exceto anos múltiplos de 100 que não são múltiplos de 400: and ano % 100 != 0 or ano % 400 == 0:

# --------------------------------------ver anos simples-----------------------------------------------------------------
'''
ano = int(input('Que ano você quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
'''

# -------------------------------------importar ano atual do computador do usuário---------------------------------------

from datetime import date  # A importação deve sempre ficar no topo do script.

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
#importar data atual
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

# -----------------------------------------------------------------------------------------------------------------------

'''
### Como funciona:
1. **`ano % 4 == 0`**: Verifica se o ano é divisível por 4.
2. **`ano % 100 != 0`**: Verifica se o ano **não é** divisível por 100. (Porque anos múltiplos de 100 não são bissextos, a menos que sejam múltiplos de 400.)
3. **`ano % 400 == 0`**: Uma exceção é quando o ano é também divisível por 400.

Exemplo de saídas:
- Se você digitar 2020, ele dirá que **é bissexto**.
- Se você digitar 2017, ele dirá que **não é bissexto**.
'''
# -----------------------------------------------------------------------
'''
ano = int(input('Que ano você quer analisar'))
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Que ano você quer analisar? '))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é bissexto.')
'''
# -----------------------------------------------------------------------------------------------------------------------
