lista_de_funcionarios = []
for _ in range(3):
    nome = input("Digite o nome do funcionário:\n")
    cargo = input("Dgite o cargo do funcionário:\n")
    salario = float(input("Digite o salário do funcionário:\n"))
    dados_do_funcionario = {"nome": nome,"cargo": cargo,"salario": salario}
    lista_de_funcionarios.append(dados_do_funcionario)
for funcinarios in lista_de_funcionarios:
    print("%s - %s - revebe R$%.2f" %(funcinarios["cargo"],funcinarios["nome"],funcinarios["salario"]))