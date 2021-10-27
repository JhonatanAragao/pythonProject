# Listagem 5.5 – Imprimindo de 1 a 3 com while
#exemplo:
#x=1 ❶
#while x<=3: ❷
#print(x) ❸
#x = x + 1 ❹

#A execução desse programa seria um pouco diferente do que vimos até agora.
#Primeiramente, ❶ seria executada inicializando a variável x com o valor 1. A linha
#❷ seria uma combinação de estrutura condicional com estrutura de repetição.
#Podemos entender a condição do while da mesma forma que a condição de if. A
#diferença é que, se a condição for verdadeira, repetiremos as linhas ❸ e ❹ (bloco)
#enquanto a avaliação da condição for verdadeira.
#Em ❸ teremos a impressão na tela propriamente dita, onde x é 1. Em ❹ temos
#que o valor de x é acrescentado de 1. Como x vale 1, x + 1 valerá 2. Esse novo valor
#é então atribuído a x. A parte nova é que a execução não termina após ❹ que é o

#Exercício 5.1 Modifique o programa para exibir os números de 1 a 100
#um_a_cem = 1
#while um_a_cem <= 100:
#    print(um_a_cem)
#    um_a_cem = um_a_cem + 1

#Exercício 5.2 Modifique o programa para exibir os números de 50 a 100
#cinquenta_a_cem = 50
#while cinquenta_a_cem <= 100:
#    print(cinquenta_a_cem)
#    cinquenta_a_cem = cinquenta_a_cem + 1


#Exercício 5.3 Faça um programa para escrever a contagem regressiva do lançamento
#de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

#contagem = 10
#while contagem >=0:
#    print(contagem)
#    contagem = contagem - 1

#print('Fogo!')

