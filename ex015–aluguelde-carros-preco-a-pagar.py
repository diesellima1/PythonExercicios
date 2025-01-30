#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#carro custa R$60 por dia e R$0,15 por Km rodado.

#preço a pagar
km_percorridos = int(input('Quantidade de Km percorridos?:'))
dias_alugado = float(input('Qual a quantidade de dias pelos quais ele foi alugado? Dias:'))
preco_apagar = dias_alugado * 60 + km_percorridos * 0.15
print('Total: -R${:.2f}'.format(preco_apagar))

