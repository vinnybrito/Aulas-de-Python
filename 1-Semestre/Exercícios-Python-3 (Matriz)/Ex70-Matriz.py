# 70- Entrar com uma matriz de ordem LxC, onde a ordem também será escolhida pelo 
# usuário, sendo que no máximo 10x10. A matriz não precisa ser quadrática. Após a 
# digitação dos elementos, criar uma rotina de consulta, onde o usuário digita um 
# valor e a rotina exibe em qual (ou quais) posição da matriz, o valor escolhido se 
# encontra. Enviar mensagem comunicando se por acaso o valor não estiver armazenado 
# na matriz. Perguntar ao usuário, se deseja ou não fazer nova consulta.

matriz = []

print('Qual será a ordem da sua matriz?')
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
while(linhas > 10):
    print('A matriz deve ter no máximo 10 linhas! Porfavor')