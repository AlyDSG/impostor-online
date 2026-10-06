from pydantic import BaseModel


class EntrarSalaRequest(BaseModel):
    codigo: str
    nick: str


class CriarSalaRequest(BaseModel):
    nick: str

class SairSalaRequest(BaseModel):
    codigo: str
    nick: str

class IniciarJogoRequest(BaseModel):
    codigo: str
    nick: str

class EnviarPalavraRequest(BaseModel):
    codigo: str
    nick: str
    palavra: str

