# Jogo da adivinhação

# Neste jogo, o computador vai
# escolher um número aleatório e o
# jogador deve tentar adivinhar qual é
# esse número.

# O computador irá fornecer dicas
# dizendo se o palpite do jogador
# está acima ou abaixo do número
# correto.

# Proposta

# Melhorias na versão inicial do jogo:

# - Adicionar limite máximo de
# tentativas

# - Permitir que o jogador escolha o
# intervalo de números

# - Incluir uma opção para o jogador
# jogar novamente ou sair do jogo
# após acertar ou esgotar todas as
# tentativas.

import random

def adivinhacao():
    print("Bem-vindo ao jogo de adivinhação de números!\n")

    while True:
        limite_superior = int(input("Digite o limite superior para o intervalo de números: "))
        numero_secreto = random.randint(1, limite_superior)
        tentativas = 0
        max_tentativas = int(input("Digite o número máximo de tentativas: "))
        print(f"Estou pensando em um número entre 1 e {limite_superior}.\n")

        while tentativas < max_tentativas:
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("\nTente um número maior!\n")
            elif palpite > numero_secreto:
                print("\nTente um número menor!\n")
            else:
                print(f"\nParabéns! Você acertou o número em {tentativas} tentativas!\n")
                break

        if tentativas == max_tentativas:
            print(f"\nSuas {max_tentativas} tentativas acabaram! O número secreto era {numero_secreto}.\n")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print("\nObrigado por jogar! Até a próxima!\n")
            break

adivinhacao()
