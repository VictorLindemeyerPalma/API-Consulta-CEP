### CONSULTA DO PROJETO ###
import requests

def consulta_cep(cep_limpo: str):
    """"A API consumi a API externa do Via CEP"""
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    print("Buscando endereço...")

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException:
        return "Erro: não foi possível conectar à API."

    if "erro" in dados:
        return "Erro: CEP não encontrado."

    return dados