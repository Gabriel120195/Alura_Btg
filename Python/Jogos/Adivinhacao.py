
import random

def jogar():
    print("=============---================")
    print("Bem vindo ao Jogo de adivinhação")
    print("================================")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print("Numero = " , numero_secreto)

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite seu chute:"))
        print("Você digitou:", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou! e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
             print("Você errou! o seu chute foi MAIOR do que o número secreto!")
            elif(menor):
                print("Você errou! o seu chute foi MENOR do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo!!!")

if(__name__ == "__main__"):
    jogar()