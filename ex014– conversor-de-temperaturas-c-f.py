#Conversor de Temperaturas de Fahrenheit Celsius


#-------------------------------
#Fórmula: °C para°F
#(33 °C × 9/5) + 32 = 92,84 °F
#-------------------------------
#Fórmula: °F para °C
#(33,8 °F − 32) × 5/9 = 1 °C
#-------------------------------


#converter a temperatura °C para°F
cel = float(input('Informe a temperatura em °C:'))
calculo = (cel * 9/5) + 32
print('a temperatura de {}°C corresponde a {}°F'.format(cel, calculo))




