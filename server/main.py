from fastapi import FastAPI
from salas import salas, gerar_codigo
from models import EntrarSalaRequest, CriarSalaRequest



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
        "host":host
    }
    
    return {
        "codigo": codigo,
        "host":host
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
        "host": salas[codigo]["host"] 
    }