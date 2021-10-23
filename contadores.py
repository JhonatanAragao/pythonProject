#5.1 Contadores pag. 84
#O poder das estruturas de repetições é muito interessante, principalmente quando
#utilizamos condições com mais de uma variável. Imagine um problema onde deveríamos imprimir os números inteiros entre 1 e um valor digitado pelo usuário.
#Vamos modificar o programa da listagem 5.5 de forma que o último número a
#imprimir seja informado pelo usuário. O programa já modificado é apresentado
#na listagem 5.6.

#numero = int(input('Digite o último número a imprimir:\n'))
#x = 1
#while x <= numero:
#    print(x)
#    x = x + 1


#alterando o programa anterior para utilizar somente os números pares.
numero = 15 #int(input('Digite o último número a imprimir:\n'))
x = 0
while x <= numero:
    if x % 2 ==0:
        print(x)
    x = x + 1


