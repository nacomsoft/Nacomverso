
#                     END OF TERMS AND CONDITIONS
#
#           How to Apply These Terms to Your New Programs
#
#  If you develop a new program, and you want it to be of the greatest
#possible use to the public, the best way to achieve this is to make it
#free software which everyone can redistribute and change under these terms.
#
#  To do so, attach the following notices to the program.  It is safest
#to attach them to the start of each source file to most effectively
#state the exclusion of warranty; and each file should have at least
#the "copyright" line and a pointer to where the full notice is found.
#
#    <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) <year>  <name of author>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#Also add information on how to contact you by electronic and paper mail.
#
#  If the program does terminal interaction, make it output a short
#notice like this when it starts in an interactive mode:
#
#    Nacomverso Copyright (C) 2022  NACOM by Grupo NCGP
#    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.
#
#The hypothetical commands `show w' and `show c' should show the appropriate
#parts of the General Public License.  Of course, your program's commands
#might be different; for a GUI interface, you would use an "about box".
#
# You should also get your employer (if you work as a programmer) or school,
#if any, to sign a "copyright disclaimer" for the program, if necessary.
#For more information on this, and how to apply and follow the GNU GPL, see
#<https://www.gnu.org/licenses/>.
#
#  The GNU General Public License does not permit incorporating your program
#into proprietary programs.  If your program is a subroutine library, you
#may consider it more useful to permit linking proprietary applications with
#the library.  If this is what you want to do, use the GNU Lesser General
#Public License instead of this License.  But first, please read
#<https://www.gnu.org/licenses/why-not-lgpl.html>.

from TextColor import*
import getpass

class Acesso:

    def __init__(self):
        self.usuario = "nome do usuario"
        self.senha = "senha do usuario"
        self.email = "email do usuario"

        self.sair_programa = False
    
        self.lista_de_sexos = ["Masculino", "Feminino"]
        self.lista_de_racas = ["Anão", "Bestial", "Draconato", "Elfo", "Espirito", "Fada", "Fluguel", "Halfling", "Humano", "Kitsune", "Lizardman", "Lobsomen", "Meio-Elfo", "Minotauro", "Neko", "Ogro", "Orcs", "Tanuki", "Tiefling", "Vampiro"]
        self.lista_de_classes = ["Arqueiro", "Assassino", "Bárbaro", "Clérigo", "Escudeiro", "Ladino", "Lanceiro", "Lutador", "Mago", "Paladino"]

        self.lista_classe_agilidade = [5, 30, 0, 0, 0, 30, 20, 20, 0, 0]
        self.lista_classe_forca = [0, 0, 30, 0, 5, 0, 30, 5, 0, 30]
        self.lista_classe_carisma = [0, 0, 0, 0, 0, 0, 5, 0, 0, 30]
        self.lista_classe_resistencia = [0, 0, 5, 0, 40, 0, 0, 5, 0, 5]
        self.lista_classe_inteligencia = [20, 5, 0, 30, 0, 5, 0, 20, 30, 5]
        self.lista_classe_magia = [0, 0, 0, 20, 0, 0, 0, 0, 30, 5]
        self.lista_classe_sorte = [30, 10, 0, 20, 0, 10, 20, 0, 0, 10]
        self.lista_classe_armaduras = ["Leve", "Nenhuma", "Média", "Média", "Todas", "Leve", "Média", "Nenhuma", "Nenhuma", "Todas"]
        self.lista_classe_armas = ["Facas", "Pequenas", "Simples", "Simples", "Pequenas", "Pequenas", "Simples", "Simples", "Disparadores", "Simples"]
        self.lista_classe_arma_principal = ["Arco", "Espada Curta", "Bastão", "Cajado de Clérigo", "Escudo", "Faca", "Lança", "Punhos", "Cajado de Mago", "Espada Longa"]
        self.lista_classe_ferramentas = ["Manutenção", "Limpeza", "Nenhuma", "Nenhuma", "Ferreiro", "Ladrão", "Nenhuma", "Artesanato", "Nenhuma", "Nenhuma"]
        self.lista_classe_vida = [6, 10, 12, 8, 15, 8, 8, 8, 6, 10]

        self.lista_raca_agilidade = [0, 20, 0, 20, 0, 20, 40, 20, 10, 0, 10, 20, 10, 0, 20, 0, 0, 20, 0, 30]
        self.lista_raca_forca = [0, 30, 20, 0, 40, 0, 30, 0, 10, 20, 10, 0, 0, 20, 0, 20, 20, 0, 0, 10]
        self.lista_raca_carisma = [0, 0, 10, 0, 0, 10, 10, 0, 10, 0, 0, 0, 20, 0, 20, 0, 0, 0, 20, 0]
        self.lista_raca_resistencia = [20, 0, 0, 0, 0, 0, 20, 0, 10, 0, 20, 0, 10, 20, 0, 0, 10, 20, 0, 0]
        self.lista_raca_inteligencia = [0, 0, 0, 10, 0, 0, 30, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0]
        self.lista_raca_magia = [0, 10, 30, 30, 40, 30, 30, 10, 10, 20, 20, 10, 20, 20, 30, 10, 0, 30, 30, 30]
        self.lista_raca_sorte = [30, 0, 0, 0, 20, 20, 0, 30, 10, 10, 0, 0, 20, 10, 30, 0, 0, 20, 0, 0]
        self.lista_raca_vida = [40, 20, 8, 7, 60, 60, 200, 15, 8, 60, 45, 12, 18, 40, 60, 10, 7, 25, 10, 200]
        self.lista_raca_mana = [20, 40, 90, 100, 100, 100, 100, 40, 30, 50, 70, 30, 70, 30, 50, 30, 20, 30, 70, 80]
        self.dados_personagem = []


    def menu_inicial(self):
        menu_repetidor = True
        while(menu_repetidor):
            print("\n\n#########################")
            print("##                     ##")
            print("##     " + negrito_azul("NACOMVERSO") + "      ##")
            print("##                     ##")
            print("#########################\n\n")
            print("         " + negrito_amarelo("Menu Inicial") +"\n")
            print("[1] Login")
            print("[2] Cadastrar\n")
            print("[3] Configurar Banco de Dados\n")
            menu_acesso = int(input())
            if(menu_acesso == 1):
                menu_repetidor = False
                self.menu_login()
            elif(menu_acesso == 2):
                menu_repetidor = False
                self.menu_cadastrar()
            elif(menu_acesso == 3):
                menu_repetidor = False
                self.configurar_banco_de_dados()
            else:
                print("Opção invalida, tente novamente")
                menu_repetidor = True

    def configurar_banco_de_dados(self):
        print(negrito_amarelo("Configurações de Servidor"))
        print("[1] Entrar em um servidor")
        print("[2] Criar um Nancomverso no seu servidor")
        
        #tipo 1
        print("selecione um servidor do seu sistema: ")

        #tipo 2
        print("Digite a URL do Servidor ou endereço de IP da rede de acesso")
        print("Digite o nome de usuário:")
        print("Digite a senha")
        print("Digite o nome do Banco de Dados")

    def menu_login(self):
        menu_login_repedidor = True
        while(menu_login_repedidor):
            print("\n\nDigite seu nome de usuário ou E-mail")
            self.usuario = input()
            print("Digite sua senha")
            self.senha = getpass.getpass()
            acesso = self.verificador_de_senha(self.usuario, self.senha)
            if(acesso):
                print(azul("login relizado com sucesso!"))
                menu_login_repedidor = False
                self.escolha_personagem()
            else:
                menu_login_repedidor2 = True     
                while(menu_login_repedidor2):
                    print(vermelho("senha ou usuário incorretos!"))
                    print("[1] Tentar novamente")
                    print("[2] Redefinir Senha")
                    senha_errada = int(input())
                    if(senha_errada == 1):
                        menu_login_repedidor = False
                        menu_login_repedidor2 = False
                        self.sair()
                    elif(senha_errada == 2):
                        menu_login_repedidor = True
                        menu_login_repedidor2 = False
                        self.redefinir_senha()
                    else:
                        print("Opção invalida, tente novamente")
                        menu_login_repedidor2 = True
                        menu_login_repedidor = True

    def verificador_de_senha(self, vusuario, vsenha):
        verificador = True
        return verificador    

    def redefinir_senha(self):
        print("funcao ainda não desenvolvida")
        self.sair()

    def escolha_personagem(self):
        a = True
        while(a):
            print("Não há personagem criado deseja criar? [s/n]:")
            resposta = input()
            if(resposta == "s"):
                a = False
                self.criar_personagem()
            elif(resposta == "n"):
                a = False
                self.sair()
            else:
                a = True

    def sair(self):
        self.sair_programa = True
        print("Clique ENTER para sair:")
        exit = input()

    def menu_cadastrar(self):
        print("\n\nDigite seu nome de usuário")
        criar_usuario = input()
        print("Digite seu endereço de email")
        criar_email = input()
        senha_nao_confirmada = True
        while(senha_nao_confirmada):
            print("Digite sua senha")
            criar_senha = str(getpass.getpass())
            print("Confirme sua senha")
            confirmar_senha = str(getpass.getpass())
            if(criar_senha == confirmar_senha):
                senha_nao_confirmada = False
            else:
                print(vermelho("As duas senhas não coincidem!"))
                senha_nao_confirmada = True
                print(vermelho("Tente novamente"))
        #Criar script para cadastrar no banco de dados
        print(azul("Conta criada com sucesso!"))
        self.criar_personagem()

    def criar_personagem(self):
        print("\n\n" + negrito_amarelo("Menu de Criação de personagem"))
        escreva_negrito_magenta("FASE 1")
        print("Defina o nome do seu personagem:")
        personagem_nome = str(input())
        print("Defina o Sexo do seu personagem:")
        print("[1] Masculino")
        print("[2] Feminino")
        s_sexo = int(input())
        s_sexo = s_sexo - 1
        personagem_sexo = self.lista_de_sexos[s_sexo]
        print("Defina a raça de seu personagem")
        print("[1] Anão\n[2] Bestial\n[3] Draconato\n[4] Elfo\n[5] Espirito\n[6] Fada\n[7] Fluguel\n[8] Halfling\n[9] Humano\n[10] Kitsune\n[11] Lizardman\n[12] Lobsomen\n[13] Meio-Elfo\n[14] Minotauro\n[15] Neko\n[16] Ogro\n[17] Orcs\n[18] Tanuki\n[19] Tiefling\n[20] Vampiro\n")
        s_raca = int(input())
        s_raca = s_raca - 1
        personagem_raca = self.lista_de_racas[s_raca]
        print("Defina a classe do seu personagem")
        print("[1] Arqueiro\n[2] Assassino\n[3] Bárbaro\n[4] Clérigo\n[5] Escudeiro\n[6] Ladino\n[7] Lanceiro\n[8] Lutador\n[9] Mago\n[10] Paladino\n")
        s_classe = int(input())
        s_classe = s_classe - 1
        personagem_classe = self.lista_de_classes[s_classe]

        personagem_agilidade = self.lista_classe_agilidade[s_classe] + self.lista_raca_agilidade[s_raca]
        personagem_forca = self.lista_classe_forca[s_classe] + self.lista_raca_forca[s_raca]
        personagem_carisma = self.lista_classe_carisma[s_classe] + self.lista_raca_carisma[s_raca]
        personagem_resistencia = self.lista_classe_resistencia[s_classe] + self.lista_raca_resistencia[s_raca]
        personagem_inteligencia = self.lista_classe_inteligencia[s_classe] + self.lista_raca_inteligencia[s_raca]
        personagem_magia = self.lista_classe_magia[s_classe] + self.lista_raca_magia[s_raca]
        personagem_sorte = self.lista_classe_sorte[s_classe] + self.lista_raca_sorte[s_raca]
        personagem_vida = self.lista_classe_vida[s_classe] + self.lista_raca_vida[s_raca]

        personagem_proeficiencia_armaduras = self.lista_classe_armaduras[s_classe]
        personagem_proeficiencia_armas = self.lista_classe_armas[s_classe]
        personagem_proeficiencia_arma_principal = self.lista_classe_arma_principal[s_classe]
        personagem_proeficiencia_ferramentas = self.lista_classe_ferramentas[s_classe]
        personagem_mana = self.lista_raca_mana[s_raca]
        personagem_experiencia = 0

        print("\n\n\n" + negrito_amarelo("Confirmando os dados"))
        print(negrito_ciano("Nome: ") + negrito_azul(personagem_nome))
        print(negrito_ciano("Sexo: ") + negrito_azul(personagem_sexo))
        print(negrito_ciano("Raça: ") + negrito_azul(personagem_raca))
        print(negrito_ciano("Classe: ") + negrito_azul(personagem_classe))
        print(negrito_ciano("MP: ") + negrito_vermelho(str(personagem_mana)))
        print(negrito_ciano("HP: ") + negrito_vermelho(str(personagem_vida)))
        print(negrito_ciano("XP: ") + negrito_vermelho(str(personagem_experiencia)))
        print(negrito_ciano("AGILIDADE: ") + negrito_azul(str(personagem_agilidade)))
        print(negrito_ciano("FORÇA: ") + negrito_azul(str(personagem_forca)))
        print(negrito_ciano("CARISMA: ") + negrito_azul(str(personagem_carisma)))
        print(negrito_ciano("RESISTÊNCIA: ") + negrito_azul(str(personagem_resistencia)))
        print(negrito_ciano("INTELIGÊNCIA: ") + negrito_azul(str(personagem_inteligencia)))
        print(negrito_ciano("MAGIA: ") + negrito_azul(str(personagem_magia)))
        print(negrito_ciano("SORTE: ") + negrito_azul(str(personagem_sorte)))
        print(negrito_ciano("Armaduras: ") + negrito_azul(personagem_proeficiencia_armaduras))
        print(negrito_ciano("Armas: ") + negrito_azul(personagem_proeficiencia_armas))
        print(negrito_ciano("Ferramentas: ") + negrito_azul(personagem_proeficiencia_ferramentas))
        print(negrito_ciano("Arma Principal: ") + negrito_azul(personagem_proeficiencia_arma_principal))
        self.dados_personagem = [personagem_nome, personagem_sexo, personagem_classe, personagem_raca, personagem_agilidade, personagem_forca, personagem_carisma, personagem_resistencia, personagem_inteligencia, personagem_magia, personagem_sorte, personagem_proeficiencia_armaduras, personagem_proeficiencia_armas, personagem_proeficiencia_arma_principal, personagem_proeficiencia_ferramentas, personagem_vida, personagem_mana, personagem_experiencia]
        
class Personagem:
    def __init__(self, ent_usuario):
        self.usuario = ent_usuario
        self.nome = "Vazio"
        self.sexos = "Vazio"
        self.classe = "Vazio"
        self.raca = "Vazio"

        self.agilidade = 0
        self.forca = 0
        self.carisma = 0
        self.resistencia = 0
        self.inteligencia = 0
        self.magia = 0
        self.sorte = 0
        self.proeficiencia_armaduras = "Vazio"
        self.proeficiencia_armas = "Vazio"
        self.proeficiencia_arma_principal = "Vazio"
        self.proeficiencia_ferramentas = "Vazio"
        self.vida = 0
        self.mana = 0
        self.experiencia = 0

    def carregar_inicial(self, lista_de_dados):
        self.nome = lista_de_dados[0]
        self.sexos = lista_de_dados[1]
        self.classe = lista_de_dados[2]
        self.raca = lista_de_dados[3]
        self.agilidade = lista_de_dados[4]
        self.forca = lista_de_dados[5]
        self.carisma = lista_de_dados [6]
        self.resistencia = lista_de_dados[7]
        self.inteligencia = lista_de_dados[8]
        self.magia = lista_de_dados[9]
        self.sorte = lista_de_dados[10]
        self.proeficiencia_armaduras = lista_de_dados[11]
        self.proeficiencia_armas = lista_de_dados[12]
        self.proeficiencia_arma_principal = lista_de_dados[13]
        self.proeficiencia_ferramentas = lista_de_dados[14]
        self.vida = lista_de_dados[15]
        self.mana = lista_de_dados[16]
        self.experiencia = lista_de_dados[17]        

    def retornar_dados(self):
        retorno = [self.nome, self.sexos, self.classe, self.raca, self.agilidade, self.forca, self.carisma, self.resistencia, self.inteligencia, self.magia, self.sorte, self.proeficiencia_armaduras, self.proeficiencia_armas, self.proeficiencia_arma_principal, self.proeficiencia_ferramentas, self.vida, self.mana, self.experiencia]
        return retorno
