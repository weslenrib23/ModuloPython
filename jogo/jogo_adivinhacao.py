import random

def adivinhacao():
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de números!\n")
    print("Estou pensando em um número entre 1 e 100.\n")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("\nTente um número maior!\n")
        elif palpite > numero_secreto:
            print("\nTente um número menor!\n")
        else:
            print(f"\nParabéns! Você acertou o número em {tentativas} tentativas!")
            break

adivinhacao()