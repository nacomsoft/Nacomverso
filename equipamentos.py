import struct
from xml.dom.minidom import Element


class Equipamento:
    def __init__(self):
        self.nome = "VAZIO"
        self.tipo = "VAZIO"
        self.tipo_de_arma = "VAZIO"
        self.tipo_de_alcance_da_arma = "VAZIO"
        self.alcance_em_distancia = 0
        self.categoria = "VAZIO"
        self.tipo_de_dano = ["VAZIO"]
        self.potos_de_ativacao = 0
        self.classe_permitida = ["TODAS"]
        self.peso = 0
        self.tamanho = 0
        self.preco = 0
        self.dano = 0
        self.critico = 0
        self.municao = False
        self.projeteis = False
        self.tipo_projeteis = "VAZIO"
        self.projeteis_carregados = 0
        self.tempo_de_carregamento = 0
        self.escudo = False
        self.magia = False
        self.agrupamento = False
        self.quantidade_agrupada = 5

class Armas:
    def __init__(self):
        # Corpo a Corpo leves
        self.adaga = self.criador_arma("adaga", "arma simples", "arma leve", "corpo a corpo", 3, ["corte", "perfuracao"], 500, 35, 200, 25, 10)
        
        self.agulha_longa = self.criador_arma("agulha longa", "arma simples", "arma leve", "corpo a corpo", 0, ["perfuracao"], 250, 15, 5000, 25, 10)
        
        self.bota_com_lamina = self.criador_arma("bota com lamina", "arma simples", "arma leve", "corpo a corpo", 0, ["perfuracao"], 500, 45, 2500, 35, 10)
        
        self.espada_curta = self.criador_arma("espada curta", "arma simples", "arma leve", "corpo a corpo", 0, ["corte", "perfuracao"], 1000, 48, 1000, 35, 10)
        
        self.gladium = self.criador_arma("adaga", "arma simples", "arma leve", "corpo a corpo", 0, ["corte", "perfuracao"], 1000, 50, 1500, 35, 10)

        self.manopla = self.criador_arma("manopla", "arma simples", "arma leve", "corpo a corpo", 0, ["esmagamento"], 1000, 25, 500, 25, 8)

        self.cestus = self.criador_arma("cestus", "arma marcial", "arma leve", "corpo a corpo", 0, ["esmagamento"], 500, 40, 500, 10, 0) #peso, tamanho, custo, dano, crítico 

        self.escudo_leve = self.criador_arma("escudo leve", "arma marcial", "arma leve", "corpo a corpo", 0, ["esmagamento"], 3000, 100, 500, 25, 12) #peso, tamanho, custo, dano, crítico 
        self.escudo_leve.escudo = True

        self.machadinha = self.criador_arma("machadinha", "arma marcial", "arma leve", "corpo a corpo", 3, ["corte"], 3000, 100, 500, 35, 18) #peso, tamanho, custo, dano, crítico 

        self.martelo = self.criador_arma("martelo", "arma marcial", "arma leve", "corpo a corpo", 6, ["esmagamento"], 1000, 40, 100, 35, 12) #peso, tamanho, custo, dano, crítico 

        #corpo a corpo de uma mão
        self.bastao = self.criador_arma("bastao", "arma simples", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 2000, 100, 100, 30, 12)

        self.clava = self.criador_arma("clava", "arma simples", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 1500, 70, 1000, 30, 12)

        self.lanca = self.criador_arma("lanca", "arma simples", "arma de uma mao", "corpo a corpo", 6, ["perfuracao"], 1500, 180, 200, 30, 12)

        self.lanca_dori = self.criador_arma("lanca dori", "arma simples", "arma de uma mao", "corpo a corpo", 7, ["perfuracao"], 1700, 215, 500, 32, 13)

        self.maca = self.criador_arma("maça", "arma simples", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 6000, 25, 1200, 45, 18)

        self.espada_cimitarra = self.criador_arma("espada cimitarra", "arma simples", "arma de uma mao", "corpo a corpo", 0, ["corte"], 2000, 105, 1500, 35, 8) #peso, tamanho, custo, dano, crítico 

        self.escudo_pesado = self.criador_arma("escudo pesado", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 7000, 110, 1500, 35, 12) #peso, tamanho, custo, dano, crítico 
        self.escudo_pesado.escudo = True

        self.espada_de_cavaleiro = self.criador_arma("espada de cavaleiro", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["corte", "perfuracao"], 2000, 90, 1500, 45, 10) #peso, tamanho, custo, dano, crítico 

        self.machado_de_batalha = self.criador_arma("machado de batalha", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["corte"], 3000, 100, 1000, 45, 24) #peso, tamanho, custo, dano, crítico 

        self.maca_estrela = self.criador_arma("maca estrela", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 3000, 90, 1500, 50, 16) #peso, tamanho, custo, dano, crítico 

        self.martelo_de_guerra = self.criador_arma("martelo de guerra", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 2500, 120, 1200, 45, 24) #peso, tamanho, custo, dano, crítico

        self.tridente = self.criador_arma("tridente", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["perfuracao"], 2000, 180, 1500, 45, 16) #peso, tamanho, custo, dano, crítico

        #corpo a corpo duas maos
        self.lanca_sarissa = self.criador_arma("lanca sarissa", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["perfuracao"], 2500, 400, 2500, 65, 8)

        self.lanca_pique = self.criador_arma("lanca pique", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["perfuracao"], 5000, 600, 200, 45, 18) #peso, tamanho, custo, dano, crítico

        self.alabarda = self.criador_arma("alabarda", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["perfuracao", "corte"], 6000, 170, 1000, 55, 30) #peso, tamanho, custo, dano, crítico

        self.espada_longa = self.criador_arma("espada longa", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["perfuracao", "corte"], 3000, 110, 5000, 70, 10) #peso, tamanho, custo, dano, crítico

        self.foice = self.criador_arma("foice", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["corte"], 2000, 110, 1800, 50, 32) #peso, tamanho, custo, dano, crítico

        self.machado_grande = self.criador_arma("machado grande", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["corte"], 6000, 150, 2000, 65, 36) #peso, tamanho, custo, dano, crítico

        self.marreta = self.criador_arma("marreta", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["esmagamento"], 8000, 150, 2000, 75, 24) #peso, tamanho, custo, dano, crítico

        #ataque a distância
        self.acido = self.criador_arma("acido", "arma simples", "arma leve", "distancia", 3, ["contato"], 500, 20, 1000, 50, 0)
        self.acido.agrupamento = True

        self.agua_benta = self.criador_arma("agua benta", "arma simples", "arma leve", "distancia", 3, ["contato"], 500, 20, 2500, 70, 0)
        self.agua_benta.agrupamento = True

        self.arco_curto = self.criador_arma("arco curto", "arma simples", "arma de duas maos", "distancia", 12, ["perfuracao"], 1000, 100, 3000, 35, 18)
        self.arco_curto.projeteis = True
        self.arco_curto.projeteis_carregados = 1
        self.arco_curto.tipo_projeteis = "flecha"
        
        self.azagaia = self.criador_arma("azagaia", "arma simples", "arma de duas maos", "distancia", 9, ["perfuracao"], 1000, 120, 100, 35, 12)
        self.azagaia.agrupamento = True

        self.explosivo = self.criador_arma("explosivo", "arma simples", "arma leve", "distancia", 10, ["area"], 1000, 30, 5000, 65, 0)
        self.explosivo.agrupamento = True

        self.besta_leve = self.criador_arma("besta leve", "arma simples", "arma de duas maos", "distancia", 18, ["perfuracao"], 3000, 70, 3500, 45, 10)
        self.besta_leve.projeteis = True
        self.besta_leve.projeteis_carregados = 1
        self.besta_leve.tipo_projeteis = "virote"

        self.besta_pesada = self.criador_arma("besta pesada", "arma marcial", "arma de duas maos", "distancia", 27, ["perfuracao"], 4000, 100, 5000, 65, 10)
        self.besta_leve.projeteis = True
        self.besta_leve.projeteis_carregados = 1
        self.besta_leve.tipo_projeteis = "virote"
        
        self.funda = self.criador_arma("funda", "arma simples", "arma leve", "distancia", 15, ["esmagamento"], 250, 30, 100, 25, 8)
        self.funda.projeteis = True
        self.funda.projeteis_carregados = 1
        self.funda.tipo_projeteis = "bala"
        
        self.arco_longo = self.criador_arma("arco longo", "arma simples", "arma leve", "distancia", 24, ["perfuracao"], 1500, 150, 7500, 45, 24)
        self.arco_longo.projeteis = True
        self.arco_longo.projeteis_carregados = 1
        self.arco_longo.tipo_projeteis = "flecha"

        self.felcha = self.criador_projeteis("flecha")
        self.bala = self.criador_projeteis("bala")
        self.virote = self.criador_projeteis("virote")

        #CLASSES ARMAS

        self.classe_arco = self.criador_arma("Arco", "arma simples", "arma leve", "distancia", 24, ["perfuracao"], 1500, 150, 7500, 45, 24)
        self.classe_arco.projeteis = True
        self.classe_arco.projeteis_carregados = 1
        self.classe_arco.tipo_projeteis = "flecha"

        self.classe_espada_curta =  self.criador_arma("Espada Curta", "arma simples", "arma leve", "corpo a corpo", 0, ["corte", "perfuracao"], 1000, 48, 1000, 35, 10)

        self.classe_bastao =  self.criador_arma("Bastao", "arma simples", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 2000, 100, 100, 30, 12)

        self.classe_cajado_clerigo = self.criador_arma("Cajado de Clérigo", "arma magica", "arma magica","distancia", 10, ["Magico"], 1500, 150, 1500, 10, 0)
        self.classe_cajado_clerigo.magia = True

        self.classe_escudo = self.criador_arma("Escudo", "arma marcial", "arma de uma mao", "corpo a corpo", 0, ["esmagamento"], 7000, 110, 1500, 35, 12) #peso, tamanho, custo, dano, crítico 
        self.classe_escudo.escudo = True
        
        self.classe_faca = self.criador_arma("Faca", "arma simples", "arma leve", "corpo a corpo", 3, ["corte", "perfuracao"], 500, 25, 200, 25, 10)
        
        self.classe_lanca = self.criador_arma("Lança", "arma simples", "arma de uma mao", "corpo a corpo", 6, ["perfuracao"], 1500, 180, 200, 30, 12)
        
        self.classe_punhos = self.criador_arma("Punhos", "arma marcial", "arma leve", "corpo a corpo", 0, ["esmagamento"], 500, 40, 500, 10, 0) #peso, tamanho, custo, dano, crítico
        
        self.classe_cajado_mago = self.criador_arma("Cajado de Mago", "arma magica", "arma magica","distancia", 10, ["Magico"], 1500, 150, 1500, 10, 0)
        self.classe_cajado_mago.magia = True
        
        self.classe_espada_longa = self.criador_arma("Espada Longa", "arma simples", "arma de duas maos", "corpo a corpo", 0, ["perfuracao", "corte"], 3000, 110, 5000, 70, 10) #peso, tamanho, custo, dano, crítico

    def criador_arma(self, nome, tipo, tipo_de_arma, tipo_de_alcance_da_arma, alcance_em_distancia, tipo_de_dano, peso, tamanho, preco, dano, critico):
        arma = Equipamento()
        arma.nome = nome
        arma.tipo = tipo
        arma.tipo_de_arma = tipo_de_arma
        arma.tipo_de_alcance_da_arma = tipo_de_alcance_da_arma
        arma.alcance_em_distancia = alcance_em_distancia
        arma.tipo_de_dano = tipo_de_dano
        arma.peso = peso
        arma.tamanho = tamanho
        arma.preco = preco
        arma.dano = dano
        arma.critico = critico
        return arma

    def criador_projeteis(self, nome):
        municao = Equipamento()
        municao.nome = nome
        municao.municao = True
        municao.projeteis_carregados = 5
        municao.tipo = "municao"
        municao.preco = 25

        return municao



class Loja:
    
    def __init__(self):
        self.armamento = Armas()
        self.cardapio = [Equipamento()]
        self.lojinha()

    def lojinha(self):
        self.cardapio = [self.armamento.adaga]
        self.cardapio += [self.armamento.agulha_longa]
        self.cardapio += [self.armamento.bota_com_lamina]
        self.cardapio += [self.armamento.espada_curta]
        self.cardapio += [self.armamento.gladium]
        self.cardapio += [self.armamento.manopla]
        self.cardapio += [self.armamento.cestus]
        self.cardapio += [self.armamento.escudo_leve]
        self.cardapio += [self.armamento.machadinha]
        self.cardapio += [self.armamento.martelo]
        self.cardapio += [self.armamento.bastao]
        self.cardapio += [self.armamento.clava]
        self.cardapio += [self.armamento.lanca]
        self.cardapio += [self.armamento.lanca_dori]
        self.cardapio += [self.armamento.maca]
        self.cardapio += [self.armamento.espada_cimitarra]
        self.cardapio += [self.armamento.escudo_pesado]
        self.cardapio += [self.armamento.espada_de_cavaleiro]
        self.cardapio += [self.armamento.machado_de_batalha]
        self.cardapio += [self.armamento.maca_estrela]
        self.cardapio += [self.armamento.martelo_de_guerra]
        self.cardapio += [self.armamento.tridente]
        self.cardapio += [self.armamento.lanca_sarissa]
        self.cardapio += [self.armamento.lanca_pique]
        self.cardapio += [self.armamento.alabarda]
        self.cardapio += [self.armamento.espada_longa]
        self.cardapio += [self.armamento.foice]
        self.cardapio += [self.armamento.machado_grande]
        self.cardapio += [self.armamento.marreta]
        self.cardapio += [self.armamento.acido]
        self.cardapio += [self.armamento.agua_benta]
        self.cardapio += [self.armamento.arco_curto]
        self.cardapio += [self.armamento.azagaia]
        self.cardapio += [self.armamento.explosivo]
        self.cardapio += [self.armamento.besta_leve]
        self.cardapio += [self.armamento.besta_pesada]
        self.cardapio += [self.armamento.funda]
        self.cardapio += [self.armamento.arco_longo]
        self.cardapio += [self.armamento.felcha]
        self.cardapio += [self.armamento.bala]
        self.cardapio += [self.armamento.virote]

    def shopping(self, mostrador, dinheiro, inventario):
        self.lojinha()
        numero = len(self.cardapio)
        cifrao = str(" NS$ ")
        nome = str()
        preco = int()
        spreco = str()
        valor = [str()]
        while(numero > 0):
            numero -= 1
            nome = self.cardapio[numero].nome
            preco = self.cardapio[numero].preco
            spreco = str(preco)
            valor += [str(numero) + "." + nome + cifrao + spreco]

        numero = len(valor)
        while(numero > 0):
            numero -= 1
            print(valor[numero])
        print('Escolha uma opção\nEscreva "sair" para sair')
        print(mostrador)
        resposta = str(input())
        
        
        equipamento = str()
        dados_equipamento = Equipamento()
        porta_do_inventario = int()
        gravar_alteracoes = False

        if(self.verificador_inteiro(resposta)):
            if((int(resposta) > -1) and (int(resposta) < 41)):
                if(dinheiro >= self.cardapio[int(resposta)].preco):
                    porta_do_inventario = self.verificador_de_inventario(inventario)
                    if(porta_do_inventario >= 0):
                        dinheiro = dinheiro - self.cardapio[int(resposta)].preco
                        inventario[porta_do_inventario] = self.cardapio[int(resposta)].nome
                        gravar_alteracoes = True
                        dados_equipamento = self.cardapio[int(resposta)]
                        retorno = [gravar_alteracoes, equipamento, dados_equipamento, dinheiro, porta_do_inventario, inventario]
                    else:
                        print("inventario cheio")
                        retorno = self.shopping(mostrador, dinheiro, inventario)   
                          
                else:
                    print("Dinheiro Insuficiente")
                    retorno = self.shopping(mostrador, dinheiro, inventario)

        return retorno
        
    def verificador_inteiro(self, termo):
        if(termo == "0"):
            resultado = True
        elif(termo == "1"):
            resultado = True
        elif(termo == "2"):
            resultado = True
        elif(termo == "3"):
            resultado = True
        elif(termo == "4"):
            resultado = True
        elif(termo == "5"):
            resultado = True
        elif(termo == "6"):
            resultado = True
        elif(termo == "7"):
            resultado = True
        elif(termo == "8"):
            resultado = True
        elif(termo == "9"):
            resultado = True
        elif(termo == "10"):
            resultado = True
        elif(termo == "11"):
            resultado = True
        elif(termo == "12"):
            resultado = True
        elif(termo == "13"):
            resultado = True
        elif(termo == "14"):
            resultado = True
        elif(termo == "15"):
            resultado = True
        elif(termo == "16"):
            resultado = True
        elif(termo == "17"):
            resultado = True
        elif(termo == "18"):
            resultado = True
        elif(termo == "19"):
            resultado = True
        elif(termo == "20"):
            resultado = True
        elif(termo == "21"):
            resultado = True
        elif(termo == "22"):
            resultado = True
        elif(termo == "23"):
            resultado = True
        elif(termo == "24"):
            resultado = True
        elif(termo == "25"):
            resultado = True
        elif(termo == "26"):
            resultado = True
        elif(termo == "27"):
            resultado = True
        elif(termo == "28"):
            resultado = True
        elif(termo == "29"):
            resultado = True
        elif(termo == "30"):
            resultado = True
        elif(termo == "31"):
            resultado = True
        elif(termo == "32"):
            resultado = True
        elif(termo == "33"):
            resultado = True
        elif(termo == "34"):
            resultado = True
        elif(termo == "35"):
            resultado = True
        elif(termo == "36"):
            resultado = True
        elif(termo == "37"):
            resultado = True
        elif(termo == "38"):
            resultado = True
        elif(termo == "39"):
            resultado = True
        elif(termo == "40"):
            resultado = True
        elif(termo == "41"):
            resultado = True
        elif(termo == "42"):
            resultado = True
        elif(termo == "43"):
            resultado = True
        elif(termo == "44"):
            resultado = True
        elif(termo == "45"):
            resultado = True
        elif(termo == "46"):
            resultado = True
        elif(termo == "47"):
            resultado = True
        elif(termo == "48"):
            resultado = True
        elif(termo == "49"):
            resultado = True
        elif(termo == "50"):
            resultado = True
        else:
            resultado = False
        return resultado

    def verificador_de_inventario(self, inventario):
        numero = len(inventario)
        escolhido = -1
        while(numero > 0):
            numero -= 1
            if(inventario[numero] == "VAZIO"):
                escolhido = numero
        return escolhido

