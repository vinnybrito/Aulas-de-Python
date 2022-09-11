
v1 = int(input('Digite o primeiro valor: '))

v2 = int(input('Digite o segundo valor: '))

menu = input('\n 1– Multiplicação \n 2– Adição \n 3– Divisão \n 4– Subtração \n 5– Fim de processo \n Selecione uma das opções:  ')

if (menu == "1"):
    r = v1 * v2
    print('A multiplicação dos dois valores correspondem á', r)
elif (menu == "2"):
    r = v1 + v2
    print('A soma dos dois valores correspondem á', r)
elif (menu == "3"):
    if (v2 == 0):
        print('Não é possível realizar a divisão com um denominador 0.')
    else:
        r = v1 / v2
        print('A divisão dos dois valores correspondem á', r)
elif (menu == "4"):
    r = v1 - v2
    print('A subtração dos dois valores correspondem á', r)
elif (menu == "5"):
    print('Fim do processo.')
else:
    print('Não foi possivel idêntificar sua escolha.')
