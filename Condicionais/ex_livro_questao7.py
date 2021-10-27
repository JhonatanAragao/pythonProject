#7. Receba a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
#do mês por extenso. Exemplo: se o usuário digitar "11/09/2001" o programa deve
#mostrar "Você nasceu em 11 de Setembro de 2001";

dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa): \n");

dia = dataNascimento[0:2];
ano = dataNascimento[6:10];

if dataNascimento[3:5] == "01" :
    mes = "Janeiro";
elif dataNascimento[3:5] == "02":
    mes = "Fevereiro"
elif dataNascimento[3:5] == "03":
    mes = "Março"
elif dataNascimento[3:5] == "04":
    mes = "Abril"
elif dataNascimento[3:5] == "05":
    mes = "Maio"
elif dataNascimento[3:5] == "06":
    mes = "Junho"
elif dataNascimento[3:5] == "07":
    mes = "Julho"
elif dataNascimento[3:5] == "08":
    mes = "Agosto"
elif dataNascimento[3:5] == "09":
    mes = "Setembro"
elif dataNascimento[3:5] == "10":
    mes = "Outubro"
elif dataNascimento[3:5] == "11":
    mes = "Novembro"
elif dataNascimento[3:5] == "12":
    mes = "Dezembro"
else: print("Digite um mês válido!!!")
print(f"Você nasceu no dia {dia} de {mes} de {ano}")