#Exercício sobre strings e estruturas de decisão:

#1. Receba o nome do usuário e imprima "Seu nome é: " seguido da string recebida;
nomeUsuario = input("Digite seu nome:\n");
print("Seu nome é:\n",nomeUsuario);

#-------------------------------------------------------------------------------------

#2. Receba o nome do usuário e o imprima ao contrário após a mensagem "Seu nome é ao contrário é: ";
print("Seu nome inverso é:\n",nomeUsuario [::-1]);

#--------------------------------------------------------------------------------------

#3. Receba um texto e o imprima somente se a primeira letra do nome for ‘a’;
textoA = str(input("\nDigite um texto:\n"));
if textoA[0] == "a" or textoA[0] == "A":
    print(textoA);
else:
    print('O texto não começa com a letra "a"!');

#--------------------------------------------------------------------------------------

#4. Receba um texto e imprima suas 4 primeiras letras;
texto4Letras = str(input("Digite um texto para obter suas 4 primeiras letras:\n"));
print("As 4 primeiras letras do seu texto corresponde a:",texto4Letras[0:4]);

#--------------------------------------------------------------------------------------

#5. Receba duas strings digitadas pelo usuário e imprima a menor das duas;
string1 = str(input("Digite uma palavra:\n"));
string2 = str(input("Digite outra palavra:\n"));
if len(string1) < len(string2):
    print(string1);
else:
    print(string2);

#--------------------------------------------------------------------------------------

#6. Receba duas strings, as concatene e mostre o resultado para o usuário. Exemplo: se o
#usuário digitou primeiro "Programar é " e depois "muito bom!", então o programa deve imprimir: "Programar é muito bom!";
stringConc1 = str(input("Vamos concatenar strings?...Digite um texto:\n"));
stringConc2 = str(input("Agora digite outro texto:\n"));
print(stringConc1,stringConc2);

#--------------------------------------------------------------------------------------

#7. Receba a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
#do mês por extenso. Exemplo: se o usuário digitar "11/09/2001" o programa deve
#mostrar "Você nasceu em 11 de Setembro de 2001";


#--------------------------------------------------------------------------------------

#8. Receba um número no intervalo de 0 à 10 e imprima-o na tela por extenso;
numeroPorExtenso = int(input("Digite um número de 0 a 10:\n"));
if numeroPorExtenso == 0:
    print("Zero");
elif numeroPorExtenso == 1:
    print("Um");
elif numeroPorExtenso == 2:
    print("Dois");
elif numeroPorExtenso == 3:
    print("Três");
elif numeroPorExtenso == 4:
    print("Quatro");
elif numeroPorExtenso == 5:
    print("Cinco");
elif numeroPorExtenso == 6:
    print("Seis");
elif numeroPorExtenso == 7:
    print("Sete");
elif numeroPorExtenso == 8:
    print("Oito");
elif numeroPorExtenso == 9:
    print("Nove");
else:
    print("Dez");

#--------------------------------------------------------------------------------------

#9. Receba duas strings e informe se uma é o contrário da outra ou não;
stringContraria1 = str(input("Digite uma palavra:\n"));
stringContraria2 = str(input("Digite outra palavra:\n"));
if stringContraria1 == stringContraria2[::-1]:
    print("As palavras são iguais, porém uma está ao contrário!\n");
else:
    print("As palavras são diferentes!\n");

#--------------------------------------------------------------------------------------

#10. Receba uma string e mostre somente seus caracteres cujos índices são divisíveis por 3;
stringDivisivel = str(input("Digite uma palavra:\n"));
print("As letras dos índices divisíveis por 3 são:",stringDivisivel[3::3]);

#--------------------------------------------------------------------------------------

#11. Receba duas strings e mostre a diferença de tamanho entre elas (a diferença deve ser positiva);
stringTam1 = str(input("Digite uma palavra:\n"));
stringTam2 = str(input("Digite outra palavra:\n"));
if len(stringTam1) > len(stringTam2):
    print(len(stringTam1) - len(stringTam2));
else:
    print(len(stringTam2) - len(stringTam1));

#--------------------------------------------------------------------------------------

#12. Receba duas strings e imprima na tela o caractere de posição N na primeira string, onde N é o tamanho da segunda string;
stringN1 = str(input("Digite uma palavra:\n"));
stringN2 = str(input("Digite outra palavra:\n"));
posicaoIndice = len(stringN2);
print("O caractere com o índice de valor correspondente ao tamanho da segunda palavra é:\n",stringN1[posicaoIndice]);
#OBS: Para o funcionamento, a segunda palavra digitada nao pode ser maior que a primeira!

#--------------------------------------------------------------------------------------

#13. Receba duas strings e imprima ambas até o caractere de posição N, sendo N o tamanho da menor delas;
stringN3 = str(input("Digite uma palavra:\n"));
stringN4 = str(input("Digite outra palavra:\n"));
tamanhoMenor = ();
if len(stringN3) > len(stringN4):
    tamanhoMenor = len(stringN4)
else:
    tamanhoMenor = len(stringN3)
print(stringN3[:tamanhoMenor],'\n',stringN4[:tamanhoMenor]);

#--------------------------------------------------------------------------------------

#14. Receba duas strings e imprima os caracteres de posição PAR da primeira seguidos pelos caracteres de posição ÍMPAR da segunda;
stringPosicao1 = str(input("Digite uma palavra:\n"));
stringPosicao2 = str(input("Digite outra palavra:\n"));
caracteresPares = stringPosicao1[0::2];
caracteresImpares = stringPosicao2[1::2];
print(caracteresPares + caracteresImpares);

#--------------------------------------------------------------------------------------

#15. Receba o salário do usuário, calcule um bônus de 13% e o exiba com 3 casas decimais.
salarioFuncionario = float(input("Digite seu salário:\n"));
aumento = salarioFuncionario + (salarioFuncionario*13/100);
print(f"Seu novo salário com o bônus de 13% é: {aumento:.2f}");





