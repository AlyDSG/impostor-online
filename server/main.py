from fastapi import FastAPI
from salas import salas, gerar_codigo
from models import EntrarSalaRequest, CriarSalaRequest, SairSalaRequest, IniciarJogoRequest, EnviarPalavraRequest
import random

#salas[dados.codigo] -> todas as salas
#salas["ABC123"] - > {
 #   "jogadores": [...],
 #   "host": "aaa"
#}
#salas[dados.codigo]["jogadores"] -> todos os nicks

'''
salas = {
    "ABC123": {
        "jogadores": [
            {"nick": "aaa"},
            {"nick": "bbb"},
            {"nick": "ccc"}
        ],
        "host": "aaa"
    },

    "XYZ789": {
        "jogadores": [
            {"nick": "joao"},
            {"nick": "maria"}
        ],
        "host": "joao"
    }
}
'''



app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/criar-sala")
def criar_sala(dados: CriarSalaRequest):
    host = dados.nick
    codigo = gerar_codigo()
    salas[codigo] = {
        "jogadores": [],
        "host":host,
        "estado": "lobby"
    }
    
    return {
        "codigo": codigo,
        "host":host,
        "estado": "lobby"
    }



@app.post("/entrar-sala")
def entrar_sala(dados: EntrarSalaRequest):

    if dados.codigo not in salas:
        return {
                    "sucesso": False,
                    "erro": "Sala não existe."
                }
    
    jogadores = salas[dados.codigo]["jogadores"]

    for jogador in jogadores:
        if jogador["nick"] == dados.nick:
            return {
            "sucesso": False,
            "erro": "Nick Já utilizado."
        }

    if not dados.nick.strip():
        return {
            "sucesso": False,
            "erro": "Nick não pode ficar vazio."
        }
    
    jogadores.append({
    "nick": dados.nick
})

    return {
                "sucesso": True,
                "erro": "Jogador entrou!."
            }



@app.get("/jogadores/{codigo}")
def listar_jogadores(codigo: str):

    if codigo not in salas:
        return {
            "erro": "Sala não encontrada."
        }
    

    return {
        "jogadores": salas[codigo]["jogadores"],
        "host": salas[codigo]["host"],
        "estado": salas[codigo]["estado"]
        
    }

@app.post("/sair-sala")
def sair_lobby(dados: SairSalaRequest):

    if dados.codigo not in salas:
        return {
            "sucesso": False,
            "erro": "Sala não existe."
        }

    jogadores = salas[dados.codigo]["jogadores"]
    host = salas[dados.codigo]["host"]

    for jogador in jogadores:
        if jogador["nick"] == dados.nick:
            jogadores.remove(jogador)

            if jogador["nick"] == host:
                if jogadores:
                    salas[dados.codigo]["host"] = jogadores[0]["nick"]

            return {
                "sucesso": True
            }

    return {
        "sucesso": False,
        "erro": "Jogador não está na sala."
    }

@app.post("/iniciar-jogo")
def iniciar_jogo(dados: IniciarJogoRequest):

    if dados.codigo not in salas:
            return {
                "sucesso": False,
                "erro": "Sala não existe."
            }
    host = salas[dados.codigo]["host"]
    if dados.nick == host:
        #jogador é host
        pass
    else:
        return{
            "sucesso": False,
            "erro": "Jogador não é o host"
        }

    salas[dados.codigo]["estado"] = "jogo"
    return {
        "sucesso": True,
        "estado": "jogo"
    }


@app.post("/enviar-palavra")
def enviar_palavra(dados: EnviarPalavraRequest):
#{"nick": "Alysson", "palavra": "banana"}
    jogadores = salas[dados.codigo]["jogadores"]
    todos_enviaram = True

    for jogador in jogadores:
        if jogador["nick"] == dados.nick:
            jogador["palavra"] = dados.palavra

    for jogador in jogadores:
        if "palavra" not in jogador:
            todos_enviaram = False

    if todos_enviaram is True:
        palavras = []

        for jogador in jogadores:
            palavras.append(jogador["palavra"])

        palavra_escolhida = random.choice(palavras)
        salas[dados.codigo]["palavra"] = palavra_escolhida
        jogador_escolhido = random.choice(jogadores)
        salas[dados.codigo]["impostor"] = jogador_escolhido["nick"]

        if dados.nick == salas[dados.codigo]["impostor"]["nick"]:
            informacao = "IMPOSTOR"
        else:
            informacao = salas[dados.codigo]["palavra"]

        for jogador in jogadores:
            if jogador["nick"] == salas[dados.codigo]["impostor"]["nick"]:
                jogador["resultado"] = "IMPOSTOR"
            else:
                jogador["resultado"] = salas[dados.codigo]["palavra"]

        return {
            "sucesso": True,
            "todos_enviaram": todos_enviaram,
            "resultado": informacao
        }
    return{
        "sucesso": True,
        "todos_enviaram": todos_enviaram
    }

@app.get("/resultado/{codigo}/{nick}")
def resultado(codigo: str, nick: str):
    jogadores = salas[codigo]["jogadores"]

    for jogador in jogadores:
        if jogador["nick"] == nick:
            if "resultado" in jogador:
                return{
                    "sucesso": True,
                    "resultado": jogador["resultado"]
                }
            else:
                return {
                    "sucesso": False
                }
