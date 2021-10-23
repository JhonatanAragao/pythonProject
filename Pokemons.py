#PROBLEMAS

#Ash Ketchum é um jovem da cidade de Pallet que está
#viajando pelo país em sua aventura de tornar-se o
#melhor treinador pokémon. No caminho ele participou
#de muitas batalhas e tem um grande número de
#pokémons, tantos que já é bem difícil saber quantos e
#quais são e frequentemente ele se embaraça achando
#que possui um pokémon quando não o possui, ou
#esquecendo os que possui.
#Para resolver este problema, Ash pediu a você que o ajudasse criando um programa que
#o auxilie a gerenciar melhor seus pokémons. O programa deve exibir um menu com as
#opções:
#1. Adicionar pokémon
#2. Remover pokémon
#3. Listar pokémons
#4. Mostrar pokémons por letra inicial
#5. Sair
#As opções 3 e 4 deve exibir os itens e mostrar a quantidade de itens exibidos (ex.: “37
#pokémons encontrados”). A opção 4 deve receber uma letra do usuário e mostrar todos
#os itens da lista que iniciam com essa letra (maiúsculas e minúsculas devem ser
#ignoradas).
#menu = ["1. Adicionar pokémon","2. Remover pokémon","3. Listas","4. Mostrar pokémons por letra inicial","5. Sair"]
codigo = True
while codigo == True:
    menu = ("1. Adicionar pokémon\n2. Remover pokémon\n3. Listar pokémons\n4. Mostrar pokémons por letra inicial\n5. Sair\n")#criação do menu de interação!
    print(menu)
    escolha_do_menu = int(input("Escolha uma opão acima:\n"))
    if escolha_do_menu > 5 or escolha_do_menu < 1: #tratando erro caso o usuário digite um valor diferente dos valores do menu!
        print("Escolha uma opção válida!!!\n")

    #CASO 1: USUÁRIO ESCOLHEU ADICIONAR POKÉMONS
    elif escolha_do_menu == 1:
        lista_de_pokemons = []
        print("** Adicionar um novo pokémon **")
        novo_pokemon = input("Qual pokémon você deseja adicionar?\n")
        lista_de_pokemons.append(novo_pokemon)
        print("Parabéns você adicionou o pokémon %s com sucesso!"%(novo_pokemon))
        limite_de_pokemons = 0###
        while limite_de_pokemons < 5:
            add_mais = int(input("Deseja adicionar mais outro pokémon?\n Se sim, digite 1. Se não, digite 2:\n"))
            if add_mais < 1 or add_mais > 2:#impede que o usuario digite outro numero que nao seja 1 ou 2
                print("Escolha uma opção válida!")
            elif add_mais == 1:
                novo_pokemon = input("Qual pokémon você deseja adicionar?\n")
                print("Parabéns você adicionou o pokémon %s com sucesso!" % (novo_pokemon))
                lista_de_pokemons.append(novo_pokemon)
                limite_de_pokemons += 1
            else:
                print("Voltando para o menu inicial...\n")
                break

    #CASO 2: USUÁRIO ESCOLHEU REMOVER  UM POKÉMON
    elif escolha_do_menu == 2:
        print("** Remover um pokémon **\n")
        remover_pokemon = input("Qual o nome do pokémon que você deseja remover?")
        lista_de_pokemons.remove(remover_pokemon)
        print("Pokémon %s removido com sucesso!"%(remover_pokemon))
        limite_de_remover = 0
        while limite_de_remover < 5:
            remover_outro = int(input("Digite '1' para remover mais um pokémon ou digite '2' para voltar ao menu.\n"))
            if remover_outro < 1 or remover_outro > 2:
                print("Digite uma opção válida")
            elif remover_outro == 1:
                remover_pokemon = input("Qual o nome do pokémon que você deseja remover?\n")
                lista_de_pokemons.remove(remover_pokemon)
                print("Pokémon %s removido com sucesso!\n" % (remover_pokemon))
            else:
                print("Voltando para o menu inicial...\n")
                break

    #CASO 3: USUÁRIO DESEJA LISTAR  OS POKÉMONS ADICIONADOS
    elif escolha_do_menu == 3:
#vdc















