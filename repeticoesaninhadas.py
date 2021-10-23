#a = "";
#b = "";
#escolha = ("Escolha a operação [+,-,*,/] ou 0 para sair: \n");
#operacao = input(escolha);

#while operacao != 0:
#    for a in range(1,11):
#        for b in range(0,10):
#            if operacao == "+":
#                resultado = b + a;
#            elif operacao == "-":
#                resultado = b - a;
#            elif operacao == "*":
#                resultado = b * a;
#            elif operacao == "/":
#                if a == 1:
#                    resultado = b / a
#                else:
#                    if b % 2 == 0 and a % 2 == 0:
#                        resultado = b / a
#                    elif b % 3 == 0 and a == 3:
#                        resultado = b / a
#                    else:
#                        continue

#            else:
#                print("Você não escolheu uma operação válida!");
#                break
#            print("%d %s %d = %d" %(b,operacao,a,resultado))
#    operacao = input(escolha)


#print("FIM do meu progama")



#Exercicio: