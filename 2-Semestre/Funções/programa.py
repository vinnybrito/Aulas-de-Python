from utils import ApiCep as ac

cep = input("Digite o CEP desejado: ")

dados = ac.consultaCep(cep)

if dados != '':
    print(f"CEP: {dados['cep']}")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
else:
    print("CEP não encontrado.")