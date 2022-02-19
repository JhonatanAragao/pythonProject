import random

print("A dica é paises")
paises = ["brasil", "argentina", "mexico", "chile", "uruguai"]
ad = random.randint(0, len(paises) - 1)
pais = paises[ad]
print(pais)

tentativas = 0
chances = 6
letras_do = []
pronto = ["_"] * len(pais)
print(pronto)
while tentativas < chances and "".join(letras_do) != pais:
    letras = input("Escolha uma letra: ")
    letras_do.append(letras)

    if letras in pais:
        print("Acertou, mizeravi")
    else:
        print("Não acredito que errou essa, tão facinho")
        tentativas += 1
    print(letras_do)
    print(pronto)

if tentativas == chances:
    print("Suas chances acabaram, bora mais uma ")
else:
    print("Alá, ganhou em ")

print("A palavra era", pais)
