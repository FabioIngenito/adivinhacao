# Python built-in - São funções já disponíveis que não precisam ser importadas.
# O módulo random não está automaticamente disponível dentro do programa, só após importação.
import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random(1, 100)) # Número entre: 0.0 e 1,0
    numero_secreto = random.randrange(1, 101) # Número entre: 1 e 100
    total_de_tentativas = 0
    pontos = 1000
    # rodada = 1
    # print(numero_secreto)

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio e (3) Difícil")
    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1) :
        # String Interpolation
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (acertou):
            print("Você acertou fez {} pontos!".format(pontos))
            break
            # Para tudo. Não mostra a mensagem "Fim do Jogo"
            #exit();
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
        # rodada = rodada + 1

    print("Fim do jogo.")

if(__name__ == "__main__"):
    jogar()