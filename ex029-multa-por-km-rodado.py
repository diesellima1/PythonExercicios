#Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80 km por hora mostra uma
# mensagem dizendo que ele foi multado a multa vai custar 7 BRL por cada quilômetro acima do limite

#se a velociadade for mair que 80 km/h, o motorista será multado


#if velocidade > 80:
#-----------------------------------------------boa viagem!-------------------------------------------------------------

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80: #condição simples
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7   #multa por km rodado
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
