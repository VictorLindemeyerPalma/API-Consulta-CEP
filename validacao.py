### VALIDAÇÃo DO PROJETO ###

def validacao_cep(cep: str) -> str:

    cep_limpo = cep.replace("-", "").replace(".", "").strip()

    if cep_limpo.lower() == "sair":
        return "sair"

    elif cep_limpo == "":
        return "Erro: nenhum CEP digitado"


    elif len(cep_limpo) != 8:
        return "Erro: o CEP deve conter 8 dígitos"


    elif not cep_limpo.isdigit():
        return "Erro: o CEP deve conter apenas números"

    return cep_limpo