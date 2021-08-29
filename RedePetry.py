from Lugar import Lugar

class RedePetry:
    def __init__(self):
        self.lugares = []
        self.transicoes = []

    def criarLugar(self, id, marcas):
        self.lugares.append(Lugar(id, marcas))
