import random

numero_secreto = random.randint(1,100)

print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = random.randint(1,100)
tentativas = 5
rodada = 1

while (rodada <= tentativas):
    print("tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite o seu número: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute > numero_secreto

    if (acertou):
        print("Você acertou. Parabéns!! :)")
        break
    elif (maior):
        print("Você errou. Seu chute foi maior :(")
    else:
        print("Você errou. Seu chute foi menor :(")

        rodada = rodada + 1

print("Fim do jogo")

