import random
lis = []
for i in range(5):
    if i > 0:
        nome = input("Digite o nome do %sº jogador:\n"%(i))

        lis.append(nome)
print(random.choice(lis), end=" venceu o jogo!")