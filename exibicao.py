### EXIBIÇÃO DOS DADOS DO PROJETO ###
def exibir_endereco(dados: dict) -> None:

    print(f"CEP: {dados.get('cep')}")
    print(f"Logradouro: {dados.get('logradouro')}")
    print(f"Bairro: {dados.get('bairro')}")
    print(f"Cidade: {dados.get('localidade')}")
    print(f"Estado: {dados.get('uf')}")
