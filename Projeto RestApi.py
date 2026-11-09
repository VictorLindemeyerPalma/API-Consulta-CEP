from validacao import validacao_cep
from exibicao import exibir_endereco
from consulta import consulta_cep
### Arquivo principal ###

def sistema_cep():
    while True:
        cep = input("Digite seu CEP (digite sair para sair do programa):  ")

        cep_limpo = validacao_cep(cep)
        if cep_limpo == "sair":
            print("Saindo do programa...")
            break

        dados = consulta_cep(cep_limpo)
        if isinstance(dados, str) and dados.startswith("Erro"):
            print(f"Erro: {dados}")
        else:
            exibir_endereco(dados)

if __name__ == "__main__":
    sistema_cep()
