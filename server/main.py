from fastapi import FastAPI
from salas import salas, gerar_codigo
from pydantic import BaseModel
from models import EntrarSalaRequest



class EntrarSalaRequest(BaseModel):
    codigo: str
    nick: str

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/criar-sala")
def criar_sala():
    codigo = gerar_codigo()
    salas[codigo] = {
        "jogadores": []
    }
    return {
        "codigo": codigo
    }

@app.post("/entrar-sala")
def entrar_sala(dados: EntrarSalaRequest):

    if dados.codigo not in salas:
        return {
            "erro": "Sala não encontrada."
        }

    jogadores = salas[dados.codigo]["jogadores"]

    for jogador in jogadores:
        if jogador["nick"] == dados.nick:
            return {
                "erro": "Já existe um jogador com esse nick."
            }
    jogadores.append({
    "nick": dados.nick
})

    return {
    "mensagem": "Jogador entrou na sala!"
}


@app.get("/jogadores/{codigo}")
def listar_jogadores(codigo: str):

    if codigo not in salas:
        return {
            "erro": "Sala não encontrada."
        }

    return {
        "jogadores": salas[codigo]["jogadores"]
    }