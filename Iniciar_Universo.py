
from TextColor import*
from equipamentos import *
from Login import Personagem

class Universo:
    def __init__(self, usuario, lista_dados):
        self.personagem = Personagem(usuario)
        self.personagem.carregar_inicial(lista_dados)
        self.arma_equipada = self.personagem.proeficiencia_arma_principal
        self.arma_equipada_dados = Equipamento()
        self.arma_equipada_dados = self.personagem.arma_dados

        self.arma_secundaria_ativa = True
        self.arma_secundaria = "VAZIO"
        self.arma_secundaria_dados = Equipamento()
        self.texto_secundaria = "["+ self.arma_secundaria +"]"
        
        if(self.arma_equipada_dados.tipo_de_arma == "arma de duas maos"):
            self.arma_secundaria_ativa = False
            self.texto_secundaria = "..."
        else:
            if(self.arma_secundaria == "VAZIO"):
                self.texto_secundaria = "[...]" 
        
        self.mostrador = "VAZIO"
        self.inventario = ["VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO"]
        self.menu = ["VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO"]
        self.carregador_de_xp = 0
        self.rodando = True
        self.detector_de_dialogo = False
        self.inventario_equipamento = [Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento(), Equipamento()]
        self.dinheiro = 1000

    def retornar_dados_personagem(self):
        dados = self.personagem.retornar_dados()
        return dados

    def inicio(self):
        print("\n CARREGANDO... \n")
        print("Para executar comandos digite no inicio \"//\" \n")
        nome = str(negrito_ciano(self.personagem.nome))
        raca_classe = str(negrito_amarelo("["+ self.personagem.raca +"]["+ self.personagem.classe +"]"))
        dados_cabecalho = str(negrito_verde("[HP:"+ str(self.personagem.vida) +"][MP:"+ str(self.personagem.mana) +"][XP:"+ str(self.personagem.experiencia) +"]"))
        arma_principal = negrito_amarelo("[" + self.arma_equipada + "]" + self.texto_secundaria)
        print("\n")
        while(self.rodando):
            nome = str(negrito_ciano(self.personagem.nome))
            raca_classe = str(negrito_amarelo("["+ self.personagem.raca +"]["+ self.personagem.classe +"][NS$" + str(self.dinheiro) + "]"))
            dados_cabecalho = str(negrito_verde("[HP:"+ str(self.personagem.vida) +"][MP:"+ str(self.personagem.mana) +"][XP:"+ str(self.personagem.experiencia) +"]"))
            arma_principal = negrito_amarelo("[" + self.arma_equipada + "]" + self.texto_secundaria)
            self.mostrador = str(nome + raca_classe + dados_cabecalho + arma_principal)
            print(self.mostrador)
            acao = input()
            self.comandos(acao)
            self.dialogo(acao)
            self.carregador_de_xp += 1
            if(self.carregador_de_xp == 100):
                self.personagem.experiencia += 1
                self.carregador_de_xp = 0

    def dialogo(self, comando):
        if(self.detector_de_dialogo == True):
            print("Dialogo")

    def sair_programa(self):
        print("Clique ENTER para sair")
        self.rodando = False
        sair = input()

    def comandos(self, comando):
        if(comando == "//comandos"):
            print(ciano("//comandos") + amarelo("//dados") + magenta("//inventario") + vermelho("//sair") + ciano("//menu-game"))
        elif(comando == "//dados"):
            self.mostrar_dados()
        elif(comando == "//inventario"):
            self.mostrar_inventario()
        elif(comando == "//sair"):
            self.sair_programa()
        elif(comando == "//menu-game"):
            self.menu_game()
        elif(comando == "//loja"):
            self.loja()
        
        else:
            self.enviar_mensagem(self.mostrador + comando)
    
    def loja(self):
        organizacao = [bool(False), str("VAZIO"), Equipamento(), self.dinheiro, int(-1), self.inventario]
        menu_loja = Loja()
        organizacao = menu_loja.shopping(self.mostrador, self.dinheiro, self.inventario)
        if(organizacao[0] == True):
            self.inventario = organizacao[5]
            self.inventario_equipamento[int(organizacao[4])] = organizacao[2]
            self.dinheiro = int(organizacao[3])
            print(str(organizacao[1]) + " Foi comprado com sucesso!!!")

    def menu_game(self):
        print(negrito_branco("================[ MENU ]==============="))
        print(negrito_branco(" 0["+self.menu[0]+"]  5["+self.menu[5]+"] 10["+self.menu[10]+"]"))
        print(negrito_branco(" 1["+self.menu[1]+"]  6["+self.menu[6]+"] 11["+self.menu[11]+"]"))
        print(negrito_branco(" 2["+self.menu[2]+"]  7["+self.menu[7]+"] 12["+self.menu[12]+"]"))
        print(negrito_branco(" 3["+self.menu[3]+"]  8["+self.menu[8]+"] 13["+self.menu[13]+"]"))
        print(negrito_branco(" 4["+self.menu[4]+"]  9[V"+self.menu[9]+"] 14["+self.menu[14]+"]"))
        print(amarelo("Digite o número do campo ou digite outra coisa para sair"))
        valor = input()
        if(valor == ""):
            valor = 12345678
        campo = int(valor)
        if((campo >= 0) and (campo <= 19)):
            self.abrir_menu(campo)
    def abrir_menu(self, campo):
        print("Menu Game")

    def enviar_mensagem(self, controle):
        enviar = controle

    def mostrar_inventario(self):
        print(negrito_branco("=============[ INVENTARIO ]============"))
        print(negrito_branco(" 0["+self.inventario[0]+"]  5["+self.inventario[5]+"] 10["+self.inventario[10]+"] 15["+self.inventario[15]+"]"))
        print(negrito_branco(" 1["+self.inventario[1]+"]  6["+self.inventario[6]+"] 11["+self.inventario[11]+"] 16["+self.inventario[16]+"]"))
        print(negrito_branco(" 2["+self.inventario[2]+"]  7["+self.inventario[7]+"] 12["+self.inventario[12]+"] 17["+self.inventario[17]+"]"))
        print(negrito_branco(" 3["+self.inventario[3]+"]  8["+self.inventario[8]+"] 13["+self.inventario[13]+"] 18["+self.inventario[18]+"]"))
        print(negrito_branco(" 4["+self.inventario[4]+"]  9[V"+self.inventario[9]+"] 14["+self.inventario[14]+"] 19["+self.inventario[19]+"]"))
        print(amarelo("Digite o número do campo ou digite outra coisa para sair"))
        valor = input()
        if(valor == ""):
            valor = 12345678
        campo = int(valor)
        if((campo >= 0) and (campo <= 19)):
            self.abrir_campo(campo)
        
    def abrir_campo(self, campo):
        recebido = self.inventario[campo]
        if(recebido == "VAZIO"):
            print(vermelho("Não há nada alocado nesse campo"))
        else:

            print(recebido)
            print("O que deseja executar?")
            print("1. Equipar como principal")
            print("2. Equipar como secundaria")
            print("3. Descartar")
            print("4. Entregar")
            
            acao = input()
            
            equipamento_1 = Equipamento()
            equipamento_2 = Equipamento()

            if(acao == "1"):
                arma_a_equipar = self.inventario[campo]
                equipamento_1 = self.inventario_equipamento[campo]
                equipar = False
                if(equipamento_1.tipo_de_arma == "arma de duas maos"):
                    if(self.arma_secundaria_dados.nome != "VAZIO"):
                        porta = self.verificador_de_inventario()
                        if(porta == -1):
                            print("Impossivel equipar equipamento, inventário cheio!!!")
                        else:
                            self.inventario[porta] = self.arma_secundaria
                            self.inventario_equipamento[porta] = self.arma_secundaria_dados
                            self.arma_secundaria_ativa = False
                            self.texto_secundaria = "..."
                            equipar = True
                else:
                    equipar = True
                if(equipar):
                    arma_a_guardar = self.arma_equipada
                    equipamento_2 = self.arma_equipada_dados
                    self.arma_equipada = arma_a_equipar
                    self.arma_equipada_dados = equipamento_1
                    self.inventario[campo] = arma_a_guardar
                    self.inventario_equipamento[campo] = equipamento_2
                    print(azul("Equipamento Equipado"))

            elif(acao == "2"):
                arma_a_equipar = self.inventario[campo]
                equipamento_1 = self.inventario_equipamento[campo]

                if(equipamento_1.tipo_de_arma == "arma de duas maos"):
                    print("Impossivel Equipar arma de duas mãos como arma secundaria")
                else:
                    if(self.arma_equipada_dados.tipo_de_arma == "arma de duas maos"):
                        print("Impossivel equipar, pois arma de duas mãos está equipada")
                    else:
                        arma_a_guardar = self.arma_secundaria
                        equipamento_2 = self.arma_secundaria_dados
                        self.arma_secundaria = arma_a_equipar
                        self.arma_secundaria_dados = equipamento_1
                        self.inventario[campo] = arma_a_guardar
                        self.inventario_equipamento[campo] = equipamento_2
                        print(azul("Equipamento Equipado"))
            elif(acao == "3"):
                print("Tem certeza que deseja descartar esse item? [s/n]")
                resposta = input()
                if(resposta == "s"):
                    print(amarelo(self.inventario[campo] + " Descartado"))
                    self.inventario[campo] = "VAZIO"
            elif(acao == "4"):
                print(verde("Não há usuário ou local para entregar item"))
                #entregar equipamento
            else:
                print(vermelho("opção invalida"))

    def verificador_de_inventario(self):
        numero = len(self.inventario)
        escolhido = -1
        while(numero > 0):
            numero -= 1
            if(self.inventario[numero] == "VAZIO"):
                escolhido = numero
        return escolhido

    def mostrar_dados(self):
        print(negrito_branco("AGILIDADE: ") + negrito_verde(str(self.personagem.agilidade)))
        print(negrito_branco("CARISMA: ") + negrito_verde(str(self.personagem.carisma)))
        print(negrito_branco("FORÇA: ") + negrito_verde(str(self.personagem.forca)))
        print(negrito_branco("INTELIGÊNCIA: ") + negrito_verde(str(self.personagem.inteligencia)))
        print(negrito_branco("MAGIA: ") + negrito_verde(str(self.personagem.magia)))
        print(negrito_branco("RESISTÊNCIA: ") + negrito_verde(str(self.personagem.resistencia)))
        print(negrito_branco("SORTE: ") + negrito_verde(str(self.personagem.sorte)))