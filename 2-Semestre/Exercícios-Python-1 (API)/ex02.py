import requests

login = input("Digite o nome do seu GitHub: ")
url = f"https://api.github.com/users/{login}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}")
    print(f"Quantidade de Repositórios: {dados['public_repos']}")
    print(f"Seguidores: {dados['followers']}")
else:
    print("Perfil não encontrado.")