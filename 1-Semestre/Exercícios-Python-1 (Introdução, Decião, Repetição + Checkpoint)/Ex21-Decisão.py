# 21. Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um 
# seletor de opções (“menu”) com as seguintes opções: (Fazer esse exercício 
# utilizando If..Else e/ou Case)

# 1 – Multiplicação
# 2 – Adição
# 3 – Divisão
# 4 – Subtração
# 5 – Fim de processo (sair do programa)

#Solicitar uma opção por parte do usuário, verificar se é ou não uma opção válida 
# (letras ou números) e processar a respectiva operação. Enviar mensagem de erro se a 
# opção escolhida não existir no seletor.

#Encerrar o programa somente quando o usuário escolher a opção de finalização. Repare 
# que a opção de número três é de divisão e o programa deverá enviar mensagem de 
# erro, (somente nesta opção) se o denominador for zero.

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
