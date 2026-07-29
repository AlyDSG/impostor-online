import random
import string

salas = {}

def gerar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))