'''
Aqui está o passo a passo **detalhado** para você transformar o texto em um programa funcional de geração de CPF
em Python. As instruções seguem uma ordem lógica para que você implemente o programa por partes, explorando os conceitos mencionados.
### **Instruções para criar o programa de Gerador de CPF**
1. **Importar bibliotecas necessárias**
    - Use o `random` para gerar números aleatórios.
    - A biblioteca `os` pode ser usada, caso queira implementar funcionalidades adicionais (como limpar o terminal).
``` python
import random
```
1. **Geração dos 9 primeiros dígitos aleatórios**
    - Crie uma função chamada `gerar_cpf()`.
    - Nessa função, use `random.randint(0, 9)` para gerar 9 números aleatórios e armazená-los em uma lista.
    - Use uma **list comprehension** ou um `for` para preencher os 9 primeiros dígitos.
``` python
nove_digitos = [random.randint(0, 9) for _ in range(9)]
```
1. **Cálculo do primeiro dígito verificador (módulo 11)**
    - Calcule o **1º dígito verificador** com a fórmula de módulo 11:
        - Multiplique cada um dos 9 dígitos pelos pesos (de 10 a 2, em ordem decrescente).
        - Some os resultados.
        - Multiplique o resultado por 10 e calcule o resto da divisão por 11.
        - Se o resto for maior que 9, o dígito será zero (`0`).

    - Adicione o **1º dígito verificador** à lista dos números gerados anteriormente.
``` python
soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(10, 1, -1)))
primeiro_digito = (soma * 10 % 11) % 10
nove_digitos.append(primeiro_digito)
```
1. **Cálculo do segundo dígito verificador (módulo 11)**
    - Inclua o **primeiro dígito verificador** no cálculo do **segundo dígito**:
        - Reutilize a fórmula do módulo 11, mas agora use os **10 primeiros números** (incluindo o
        1º dígito verificador) e os pesos de 11 a 2.

    - Adicione o **2º dígito verificador** à lista.
``` python
soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(11, 1, -1)))
segundo_digito = (soma * 10 % 11) % 10
nove_digitos.append(segundo_digito)
```
1. **Formatação do CPF no padrão `XXX.XXX.XXX-XX`**
    - Utilize `str.format` para exibir o CPF final no formato correto.
    - Separe os 9 números em blocos de três e adicione os dígitos verificadores no final.
``` python
cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*nove_digitos)
```
1. **Criação de uma interface simples no terminal**
    - Crie uma função `main()` para exibir um menu com duas opções:
        - Gerar CPF.
        - Sair do programa.

    - Use um **loop-while** para que o usuário possa gerar CPFs repetidamente.
    - Adicione verificação de entrada (para aceitar apenas as opções `1` e `2`).
``` python
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Gerar CPF")
        print("2 - Sair")
        opcao = input("Digite sua escolha: ").strip()
        if opcao == "1":
            print(f"🆕 CPF Gerado: {gerar_cpf()}")
        elif opcao == "2":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
```
1. **Montagem do programa final**
    - Agora, combine as funções para criar o programa completo.
    - Ele deve começar executando a função `main()`.
``` python
if __name__ == "__main__":
    main()
```
### Programa completo final (seguindo as instruções acima)
``` python
import random


def gerar_cpf():
    nove_digitos = [random.randint(0, 9) for _ in range(9)]

    # Primeiro dígito verificador
    soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(10, 1, -1)))
    primeiro_digito = (soma * 10 % 11) % 10
    nove_digitos.append(primeiro_digito)

    # Segundo dígito verificador
    soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(11, 1, -1)))
    segundo_digito = (soma * 10 % 11) % 10
    nove_digitos.append(segundo_digito)

    # Formatação do CPF
    return "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*nove_digitos)


def main():
    print("🔢 Bem-vindo ao Gerador de CPF 🔢")
    while True:
        print("\nEscolha uma opção:")
        print("1 - Gerar CPF")
        print("2 - Sair")
        opcao = input("Digite sua escolha: ").strip()

        if opcao == "1":
            print(f"🆕 CPF Gerado: {gerar_cpf()}")
        elif opcao == "2":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
```
Com essas instruções, você pode facilmente criar o programa, explorando as partes principais como o cálculo dos
dígitos verificadores e a interface no terminal. É simples de entender, mas utiliza conceitos importantes como:
- Manipulação de listas.
- Estruturas de repetição e entrada do usuário.
- Regras de validação real (módulo 11).

'''





#---------------------------------------------------Gerador de cpf------------------------------------------------------

import random

def gerar_cpf():
    """
    Gera um CPF válido formatado no padrão XXX.XXX.XXX-XX.
    """
    # Gerar os 9 primeiros dígitos aleatórios
    nove_digitos = [random.randint(0, 9) for _ in range(9)]

    # Calcular o primeiro dígito verificador
    soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(10, 1, -1)))
    primeiro_digito = (soma * 10 % 11) % 10

    # Adicionar o primeiro dígito verificador no final
    nove_digitos.append(primeiro_digito)

    # Calcular o segundo dígito verificador
    soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(11, 1, -1)))
    segundo_digito = (soma * 10 % 11) % 10

    # Adicionar o segundo dígito ao CPF
    nove_digitos.append(segundo_digito)

    # Formatar o CPF no padrão XXX.XXX.XXX-XX
    cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*nove_digitos)

    return cpf_formatado


def main():
    """
    Interface simples no terminal para gerar CPF ou sair do programa.
    """
    print("🔢 Bem-vindo ao Gerador de CPF em Python! 🔢")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Gerar CPF")
        print("2 - Sair")
        opcao = input("Digite sua escolha: ").strip()

        if opcao == "1":
            cpf = gerar_cpf()
            print(f"🆕 CPF Gerado: {cpf}")
        elif opcao == "2":
            print("Encerrando o programa. Até logo! 👋")
            break
        else:
            print("❌ Opção inválida. Por favor, digite 1 ou 2.")


if __name__ == "__main__":
    main()

    print("  _____ ")
    print(" /     \\")
    print("| () () |")
    print(" \\  ^  /")
    print("  ||||| ")
    print("  ||||| ")
    print("   ||   ")
    print("  /||\\  ")
    print(" / || \\ ")
    print("/  ||  \\")
    print("   ||   ")
    print("  /  \\  ")
    print(" /    \\ ")
    print("/      \\")
    print("Goodbye! 👋")
    

#---------------------------------------------------versão reduzida ----------------------------------------------------
'''
import random


def gerar_cpf():
    nove_digitos = [random.randint(0, 9) for _ in range(9)]
    for _ in range(2):
        soma = sum(valor * peso for valor, peso in zip(nove_digitos, range(len(nove_digitos) + 1, 1, -1)))
        nove_digitos.append((soma * 10 % 11) % 10)
    return "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*nove_digitos)


print(f"CPF Gerado: {gerar_cpf()}")
'''

#-----------------------------------------------------------------------------------------------------------------------