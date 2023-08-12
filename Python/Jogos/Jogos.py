import Forca
import Adivinhacao

def escolha_jogo():
    print("=================================")
    print("======Escolha o seu Jogo!!=======")
    print("=================================")

    print("(1) FORCA  (2) ADIVINHAÇÃO")
    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogo Forca")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogo Adivinhação")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()
