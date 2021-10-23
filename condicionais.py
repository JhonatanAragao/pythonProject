#Introdução à condicionais (if,else,elif)...

#Pag. 74 do livro
#Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
#80 km/h.

vel = (int(input('Qual sua velocidade em Km/h?\n')));
if vel > 80:
    print('ATENÇÃO! Você foi multado no valor de R${}.'.format(vel*5) )
    if vel < 96 : #Se a velocidade nao atingir 96kmh (80 + 10%) o programa considera infração média.
        print('Infração média 10% acima do permitido.')
    elif vel <= 120: #Porém nesse caso ela já não é menor que 96 mas se ela for menor ou igual a 120km/h vai estar dentro dos requisitos para considerar uma infração grave, 80+ 20%
        print('Infração GRAVE 20% acima do permitido. ')
    elif vel > 120:
        print('Infração GRAVÍSSIMA 50% acima do permitido \n'
              '7 pontos na carteira sujeito a recolhimento da CNH.')
else:
    print('Velocidade no limite estabelecido!')
print('Fim')