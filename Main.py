from RedePetry import RedePetry

#Criação da Rede
rp = RedePetry()
rp.criarLugar('L1',12)
rp.criarLugar('L2',0)
rp.criarTransicao('T1')
rp.criarConexao('T1','L1','L2',3)

#Imprime estado inicial
rp.imprimeRede()
rp.checaTransicoes()
rp.imprimeAtributos()

#Loop de funcionamento da rede
continuar = True
while continuar:
    rp.trocaMarcas()
    rp.checaTransicoes()
    rp.imprimeRede()
    rp.imprimeAtributos()
    if input("----------------------------------Digite 1 para sair: ") == "1": continuar = False