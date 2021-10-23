#crie um programa que armazena a quantidade de gols de um jogador em tres partidas e, ao fim, exibe os gols em cada partida e a quantidade total.
#gols_partida1 = int(input("Digite o número de gols:\n"));
#gols_partida2 = int(input("Gols da partida 2:\n"));
#gols_partida3 = int(input("Gols da partida 3:\n"));
#gols_partida4 = int(input("Gols da partida 4:\n"));
#gols_partida5 = int(input("Gols da partida 5:\n"));
#gols_partida6 = int(input("Gols da partida 6:\n"));
#gols_partida7 = int(input("Gols da partida 7:\n"));
#gols_partida8 = int(input("Gols da partida 8:\n"));
#gols_partida9 = int(input("Gols da partida 9:\n"));
#gols_partida10 = int(input("Gols da partida 10:\n"));


#print(f"Os gols feitos nas três partidas foram respectivamente: {gols_partida1}, {gols_partida2}, {gols_partida3}, {gols_partida4}, {gols_partida5}, {gols_partida6}, {gols_partida7}, {gols_partida8}, "
#      f"{gols_partida9} e {gols_partida10}.\n"
#      f"O saldo total de gols é igual a {gols_partida1+gols_partida2+gols_partida3+gols_partida4+gols_partida5+gols_partida6+gols_partida7+gols_partida8+gols_partida9+gols_partida10}");



#minutos = int(60);
#if minutos < 200:
#      preco = 0.20
#else:
#      preco = 0.15
#print("Você irá pagar R$")

#gols = [3,2,10]
#a = 0
#soma = 0
#while a < len(gols):
#      print(gols[a])
#      soma += gols[a]
#      a = a + 1;
#print("\n",soma);

#nomes = ["João","Maria","Pedro","Felipe","Maria Joaquina"]
#a = 0
#while a < len(nomes):
#      print(nomes[a])
#      a = a + 1;

#Com FOR podemos também percorrer listas:

#nomes = ["João","Maria","Pedro","Felipe","Maria Joaquina"]
#for nome in nomes:
#    print(nome);
#nomes[0]=nomes[2]
#print(nomes)

#convidado = input("Digite uma letra:\n");
#convidados = ["André","Carla","John","Luiz","Eduarda","Igor"];
#for nome in convidados:
#    if convidado[0] == nome[0] :
#        print(nome)

#inteiros = [2,5,21,1,0,56,34,6,3,45,15,10]
#for i in inteiros:
#    if i % 2 == 0 and i > 50:
#        print(i);

#a = 0
#while a < len(inteiros):
#    if inteiros[a] % 2 == 0:
#        print(inteiros[a])
#    a = a + 1



#convidados = ["André","Brasil","John","lâmpada","eduarda","Igor","aladin"];
#for i in convidados:
#    if i[0] == "a" or i[0] == "A":
#        print(i)

#print()
#for i in convidados:
#    if i[0] != "a" and i[0] !="A":
#        print(i)

#lista_inteiros = [3,67,34,2,1,89,32,55,15,10]
#for i in range(len(lista_inteiros)):
#    if i % 2 == 0 and i != 0:
#        print(lista_inteiros[i])
#lista_inteiros.append(9)
#print(lista_inteiros, "usando APPEND para adicionar o número 9 ")
#lista_inteiros.insert(2,355)
#print(lista_inteiros, "Usando o INSERT para inserir '355' no indice 2")
#del lista_inteiros[3]
#print(lista_inteiros, "usando o DEL para deletar o índice 3")
#lista_inteiros.remove(355)
#print(lista_inteiros, "usando REMOVE para apagar o elemento com valor '355'")

#notas = [5.5,3.5,2.0,7.0,9.5]
#print(notas)
#notas.append(3.2)
#print(notas)
#notas.insert(5,10.0)
#print(notas)

#palavras = ["frase","André","Informática","Hello World"]
#print(palavras)
#for i in range(2):
#    nova_palavra = input("Digite uma nova palavra:\n")
#    palavras.append(nova_palavra)
#    print(palavras)
#escolhaindice = int(input(f"Digite um numero no intervalo de 0 a {len(palavras)}:\n"))
#removido = palavras.pop(escolhaindice)
#    for i in palavras:
#        print(i + ", ",end="")
#        print(palavras, f"{removido} foi a palavra removida!")
#print(", ".join(palavras) + ".",f"{removido} foi a palavra removida") #f'{removido} foi a palavra removida!') #melhor forma para remover os colchetes

#nomes = ["Paulo","Ana","Luiz","Evelyn"]
#print(nomes)
#escolha = int(input("Escolha a opção desejada:\n[1] Adicionar nome\n[2] Remover nome"));
#if escolha == 1:
#    novo_nome = input("Digite um novo nome:\n")
#    nomes.append(novo_nome)
#    print(nomes)
#elif escolha == 2:
#    remover_nome = input("Qual nome deseja remover?")
#    nomes.remove(remover_nome)
#    print(nomes)


#aula sobre a soma de elementos dentro de uma lista;
#notas = [];
#digite_Nota = float(input("Digite uma nota\n"));
#adicao = 0
#while digite_Nota != -1:
#    nova_nota = digite_Nota
#    adicao += digite_Nota
#    notas.append(nova_nota)
#    digite_Nota = float(input("Digite uma nota\n"));
#print(notas)
#    #import math
#    #adica = math.fsum(notas)
#media = adicao/len(notas)
#print(media)

#dict1 = {"a":1,"b":2,"c":3,"d":4}
#print(dict1)
#adc = input('deseja adicionar a chave "e"?\n')
#if adc == "sim":
#    valor = int(input("qual o valor da chave?\n"))
#    dict1["e"] = valor
#
#if "e" in dict1:
#    print(dict1)
#else:
#    print("Chave não encontrada!")

#VERIFICANDO A EXISTÊNCIA DE UMA CHAVE NO DICIONÁRIO
#produtos = {"abacate":"R$5.00","pêra":"R$2.00","maça":"R$1.50","uva":"R$4.00"}
#escolha_produto = input("Digite o nome de um produto:\n")
#if escolha_produto in produtos:
#    print(produtos[escolha_produto])
#else:
#    print("Produto não encontrado!")

#produtos = {"abacate":"R$5.00","pêra":"R$2.00","maça":"R$1.50","uva":"R$4.00"}
#for i in produtos.keys():
#    if i[0] == "a":
#        print(produtos[i])#imprime o valor
#        print(i)#imprime o valor da chave

produtos = {"abacate":5.00,"pêra":2.00,"maça":1.50,"uva":4.00,"abacaxi":8.00}
print("Tabela de preços\n")
letra = input("digite uma letra\n")
if len(letra) > 1:
    print("Digite apenas uma letra!")
else:
    for chave,valor in produtos.items():
        if chave[0] == letra:
            print(chave,produtos[chave])