from RedePetry import RedePetry

#Criação da Rede
rp = RedePetry()
rp.criarLugar('L1',12)
rp.criarLugar('L2',0)
rp.criarLugar('L3',0)
rp.criarLugar('L4',3)
rp.criarTransicao('T1')
rp.criarTransicao('T2')
rp.criarConexao('T1','L1','L2',1)
rp.criarConexao('T2','L2','L3',3, type='inibidor')
rp.criarConexao('T2','L4','L3',1, type='reset')

#Loop de funcionamento da rede
continuar = True
aviso_input = "----------------------------------- Digite [1]Inserir Marcas [2]Remover Marcas [3]Sair "

while continuar:
    rp.imprimeRede()
    rp.imprimeAtributos()
    
    escolha = input(aviso_input)
    if escolha == "1":
        lugar_id = input("Qual o ID do lugar? ")
        quant_marcas = int(input("Quantas marcas? "))
        rp.insereMarcas(lugar_id, quant_marcas)
    elif escolha == "2":
        lugar_id = input("Qual o ID do lugar? ")
        quant_marcas = int(input("Quantas marcas? "))
        rp.removeMarcas(lugar_id, quant_marcas)
    elif escolha == "3": continuar = False
    else:
        rp.trocaMarcas()
        rp.checaTransicoes()