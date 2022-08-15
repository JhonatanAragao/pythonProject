
aliquota1 = "Isento"
aliquota2 = "7.5%"
aliquota3 = "15%"
aliquota4 = "22,5%"
aliquota5 = "27,5%"
while True:
    salario = float(input("digite o valor do salario\n"))
    if salario < 1903.98:
        resultado = salario
        value_aliquota = aliquota1
    elif salario < 2826.65:
        resultado = salario - (salario * 0.075)
        value_aliquota = aliquota2
    elif salario < 3751.06:
        resultado = salario - (salario * 0.15)
        value_aliquota = aliquota3
    elif salario < 4664.68:
        resultado = salario - (salario * 0.2250)
        value_aliquota = aliquota4
    else:
        resultado = salario - (salario * 0.275)
        value_aliquota = aliquota5
    print(f'o valor do salario com desconto é igual a {resultado} e a aliquota é {value_aliquota}')
    decisao_usuario= input("Digite 1 para voltar ao inicío e 2 para finalizar o programa!\n")
    if decisao_usuario == "2":
        print("Fim do programa!")
        break



