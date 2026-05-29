"""
Este módulo contém todas as ferramentas de comunicação com APIs do projeto.
"""
import requests


def buscar_cep(cep: str) -> dict:
    """
    Essa função recebe um cep como parâmetro e devolve informações sobre o endereço.
    """
    if cep.isnumeric and len(cep) == 8:
        resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}", timeout=10)
        return resposta.json()
    raise ValueError("Somente permitido CEPs numéricos com 8 digitos.")