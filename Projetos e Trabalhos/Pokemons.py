#Aluno: Jhonatan Aragão Costa
#Prof.: José Patrício
#Inst.: AESPI - Ensino superior do Piauí
#Curso: Ciência da computação - 2º Período

codigo = True #variável para guardar o valor "TRUE" e manter o while em um loop infinito até que a opção 5 do menu, que aciona o break, seja executada!
lista_de_pokemons = [] #lista para guardar os pokémons do usuário
while codigo == True:
    menu = ("1. Adicionar pokémon\n2. Remover pokémon\n3. Listar pokémons\n4. Mostrar pokémons por letra inicial\n5. Sair\n")#criação do menu de interação!
    print(menu)
    escolha_do_menu = int(input("Escolha uma opão acima:\n")) #Pede ao usuário que escolha um índice do menu;
    if escolha_do_menu > 5 or escolha_do_menu < 1: #tratando erro caso o usuário digite um valor diferente dos valores do menu!
        print("Escolha uma opção válida!!!\n")

    #CASO 1: USUÁRIO ESCOLHEU ADICIONAR POKÉMONS
    elif escolha_do_menu == 1:
        print("** Adicionar um novo pokémon **")
        novo_pokemon = input("Qual pokémon você deseja adicionar?\n")
        contem_na_lista = novo_pokemon in lista_de_pokemons; #Verificar se o pokémon já foi adicionado na lista;
        if contem_na_lista == True:
            print("Você já adicionou esse pokémon na sua lista!")
        else:
            lista_de_pokemons.append(novo_pokemon)
            print("Parabéns você adicionou o pokémon %s com sucesso!" % (novo_pokemon))
            limite_de_pokemons = 0
            while limite_de_pokemons < 5: #Define um limite de no máximo 5 pokémons que o usuário pode adicionar através da opção "Deseja adicionar mais outro?", após isso retorna ao menu inicial;
                add_mais = int(input("Deseja adicionar mais outro pokémon?\n Se sim, digite 1. Se não, digite 2:\n"))
                if add_mais < 1 or add_mais > 2:#impede que o usuario digite outro numero que nao seja 1 ou 2
                    print("Escolha uma opção válida!")
                elif add_mais == 1: #Se o usuário escolheu que sim, pedirá à ele um nome;
                    novo_pokemon = input("Qual pokémon você deseja adicionar?\n")
                    contem_na_lista = novo_pokemon in lista_de_pokemons;  # Verificar se o pokémon já foi adicionado na lista;
                    if contem_na_lista == True:
                        print("Você já adicionou esse pokémon na sua lista!")
                    else:
                        print("Parabéns você adicionou o pokémon %s com sucesso!" % (novo_pokemon))
                        lista_de_pokemons.append(novo_pokemon)
                        limite_de_pokemons += 1
                else: #Se o usuário escolher a opção 2: "não", retornará ao menu inicial;
                    print("Voltando para o menu inicial...\n")
                    break

    #CASO 2: USUÁRIO ESCOLHEU REMOVER  UM POKÉMON
    elif escolha_do_menu == 2:
        print("** Remover um pokémon **\n")
        remover_pokemon = input("Qual o nome do pokémon que você deseja remover?\n")
        contem_na_lista = remover_pokemon in lista_de_pokemons #Variável para verificar a existência do item na lista;
        if contem_na_lista == False:
            print("Você não adicionou esse pokémon na sua lista.\n")
        else:
            lista_de_pokemons.remove(remover_pokemon)
            print("Pokémon %s removido com sucesso!"%(remover_pokemon))
            limite_de_remover = 0
            while limite_de_remover < 5: #Define um limite de no máximo 5 remoções para a opção abaixo;
                remover_outro = int(input("Digite '1' para remover mais um pokémon ou digite '2' para voltar ao menu.\n"))
                if remover_outro < 1 or remover_outro > 2: #tratando erro caso o usuário digite valores diferentes de 1 ou 2 que leva as condicionais de 'sim' ou 'não';
                    print("Digite uma opção válida")
                elif remover_outro == 1:
                    remover_pokemon = input("Qual o nome do pokémon que você deseja remover?\n")
                    contem_na_lista = remover_pokemon in lista_de_pokemons #Variável para verificar a existência do item na lista;
                    if contem_na_lista == False:
                        print("Você não adicionou esse pokémon na sua lista.\n")
                    else:
                        lista_de_pokemons.remove(remover_pokemon)
                        print("Pokémon %s removido com sucesso!\n" % (remover_pokemon))
                else:
                    print("Voltando para o menu inicial...\n") #Aqui o usuário escolhe que não deseja mais remover nenhum pokémon, retornando então, ao menu inicial;
                    break

    #CASO 3: USUÁRIO DESEJA LISTAR  OS POKÉMONS ADICIONADOS
    elif escolha_do_menu == 3:
        quantidade_pokemons = len(lista_de_pokemons);
        print("%d pokémons encontrados!"%(quantidade_pokemons))
        print("Sua lista de pokémons:")
        print("\n".join(lista_de_pokemons)+"\n")

    #CASO 4: USUÁRIO DESEJA MOSTRAR POKÉMONS POR LETRA INICIAL
    elif escolha_do_menu == 4:
        letra_inicial = input("Qual a letra inicial deseja buscar na sua lista de pokémons?\n")
        while len(letra_inicial) > 1: #caso o usuário digite mais que uma letra para a busca.
            print("Digite apenas uma letra!")
            letra_inicial = input("Qual a letra inicial deseja buscar na sua lista de pokémons?\n")
            while len(letra_inicial) == 0: #caso o usuário não digite nenhuma letra.
                print("Digite alguma letra!")
                letra_inicial = input("Qual a letra inicial deseja buscar na sua lista de pokémons?\n")
        a = False #variável para criar condição caso o usuário digite uma letra inicial que nenhum pokémon possui!
        for item in lista_de_pokemons:
            if item[0] == letra_inicial.lower(): #Condição para o programa aceitar tanto letra maiúscula como minúscula
                print(item)
                a = True
        if a == False: #Se a condição da letra inicial digitada não conter em algum pokémon da lista, a variável "a" continuará com o valor "false" e será realizado o seguinte print em tela:
            print("Nenhum pokémon encontrado com essa letra!")

    #CASO 5: USUÁRIO ESCOLHEU SAIR DO PROGRAMA
    else:
        print("Saindo do programa...")
        break #finalizando o laço que abrange o código inteiro levando sempre de volta ao menu de opções;


























