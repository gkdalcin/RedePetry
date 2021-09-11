class Transicao:
    def __init__(self, id):
        self.id = id
        self.ativa = False
        self.conexoes = []