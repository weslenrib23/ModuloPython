import random

class JogoAdivinhacao:
    def __init__(self):
        self.limite_superior = 0
        self.numero_secreto = 0
        self.tentativas = 0
        self.max_tentativas = 0

    def iniciar_jogo(self):
        print("Bem-vindo ao jogo de adivinhação de números!\n")

        while True:
            self.limite_superior = int(input("Digite o limite superior para o intervalo de números: "))
            self.numero_secreto = random.randint(1, self.limite_superior)
            self.tentativas = 0
            self.max_tentativas = int(input("Digite o número máximo de tentativas: "))
            print(f"Estou pensando em um número entre 1 e {self.limite_superior}.\n")

            while self.tentativas < self.max_tentativas:
                palpite = int(input("Digite o seu palpite: "))
                self.tentativas += 1

                if palpite < self.numero_secreto:
                    print("\nTente um número maior!\n")
                elif palpite > self.numero_secreto:
                    print("\nTente um número menor!\n")
                else:
                    print(f"\nParabéns! Você acertou o número em {self.tentativas} tentativas!\n")
                    break

            if self.tentativas == self.max_tentativas:
                print(f"\nSuas {self.max_tentativas} tentativas acabaram! O número secreto era {self.numero_secreto}.\n")

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() != 's':
                print("\nObrigado por jogar! Até a próxima!\n")
                break

jogo = JogoAdivinhacao()
jogo.iniciar_jogo()
