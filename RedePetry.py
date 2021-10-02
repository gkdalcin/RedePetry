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
    
    def criarConexao(self, transicao_id, entrada, saida, peso, type="default"):
        transicao = self.getTransicao(transicao_id)
        transicao.conexoes.append([entrada,saida,peso,type])
    
    def trocaMarcas(self):
        for item in self.transicoes:
            if item.ativa:
                for conexao in item.conexoes:
                    entrada = self.getLugar(conexao[0])
                    saida = self.getLugar(conexao[1])
                    peso = conexao[2]
                    if conexao[3] == 'default':
                        entrada.marcas -= peso
                        saida.marcas += peso
                    elif conexao[3] == 'inibidor' and entrada.marcas > 0:
                        entrada.marcas -= 1
                        saida.marcas += 1
                    elif conexao[3] == 'reset':
                        saida.marcas += entrada.marcas
                        entrada.marcas = 0
                        
    
    def insereMarcas(self, id, marcas):
        lugar = self.getLugar(id)
        lugar.marcas += marcas
    
    def checaTransicoes(self):
        for item in self.transicoes:
            active = True
            for conexao in item.conexoes:
                entrada = self.getLugar(conexao[0])
                if conexao[3] in ['default','reset'] and entrada.marcas < conexao[2]: active = False
                elif conexao[3] == 'inibidor' and (entrada.marcas == 0 or entrada.marcas >= conexao[2]): active = False
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