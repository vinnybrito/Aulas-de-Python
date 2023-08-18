# 52- Armazenar dez valores na memória do computador. 
# Após a digitação dos valores, criar uma rotina para ler os valores 
# e achar e exibir o maior deles.

valores = []
for i in range(10):
    valor = int(input(f"Informe o {i + 1}° valor: "))
    valores.append(valor)

maior = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor

print("Maior valor:", maior)

