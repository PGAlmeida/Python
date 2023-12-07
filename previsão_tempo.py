import requests

url = "https://wttr.in/Ipua"

try:
    resposta = requests.get(url)
    data = resposta.text
    if resposta.status_code == 200:
        print(data)
    else:
        print("Não foi possível obter os dados desse link")

except Exception as e:
    print(f"Ocorreu um erro ao acessar a API: {e}")