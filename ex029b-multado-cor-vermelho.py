
# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
'''
# Print statement with "MULTADO" in red, "80km/h" in red, "verde" in green, and "amarelo" in yellow
print(f'{RED}MULTADO{RESET}! Você excedeu o limite permitido que é de {RED}80km/h{RESET}')
print(f'{GREEN}Dirija com cuidado: {RESET}')
print(f'{YELLOW}Boa Viagem!{RESET}')
'''


velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80: #condição simples
    print(f'{RED}MULTADO{RESET}! Você excedeu o limite permitido que é de {RED}80km/h{RESET}')
    multa = (velocidade - 80) * 7   #multa por km rodado
    print(f'{YELLOW}Você deve pagar uma multa de R$ {multa:.2f}{RESET}')
print(f'{GREEN}Tenha um bom dia! Dirija com segurança!{RESET}')
