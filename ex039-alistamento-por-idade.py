#Faça um programa que leia o ano de nascimento de um jovem informe de acordo com sua idade

#-Se ele ainda vai se a de estar ao serviço militar

#-Se é a hora de se alistar

#-Se já passou do tempo do alistamento

#Seu programa também deverá mostrar o campo que falta ou passou do prazo !



#------------------------------------------------Alistamento +18--------------------------------------------------------

# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade

# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento

# Seu programa também deverá mostrar o tempo que falta ou passou do prazo!

# ------------------------------------------------Alistamento +18 mais elaborado----------------------------------------
#--------------------------------------------frase criptografada para as mulheres!--------------------------------------

from datetime import date
import base64

# Mensagem criptografada usando UTF-8 e Base64
mensagem_criptografada = b"UXVlIHRhbCBsYXZhciBhIGxvdXNhIGUgZXN0ZW5kZXIgYSByb3VwYSBlcXVhbnRvIGlzc28/IEJyaW5jYWRlaXJhISDwn5iK"

while True:  # Loop para repetir o programa caso o usuário deseje
    # Solicita o gênero do usuário
    genero = input("Qual é o seu gênero? (M para masculino, F para feminino): ").strip().upper()

    if genero == 'M':
        # Para homens, segue a lógica do alistamento
        ano_nascimento = int(input("Digite o ano do seu nascimento: "))

        # Obtenha o ano atual
        ano_atual = date.today().year

        # Calcule a idade do usuário
        idade = ano_atual - ano_nascimento

        # Exibe a situação do alistamento militar
        print(f"\nQuem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")
        if idade < 18:
            tempo_restante = 18 - idade
            ano_alistamento = ano_atual + tempo_restante
            print("Você ainda vai se alistar ao serviço militar.")
            print(f"Faltam {tempo_restante} anos para seu alistamento, que será em {ano_alistamento}.")
        elif idade == 18:
            print("Você deve se alistar *IMEDIATAMENTE*!")
        else:
            tempo_excedente = idade - 18
            ano_alistamento = ano_atual - tempo_excedente
            print("Você já deveria ter se alistado.")
            print(f"Seu alistamento foi há {tempo_excedente} anos, em {ano_alistamento}.")
    elif genero == 'F':
        # Para mulheres, exibe a mensagem descriptografada
        mensagem_decodificada = base64.b64decode(mensagem_criptografada).decode('utf-8')
        print("Ah, você não precisa se alistar! 😊")
        print(mensagem_decodificada)
    else:
        # Caso o usuário digite algo inválido
        print("Gênero inválido. Tente novamente usando M ou F.")

    # Pergunta se deseja fazer um novo teste
    novo_teste = input("\nDeseja fazer um novo teste? (s/n): ").strip().lower()
    if novo_teste != 's':
        print("Encerrando o programa. Até a próxima!")
        break
#fonte:jb


# ------------------------------------------------Alistamento +18 simples ----------------------------------------------
'''
from datetime import date

# Leia o ano de nascimento do usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Calcule o ano atual e a idade
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Determine o status do alistamento
if idade < 18:
    print(f"Você tem {idade} anos. Você precisará se alistar em {18 - idade} anos.")
elif idade == 18:
    print(f"Você tem {idade} anos. É hora de se alistar!")
else:
    print(f"Você tem {idade} anos. Você deveria ter se alistado há {idade - 18} anos.")
#fonte:ghc
'''
# ----------------------------------Alistamento +18 obrigatorio para homens loop----------------------------------------
'''
from datetime import date

while True:
    # Leia o ano de nascimento e o gênero do usuário
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    genero = input("Digite o seu gênero (M para masculino, F para feminino): ").strip().upper()

    # Verifique o gênero
    if genero == 'F':
        print("Você é mulher. O teste de alistamento não se aplica. Por favor, Vai lavar a louça e estender as roupas.")
    else:
        # Calcule o ano atual e a idade
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento

        # Determine o status do alistamento
        if idade < 18:
            print(f"Você tem {idade} anos. Você precisará se alistar em {18 - idade} anos.")
        elif idade == 18:
            print(f"Você tem {idade} anos. É hora de se alistar!")
        else:
            print(f"Você tem {idade} anos. Você deveria ter se alistado há {idade - 18} anos.")

    # Pergunta se deseja fazer um novo teste
    novo_teste = input("Deseja fazer um novo teste? (s/n): ").strip().lower()
    if novo_teste != 's':
        print("Encerrando o programa. Até a próxima!")
        break
 '''
#-----------------------------------------------------------------------------------------------------------------------