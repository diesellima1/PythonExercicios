#faça um programa  em  python que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele. use funções "is"
#função is testa os valores ex ", var.isalnum" teste islanum "é alphanumérico'
a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('E alfabetico?', a.isalpha())
print('É alphanumérico?', a.isalnum()) #adevilson123
print('Está em MAIÚSCULAS?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está Capitalizada?', a.istitle()) #Começa com uma letra maiúscula

#a é um objeto e todo objeto string tem um método








'''
# Solicita ao usuário que insira um valor
valor = input("Digite algo: ")


# Função para verificar e exibir informações sobre o valor
def verificar_valor(valor):
    print(f"Tipo primitivo: {type(valor)}")
    if valor.isnumeric():
        print("É um número.")
    else:
        print("Não é um número.")

    if valor.isalpha():
        print("É composto apenas por letras.")
    else:
        print("Não é composto apenas por letras.")

    if valor.isalnum():
        print("É alfanumérico.")
    else:
        print("Não é alfanumérico.")

    if valor.isupper():
        print("Está em maiúsculas.")
    else:
        print("Não está em maiúsculas.")

    if valor.islower():
        print("Está em minúsculas.")
    else:
        print("Não está em minúsculas.")

    if valor.isspace():
        print("É um espaço em branco.")
    else:
        print("Não é um espaço em branco.")

    if valor.isdigit():
        print("É um dígito.")
    else:
        print("Não é um dígito.")

    if valor.isdecimal():
        print("É um número decimal.")
    else:
        print("Não é um número decimal.")

    if valor.isidentifier():
        print("É um identificador válido.")
    else:
        print("Não é um identificador válido.")

    if valor.isprintable():
        print("É imprimível.")
    else:
        print("Não é imprimível.")

    if valor.istitle():
        print("Está capitalizado (title case).")
    else:
        print("Não está capitalizado (title case).")


# Chama a função para verificar o valor
verificar_valor(valor)
'''


'''
#   #FUnçao if
#faça um programa  em  python que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele.

# Solicita ao usuário que insira um valor
valor = input("Digite algo: ")

# Verifica e exibe o tipo primitivo do valor e outras informações
print("Tipo primitivo:", type(valor))

if valor.isnumeric():
    print("É um número.")
else:
    print("Não é um número.")

if valor.isalpha():
    print("É uma letra.")
else:
    print("Não é uma letra.")

if valor.isalnum():
    print("É alfanumérico.")
else:
    print("Não é alfanumérico.")

if valor.isupper():
    print("Está em maiúsculas.")
else:
    print("Não está em maiúsculas.")

if valor.islower():
    print("Está em minúsculas.")
else:
    print("Não está em minúsculas.")

if valor.isspace():
    print("É um espaço em branco.")
else:
    print("Não é um espaço em branco.")

if valor.isdigit():
    print("É um dígito.")
else:
    print("Não é um dígito.")

if valor.isdecimal():
    print("É um número decimal.")
else:
    print("Não é um número decimal.")
    
    font:copilot github
'''