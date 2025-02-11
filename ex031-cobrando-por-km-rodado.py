#Desenvolva um programa que pergunte a distância de uma viagem em quilômetros calcule o preço da passagem cobrando
# 50 centavos por quilômetro para viagens até 200 km e
# 45 centavos para viagens mais longas


#------------------------------------------------calculo simplificado---------------------------------------------------
'''
distancia = float(input('Qual é a distância da sua viagem?:'))
print('Você está prestes a começar uma viagem de {}KM'.format(distancia))
preco = distancia * 0.50 if distancia <=200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
'''
#-------------------------------------------------calculo básico--------------------------------------------------------

distancia = float(input('Qual é a distância da viagem?: '))
print('Você está prestes a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

#-----------------------------------------------------------------------------------------------------------------------
