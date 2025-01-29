#Crie um programa que leia quanto dinheiro uma pessao tem na carteira e mostre quantos dólares ela
#pode comprar
#considere U$$1,00 = R$3,27
# dolár hoje 29/01/2025 U$$1,00 = R$5,84

reais = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolares = reais / 3.27
dolares_2025 = reais / 5.84
euro = reais / 6.11
bitcoins = reais / 604631.48
print('Com R${:.2f} você pode comprar U$${:.2f} \n No futuro de 29/01/2025 vai poder compar U$${:.2f}'.format(reais, dolares, dolares_2025 )) #U$${:.2f} f"flutuante" números com pontos
print('Euros €{:.2f}'.format(euro ))
print('Bitcoins: BTC {:.8f}'.format(bitcoins))