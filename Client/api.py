import requests



URL = "http://127.0.0.1:8000"

def criar_sala():
    resposta = requests.post(f"{URL}/criar-sala")
    return resposta.json()

def listar_jogadores(codigo):
    resposta = requests.get(f"{URL}/jogadores/{codigo}")
    return resposta.json()

def entrar_sala(codigo, nick):
    resposta = requests.post(
        f"{URL}/entrar-sala",
        json={
            "codigo": codigo,
            "nick": nick
        }
    )

    return resposta.json()