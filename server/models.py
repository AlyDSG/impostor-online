from pydantic import BaseModel


class EntrarSalaRequest(BaseModel):
    codigo: str
    nick: str


class CriarSalaRequest(BaseModel):
    nick: str