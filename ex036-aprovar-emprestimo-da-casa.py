#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa o programa vai perguntar
# o valor da casa o salário do comprador e quantos anos ele vai pagar calcule o valor de cada prestação mensal
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado


#--------------------------------Forma mais complexa com loop ----------------------------------------------------------
'''
while True:  # Início do loop para permitir múltiplas simulações [1/2]
    # Solicita os dados do comprador
    casa = float(input('Qual o valor da casa? :R$'))
    salario = float(input('Qual o valor do salário do comprador :R$'))
    anos = int(input('Quantos anos de financiamento? :'))

    # Calcula a prestação mensal e o limite de 30% do salário
    meses = anos * 12  # Converte anos em meses
    prestacao_mensal = casa / meses
    limite = salario * 0.3  # 30% do salário

    # Verifica se a prestação é maior que o limite
    print(f'\nPara pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao_mensal:.2f}')
    if prestacao_mensal <= limite:
        print('Empréstimo pode ser \033[94mCONCEDIDO!🎉\033[0m')  #Exibe com letra azul
    else:
        print(
            'Empréstimo\033[91m NEGADO\033[0m! A prestação excede \033[91m30%\033[0m do salário.')  # Exibe com letra vermelha

    # Pergunta se deseja simular novamente [2/2]
    simular_novamente = input("\nDeseja simular novamente? (s/n): ").lower()
    if simular_novamente != 's':  # Se o usuário não digitar 's', termina o loop
        print("\nObrigado por simular! Até a próxima. 👋")
        break  # Sai do loop
'''

#--------------------------------outra forma mais simples de fazer------------------------------------------------------

casa = float(input('Valor da casa :R$'))
salario = float(input('Salário do comprador :R$'))
anos = int(input('Quantos anos de financianmento? :'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo \033[91mNEGADO\033[0m') #escrito em vermelho

#-----------------------------------------------------------------------------------------------------------------------