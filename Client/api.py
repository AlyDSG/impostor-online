import requests



URL = "http://127.0.0.1:8000"

def criar_sala(nick):
    resposta = requests.post(
        f"{URL}/criar-sala",
        json={"nick": nick}
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


def iniciar_jogo(codigo,nick):
    resposta = requests.post(
                f"{URL}/iniciar-jogo",
                json={
                    "codigo": codigo,
                    "nick": nick
                }
            )
    return resposta.json()


def enviar_palavra_api(codigo, nick, palavra):
    resposta = requests.post(
        f"{URL}/enviar-palavra",
        json={
            "codigo": codigo,
            "nick": nick,
            "palavra": palavra
        }
    )

    return resposta.json()


def resultado_api(codigo, nick):
    resposta = requests.get(
        f"{URL}/resultado/{codigo}/{nick}"
    )

    print(resposta.status_code)
    print(resposta.text)

    return resposta.json()
