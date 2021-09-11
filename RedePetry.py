from Lugar import Lugar
from Transicao import Transicao

class RedePetry:
    def __init__(self):
        self.lugares = []
        self.transicoes = []

    def criarLugar(self, id, marcas):
        self.lugares.append(Lugar(id, marcas))

    def getLugar(self,id):
        for i in range(0, len(self.lugares)):
            if self.lugares[i].id == id: return self.lugares[i]
    
    def removeLugar(self,id):
        for i in range(0, len(self.lugares)):
            if self.lugares[i].id == id:
               ind = i
               break
        del self.lugares[ind]
    
    def criarTransicao(self, id):
        self.transicoes.append(Transicao(id))
    
    def getTransicao(self,id):
        for i in range(0, len(self.transicoes)):
            if self.transicoes[i].id == id: return self.transicoes[i]
    
    def removeTransicao(self,id):
        for i in range(0, len(self.transicoes)):
            if self.transicoes[i].id == id:
               ind = i
               break
        del self.transicoes[ind]
    
    def criarConexao(self, transicao_id, entrada, saida, peso):
        transicao = self.getTransicao(transicao_id)
        transicao.conexoes.append([entrada,saida,peso])
    
    def trocaMarcas(self):
        for item in self.transicoes:
            if item.ativa:
                for conexao in item.conexoes:
                    entrada = self.getLugar(conexao[0])
                    saida = self.getLugar(conexao[1])
                    peso = conexao[2]
                    entrada.marcas -= peso
                    saida.marcas += peso

    
    def checaTransicoes(self):
        for item in self.transicoes:
            active = True
            for conexao in item.conexoes:
                entrada = self.getLugar(conexao[0])
                if entrada.marcas < conexao[2]: active = False
            item.ativa = active

    def imprimeRede(self):
        ids = ""
        for item in self.lugares:
            ids += item.id + " "
        for item in self.transicoes:
            ids += item.id + " "
        print(ids)
    
    def imprimeAtributos(self):
        atts = ""
        for item in self.lugares:
            atts += str(item.marcas) 
            if len(str(item.marcas))==1: atts += "  "
            elif len(str(item.marcas))==2: atts += " "
        for item in self.transicoes:
            if item.ativa: atts += "S  "
            else: atts += "N  "
        print(atts)