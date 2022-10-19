# 22. Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os 
# dados necessários para o cálculo da respectiva área. Enviar mensagem de erro se o 
# usuário escolher uma opção inexistente.

# Encerrar o programa somente quando selecionada a opção de finalização. (Fazer esse 
# exercício utilizando If..Else e/ou Case)

# 1 – Triângulo
# 2 – Quadrado
# 3 – Retângulo
# 4 – Círculo
# 5 – Fim de processo

menu = input(" 1– Triângulo \n 2– Quadrado \n 3– Retângulo \n 4– Círculo \n 5– Fim de processo \n Selecione uma das opções: ")

if (menu == "1"):
    b = int(input("Digite o valor da base do triângulo: "))
    h = int(input("Digite o valor da altura do triângulo: "))

    a = (b * h) / 2
    
    print("O valor da área do seu triângulo é: ", a)
elif (menu == "2"):
    l = int(input("Digite o valor da aresta do seu quadrado: "))

    a = l * l

    print("A área do seu quadrado é: ", a)
elif (menu == "3"):
    b = int(input('Digite o valor da base do se retângulo: '))
    h = int(input('Digite o valor da altura do seu retângulo: '))

    a = b * h
    print('A área do se retângulo é: ', a)
elif (menu == "4"):
    r = float(input("Digite o valor do raio: "))

    a = 3.14 * (r * r)
    print("O valor aproximado da área do círculo é: ", a)
elif (menu == "5"):
    exit("Fim do processo.")
else:
    print("Não foi possivel idêntificar sua escolha.")
