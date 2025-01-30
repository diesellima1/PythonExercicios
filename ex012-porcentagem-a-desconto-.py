# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto!


#   FORMULA DA PORCENTAGEM  "VALOR * DESCONTO / 100"
#EXEMPLO_CALCULO 10*5/100 ==5 AGORA PASTA SUBTRAIR 5 DO VALOR TOTAL DO PRODUTO

#calculo de múltiplos descontos
produto = float(input('Qual o preço do produto? R$'))
desconto = float(input("Qual a porcentagem do desconto?"))
calculo = produto * (desconto / 100) #PARENTES PARA FICAR NA ORDEM
total = produto - calculo
print('Valor original  R${:.2f} \n {:.0f}% valor do desconto R${:.2f} \ntotal com desconto R${:.2f}'.format(produto, desconto, calculo, total))