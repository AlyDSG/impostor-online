from pydantic import BaseModel


class EntrarSalaRequest(BaseModel):
    codigo: str
    nick: str