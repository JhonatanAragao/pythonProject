 #..............  #Encerrando o capitulo 4 do livro

#Convertendo str:
#print (float ("2.5"));
#print(int('25'));
#print(int('25'+"4"));
#a = "3.82";
#print(type (a) );
#a = float(a);
#print(type(a));


#Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
#e o menor.

#Variáveis para os números
#n1 = int(input('Digite o primeiro número:\n'));
#n2 = int(input('Digite o segundo número:\n'));
#n3 = int(input('Digite o terceiro número:\n'));

#Condições
#if n1 > (n2 and n3):
# print(f'O número {n1} é o maior.')
#elif n2 > n3:
#    print(f'O número {n2} é o maior.')
#else: print(f'O número {n3} é o maior.')
#print(f'1º numero {n1}\n2º numero {n2}\n3º numero {n3}')


#Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.

salario = (float(input('Digite seu salário:\n')))
if salario <= 1.250:
    print('O seu reajuste com o aumento de 15% é de R${} e o seu salário reajustado é R${}'.format(salario*15/100,salario+(salario*15/100)))
if salario > 1.250:
    print('O seu reajuste com o aumento de 10% é de R${} e o seu salário reajustado é R${}'.format(salario+salario*10/100(salario*10/100)))

import math
angulo = float (input('Digite o ângulo que você deseja:\n')
seno = math.sin(math.radians(angulo)) #NOTA IMPORTANTE: aqui nesse caso a função math.sin (seno) retorna um valor em graus por padrão. Por isso nesse caso utilizamos math.radius para realizar a conversão desse resultado em graus para radianos.
print (f'o ângulo de {angulo} tem o SENO de {seno}\n')
