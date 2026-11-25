# API-Consulta-CEP
(ING) Modular Python application that validates a Brazilian ZIP code (CEP), queries the
public [ViaCEP](https://viacep.com.br) REST API, and displays the formatted address.

## Features

- ZIP code format validation before the request
- Address lookup through the ViaCEP API
- Error handling for network failures and non-existent ZIP codes
- Formatted output

## Tech stack

- Python 3
- Requests

## Project structure

[Replace with your actual file names]

| File | Responsibility |
|---|---|
| `main.py` | Orchestrates the program flow |
| `validacao.py` | Validates the ZIP code input |
| `consulta.py` | Sends the request to the ViaCEP API |
| `exibicao.py` | Formats and displays the result |

## How to run

```bash
git clone https://github.com/VictorLindemeyerPalma/API-Consulta-CEP.git
cd API-Consulta-CEP
pip install requests
python main.py
```

## Usage example

[Paste a real input/output example from your program]

```
Enter ZIP code: 90010-000
Street: ...
Neighborhood: ...
City: ...
State: RS
```

(PT-BR) # Consulta de CEP em Python

Aplicação modular em Python que valida um CEP, consulta a API REST pública
[ViaCEP](https://viacep.com.br) e exibe o endereço formatado.

Modular Python application that validates a Brazilian ZIP code (CEP), queries the
public [ViaCEP](https://viacep.com.br) REST API, and displays the formatted address.

## Funcionalidades

- Validação do formato do CEP antes da consulta
- Consulta de endereço na API ViaCEP
- Tratamento de erros de rede e de CEP inexistente
- Exibição formatada do resultado

## Tecnologias

- Python 3
- Requests

## Estrutura do projeto

[Troque pelos nomes reais dos seus arquivos]

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Orquestra o fluxo do programa |
| `validacao.py` | Valida o CEP informado |
| `consulta.py` | Faz a requisição à API ViaCEP |
| `exibicao.py` | Formata e mostra o resultado |

## Como executar

```bash
git clone https://github.com/VictorLindemeyerPalma/API-Consulta-CEP.git
cd API-Consulta-CEP
pip install requests
python main.py
```

## Exemplo de uso

[Cole aqui um exemplo real de entrada e saída do seu programa]

```
Digite o CEP: 90010-000
Logradouro: ...
Bairro: ...
Cidade: ...
UF: RS
```

