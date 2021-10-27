dict1 = {"a":1,"b":2,"c":3,"d":4}
print(dict1)
adc = input('deseja adicionar a chave "e"?\n')
if adc == "sim":
    valor = int(input("qual o valor da chave?\n"))
    dict1["e"] = valor

if "e" in dict1:
    print(dict1)
else:
    print("Chave não encontrada!")

#VERIFICANDO A EXISTÊNCIA DE UMA CHAVE NO DICIONÁRIO
produtos = {"abacate":"R$5.00","pêra":"R$2.00","maça":"R$1.50","uva":"R$4.00"}
escolha_produto = input("Digite o nome de um produto:\n")
if escolha_produto in produtos:
    print(produtos[escolha_produto])
else:
    print("Produto não encontrado!")
produtos = {"abacate":"R$5.00","pêra":"R$2.00","maça":"R$1.50","uva":"R$4.00"}
for i in produtos.keys():
    if i[0] == "a":
        print(produtos[i])#imprime o valor
        print(i)#imprime o valor da chave

produtos = {"abacate":5.00,"pêra":2.00,"maça":1.50,"uva":4.00,"abacaxi":8.00}
print("Tabela de preços\n")
letra = input("digite uma letra\n")
if len(letra) > 1:
    print("Digite apenas uma letra!")
else:
    for chave,valor in produtos.items():
        if chave[0] == letra:
            print(chave,produtos[chave])