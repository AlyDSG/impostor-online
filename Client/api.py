import requests



URL = "http://127.0.0.1:8000"

def criar_sala(nick):
    resposta = requests.post(
        f"{URL}/criar-sala",
        json={
            "nick": nick
        }
    )

  
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

def sairsala(codigo, nick):
    resposta = requests.post(
            f"{URL}/sair-sala",
            json={
                "codigo": codigo,
                "nick": nick
            }
        )
    return resposta.json()