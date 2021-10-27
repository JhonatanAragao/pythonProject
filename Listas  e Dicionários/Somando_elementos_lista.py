aula sobre a soma de elementos dentro de uma lista;
notas = [];
digite_Nota = float(input("Digite uma nota\n"));
adicao = 0
while digite_Nota != -1:
    nova_nota = digite_Nota
    adicao += digite_Nota
    notas.append(nova_nota)
    digite_Nota = float(input("Digite uma nota\n"));
print(notas)
    #import math
    #adica = math.fsum(notas)
media = adicao/len(notas)
print(media)
