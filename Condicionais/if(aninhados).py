#curso em vídeo#12#17:13
#desafio 036
import random

#valorCasa = int(input("Valor da casa:\n"))
#salarioComprador = float(input("Seu salário:\n"))
#tempoAnos = int(input("Em quantos anos quer pagar?\n"))
#prestacao = valorCasa / (tempoAnos * 12)
#limiteEmprestimo = salarioComprador * (30/100)
#if prestacao > limiteEmprestimo:
#    print("Emprestimo negado");
#else:
#    print("Emprestimo aprovado")

#jogo pedra papel tesoura
a = 0
placarpc = 0
placarjogador = 0
while a < 5:
    jogadorHumano = input("Escolha: pedra, papel ou tesoura?\n")
    pc = ["pedra","papel","tesoura"]
    elemento = random.choice(pc)

    if jogadorHumano == "pedra" and elemento == "pedra":
        print(f"EMPATE, o pc jogou {elemento}")
    elif jogadorHumano == "papel" and elemento == "papel":
        print(f"EMPATE, o pc jogou {elemento}")
    elif jogadorHumano == "tesoura" and elemento == "tesoura":
        print(f"EMPATE, o pc jogou {elemento}")
    else:
        if jogadorHumano == "pedra" and elemento == "papel":
            print(f"Você PERDEU!\nO computador jogou {elemento}")
            placarpc = placarpc + 1
        elif jogadorHumano == "pedra" and elemento == "tesoura":
            print(f"EEEE...Você GANHOU!\nO computador jogou {elemento}")
            placarjogador = placarjogador + 1
        elif jogadorHumano == "tesoura" and elemento == "pedra":
            print(f"Você PERDEU, o computador jogou {elemento}!")
            placarpc = placarpc + 1
        elif jogadorHumano == "tesoura" and elemento == "papel":
            print(f"EEEE...Você GANHOU!\nO computador jogou {elemento}")
            placarjogador = placarjogador + 1
        elif jogadorHumano == "papel" and elemento == "pedra":
            print(f"EEEE...Você GANHOU!\nO computador jogou {elemento}")
            placarjogador = placarjogador + 1
        elif jogadorHumano == "papel" and elemento == "tesoura":
            print(f"Você PERDEU!\nO computador jogou {elemento}")
            placarpc = placarpc + 1
    a = a + 1
print(f"Fim do jogo!!!\nResultado final:\nJogadorAnônimo {placarjogador} X {placarpc} PCparrudo")
if placarjogador > placarpc:
    print("\nVencedor: JogadorAnônimo")
else:
    print("\nVencedor: PCparrudo")
