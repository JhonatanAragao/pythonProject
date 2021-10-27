#a = 0
#b = 0
#nome = ""
#dic = {}
#salario = ""
#b = int(input("Digite o número de funcionários:\n"))
#valor_limite = ''
#while a < b:
#    nome = input("Digite seu nome:\n")
#    salario = float(input("Digite seu salário:\n"))
#    dic[nome] = salario
#    a += 1
#valor_limite = int(input("Valor do salário a ser filtrado:\n"))
#for chave,valor in dic.items():
#    if valor > valor_limite:
#        print("Funcionário: %s\nSalário: R$%.2f\n"%(chave,valor))

lista_de_funcionarios = [
    {"nome":"Joao", "cargo":"Dev","Salario":3125},{"nome":"Maria", "cargo":"Gerente","Salario":5120},{"nome":"Suellen", "cargo":"CEO","Salario":11520}
]
for funcinarios in lista_de_funcionarios:
    print("%s - %s - revebe R$%.2f" %(funcinarios["cargo"],funcinarios["nome"],funcinarios["Salario"]))