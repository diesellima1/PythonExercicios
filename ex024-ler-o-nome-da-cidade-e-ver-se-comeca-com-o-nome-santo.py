#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


cid = str(input('Em que cidade você nasceu? ')).strip() #strip() remove os espaços inúteis no começo e no final
print(cid[0:5].upper() == 'SANTO')                    #[:5] pega os 5 primeiros caracteres da string e upper() deixa a string em maiúsculo

#"como programador preciso pensar se o úsuario vai fazr besteira na hora de digitar e na maioria das vezes ele vai fazer besteira"






#-----------------------------------------------------------------------------------------------------------------------
'''
#-----> Exercício 024 - Aula 9 - Manipulando Texto
cidade = input("Digite o nome de uma cidade: ").strip() #strip() remove os espaços antes e depois da string
print(cidade[:5].upper() == "SANTO")                    #[:5] pega os 5 primeiros caracteres da string
                                                        #upper() deixa a string em maiúsculo
                                                        #== "SANTO" compara se os 5 primeiros caracteres são iguais a "SANTO"
                                                        #e retorna True ou False
                                                        
'''
#fonte:ghc






