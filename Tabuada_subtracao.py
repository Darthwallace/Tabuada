import emoji

opcao = int(input("Qual a tabuada que deseja escolher: \n1- Soma\n\n2- Subtração\n\n3- Divisão\n\n4- Multiplicação\n\nopção: "))
while opcao > 4:
    print(emoji.emojize("Essa opção não existe. Digite uma das opções :point_up_2:",use_aliases=True))
    opcao = int(input("Opção: "))
else:
    if opcao == 1:
        n = int(input("Informe o número de 0 á 10: "))
        while n > 10:
            print("A tabuada vai somente o número 10. favor inserir o valor de 0 á 10: ")
            n = int(input(" "))
        else:
            print('-' * 46)
            print("A tabuada de SOMA com o número {} ficará assim:".format(n))
            print('-' * 46)
            for i in range(1,10+1):
                print("|{} + {} = {}|".format(n, i , i + n))
                print('=' * 11)
    elif opcao == 2:
        n = int(input("Informe o número: "))
        while n > 10:
            print("A tabuada vai somente o número 10. favor inserir o valor de 0 á 10: ")
            n = int(input(" "))
        else:
            print("A tabuada de SUBTRAÇÃO com o número {} ficará assim:".format(n))
            for i in range(n+1,11+n):
                print("|{} - {} = {}|".format(i,n , i - n))
    elif opcao == 3:
        n = int(input("Informe o número: "))
        while n > 10:
            print("A tabuada vai somente o número 10. favor inserir o valor de 0 á 10: ")
            n = int(input(" "))
        else:
            print("A tabuada de DIVISÃO com o número {} ficará assim:".format(n))
            for i in range(n,(n*10)+1,n):
                print("|{} / {} = {}|".format(i,n , i / n))
    else:
        n = int(input("Informe o número: "))
        while n > 10:
            print("A tabuada vai somente o número 10. favor inserir o valor de 0 á 10: ")
            n = int(input(" "))
        else:
            print("A tabuada de MULTIPLICAÇÃO com o número {} ficará assim:",format(n))    
            for i in range(1,10+1):
                print("|{} X {} = {}|".format(i,n , i * n))
print(emoji.emojize("Que bom que obteve informações importantes na sua aprendizagem :pray:",use_aliases=True))
