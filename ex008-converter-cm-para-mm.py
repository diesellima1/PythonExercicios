#escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros


medida = float(input("Digite uma distância em Metros:"))
cm = medida *100
mm = medida *1000
#decâmetro →
dam = medida * 10
#decímetro →
dm = medida / 10
#hectômetro →
hm = medida / 100
#polegadas''
pol = medida * 39.3701
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm \n{}dam \n{}dm \n{}hm \n{}"'.format(medida, cm, mm, dam, dm, hm, pol))








'''
# cálculo básico
metros = float(input("digite o valor em metros "))
centimetros = metros * 100
milimitros = metros * 1000
polegadas = metros * 39,3701
print("A distância de {}m \n {}cm \n {}mil \n {}pol".format(metros, centimetros, milimitros, polegadas))
'''