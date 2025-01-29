#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
 #pinta uma área de 2m quadradados

largura = float(input('Largura da parede?'))
altura = float(input('Altura da parede?'))
area = altura * largura
litros_tinta = area / 2

print('sua parede tem a dimensão de {} x {} e sua área é de {}m\u00B2 \nPara pintar essa parede, você precisa de {}l de tinta'.format(largura, altura, area, litros_tinta))
#u00B2 significa dois elevado "m²"