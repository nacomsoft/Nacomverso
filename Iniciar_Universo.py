
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
from Login import Personagem

class Universo:
    def __init__(self, usuario, lista_dados):
        self.personagem = Personagem(usuario)
        self.personagem.carregar_inicial(lista_dados)
        self.arma_equipada = self.personagem.proeficiencia_arma_principal
        self.mostrador = "VAZIO"
        self.inventario = ["VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO"]
        self.carregador_de_xp = 0
        self.rodando = True
        
    def retornar_dados_personagem(self):
        dados = self.personagem.retornar_dados()
        return dados

    def inicio(self):
        print("\n CARREGANDO... \n")
        print("Para executar comandos digite no inicio \"//\" \n")
        nome = str(negrito_ciano(self.personagem.nome))
        raca_classe = str(negrito_amarelo("["+ self.personagem.raca +"]["+ self.personagem.classe +"]"))
        dados_cabecalho = str(negrito_verde("[HP:"+ str(self.personagem.vida) +"][MP:"+ str(self.personagem.mana) +"][XP:"+ str(self.personagem.experiencia) +"]"))
        arma_principal = negrito_amarelo("[" + self.arma_equipada + "]")
        print("\n")
        while(self.rodando):
            nome = str(negrito_ciano(self.personagem.nome))
            raca_classe = str(negrito_amarelo("["+ self.personagem.raca +"]["+ self.personagem.classe +"]"))
            dados_cabecalho = str(negrito_verde("[HP:"+ str(self.personagem.vida) +"][MP:"+ str(self.personagem.mana) +"][XP:"+ str(self.personagem.experiencia) +"]"))
            arma_principal = negrito_amarelo("[" + self.arma_equipada + "]")
            self.mostrador = str(nome + raca_classe + dados_cabecalho + arma_principal)
            print(self.mostrador)
            acao = input()
            self.comandos(acao)
            self.carregador_de_xp += 1
            if(self.carregador_de_xp == 100):
                self.personagem.experiencia += 1
                self.carregador_de_xp = 0

    def sair_programa(self):
        print("Clique ENTER para sair")
        self.rodando = False
        sair = input()

    def comandos(self, comando):
        if(comando == "//comandos"):
            print(ciano("//comandos") + amarelo("//dados") + magenta("//inventario") + vermelho("//sair"))
        elif(comando == "//dados"):
            self.mostrar_dados()
        elif(comando == "//inventario"):
            self.mostrar_inventario()
        elif(comando == "//sair"):
            self.sair_programa()
        else:
            self.enviar_mensagem(self.mostrador + comando)
            

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
        campo = int(input())
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
            print("2. Descartar")
            print("3. Entregar")
            acao = int(input())
            if(acao == 1):
                arma_a_equipar = self.inventario[campo]
                arma_a_guardar = self.arma_equipada
                self.arma_equipada = arma_a_equipar
                self.inventario[campo] = arma_a_guardar
                print(azul("Equipamento Equipado"))
            elif(acao == 2):
                print(amarelo(self.inventario[campo] + " Descartado"))
                self.inventario[campo] = "VAZIO"
            elif(acao == 3):
                print(verde("Não há usuário ou local para entregar item"))
                #entregar equipamento
            else:
                print(vermelho("opção incalida"))



    def mostrar_dados(self):
        print(negrito_branco("AGILIDADE: ") + negrito_verde(str(self.personagem.agilidade)))
        print(negrito_branco("CARISMA: ") + negrito_verde(str(self.personagem.carisma)))
        print(negrito_branco("FORÇA: ") + negrito_verde(str(self.personagem.forca)))
        print(negrito_branco("INTELIGÊNCIA: ") + negrito_verde(str(self.personagem.inteligencia)))
        print(negrito_branco("MAGIA: ") + negrito_verde(str(self.personagem.magia)))
        print(negrito_branco("RESISTÊNCIA: ") + negrito_verde(str(self.personagem.resistencia)))
        print(negrito_branco("SORTE: ") + negrito_verde(str(self.personagem.sorte)))