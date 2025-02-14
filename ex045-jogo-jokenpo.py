#Crie um programa que faça o computador jogar jokenpô com você.

#pedra/papel/tesoura


import random  # Para gerar a jogada do computador
import time  # Para criar pausas e melhorar a experiência


def apresentar_instrucoes():
    print("🎮 Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    time.sleep(1)

    print("\n📜 Regras do jogo:")
    time.sleep(1)
    print("1️⃣ Você deve escolher entre Pedra, Papel ou Tesoura.")
    print("2️⃣ As escolhas têm as seguintes interações:")
    print("   ✊ Pedra quebra Tesoura 🗿")
    print("   ✋ Papel embrulha Pedra 📄")
    print("   ✌️ Tesoura corta Papel ✂️")
    time.sleep(1)
    print("\n🔄 Se os dois escolherem a mesma opção, é um EMPATE!")
    time.sleep(1)

    print("\n👊 Agora é a sua vez de jogar! Faça sua escolha:")
    print("Digite:")
    print(" [ 1 ] para Pedra ✊")
    print(" [ 2 ] para Papel ✋")
    print(" [ 3 ] para Tesoura ✌️")
    time.sleep(1)


# Função principal do jogo
def jogar():
    apresentar_instrucoes()  # Exibe as instruções

    # Jogador faz sua escolha
    try:
        escolha_jogador = int(input("\nQual é a sua jogada? "))
        if escolha_jogador not in [1, 2, 3]:
            print("❌ Escolha inválida! Escolha 1, 2 ou 3.")
            return

        # Nome das escolhas correspondentes
        opcoes = {1: "Pedra ✊", 2: "Papel ✋", 3: "Tesoura ✌️"}
        print(f"\nVocê escolheu: {opcoes[escolha_jogador]}")

        # Computador faz uma escolha aleatória
        escolha_computador = random.randint(1, 3)
        print(f"Computador escolheu: {opcoes[escolha_computador]}")

        # Regra para determinar o vencedor
        if escolha_jogador == escolha_computador:
            print("\n\033[94m🤝 Empate!\033[0m")
        elif (escolha_jogador == 1 and escolha_computador == 3) or \
                (escolha_jogador == 2 and escolha_computador == 1) or \
                (escolha_jogador == 3 and escolha_computador == 2):
            print("\n\033[92m🎉 Parabéns, você venceu!\033[0m")
        else:
            print("\n\033[91m💻 O computador venceu! Tente novamente.\033[0m")

    except ValueError:
        print("❌ Escolha inválida! Por favor, insira um número inteiro (1, 2 ou 3).")


# Executa o jogo
jogar()



