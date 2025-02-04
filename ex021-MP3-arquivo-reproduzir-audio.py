#copiar o arquivo clicar na pasta e colar o arquivo
# ele deve estar dentro da pasta do projeto
#pygame é uma biblioteca de jogos que pode ser usada para reproduzir arquivos de áudio

#copiar o arquivo clicar na pasta e colar o arquivo
# ele deve estar dentro da pasta do projeto
#pygame é uma biblioteca de jogos que pode ser usada para reproduzir arquivos de áudio
#https://www.pygame.org/news


#-------------------------------------------------------------------------------------------------------------

# importa a biblioteca pygame para instalar vai na lampada vermelha e instala o pygame
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Aguarda 100 milissegundos para evitar uso excessivo de CPU
#fonte:cp


#-------------------------------------------------------------------------------------------------------------

'''
#  DESATUALIZO NÃO FUNCIONA MAIS
import pygame #importa a biblioteca pygame
pygame.init() #inicializa o pygame
pygame.mixer.music.load('ex021.mp3') #carrega o arquivo de áudio
pygame.mixer.music.play() #reproduz o áudio
pygame.event.wait() #espera o fim do áudio
'''

#-------------------------------------------------------------------------------------------------------------

'''
import pygame
import time

# Initialize pygame
pygame.init()

# Try to load and play the audio file
try:
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    print("Playing audio...")

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)
except pygame.error as e:
    print(f"Error loading or playing audio: {e}")
#fonte:ghc
'''

