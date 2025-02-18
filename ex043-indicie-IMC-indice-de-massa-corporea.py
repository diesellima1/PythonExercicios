# Desenvolvo uma lógica que leia o peso e a altura de uma pessoa calcule seu IMC e mostre seu
# status de acordo com a tabela abaixo:

# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

# dividindo o peso em quilos pela altura em metros ao quadrado.
# Por exemplo, se uma pessoa pesa 70 kg e mede 1,60 m, seu IMC será:
# IMC = 70 Kg/ (1,60)² = 70/ 2,56 = 27,3



# -------------------------------------------------------loop 1/2--------------------------------------------------------
while True:  # Loop para repetir os cálculos enquanto o usuário quiser
    # ----------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------Código----------------------------------------------------------
    # Lê o peso e altura do usuário
    peso = float(input('Qual o peso (em kg)? : '))
    altura = float(input('Qual a altura (em metros)? : '))

    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Exibe o valor do IMC formatado com duas casas decimais
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))

    # Determina o status baseado no IMC
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Peso Ideal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    elif 30 <= imc < 40:
        print('Obesidade')
    else:
        print('Obesidade Mórbida')
        # Adiciona restrição para não permitir entrada no avião
        print('Thais Carla infelizmente, sua entrada no avião será negada por questões de segurança.')
        # Sai do programa, pois não será permitido continuar
        novo_calculo = input('Deseja tentar novamente? (s/n): ').strip().lower()
        if novo_calculo != 's':
            print('Encerrando o programa. Até mais!')
            break
        continue

    # -------------------------------------------------------loop 2/2---------------------------------------------------
    # Verifica se deseja realizar outro cálculo
    novo_calculo = input('Deseja fazer um novo cálculo? (s/n): ').strip().lower()
    if novo_calculo != 's':  # Sai do loop se a resposta não for 's'
        print('Encerrando o programa. Até mais!')
        break
    # ------------------------------------------------------------------------------------------------------------------
