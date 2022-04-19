#  If the program does terminal interaction, make it output a short
#notice like this when it starts in an interactive mode:
#
#    decentralized-database Copyright (C) 2022 Osvaldo Lucas da Silva Figueiredo
#    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.
#
#The hypothetical commands `show w' and `show c' should show the appropriate
#parts of the General Public License.  Of course, your program's commands
#might be different; for a GUI interface, you would use an "about box".
#
#  You should also get your employer (if you work as a programmer) or school,
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


from cryptography.fernet import Fernet 
from datetime import datetime
from Identificador import Identificador_de_Bloco



class Criador_de_Blocos:
    def __init__(self):
        self.indice = Identificador_de_Bloco()
        self.chave_criacao = self.indice.gerar_validador()
        self.arquivo = []
        self.chave_cripto = Fernet.generate_key()
        self.encriptador = Fernet(self.chave_cripto)

    def criar(self):
        primeiro_indice = self.indice.bloco_genesis
        rota = self.chave_criacao.split("-")
        falso = rota[0] + "-" + "FALSO" + "-" + rota[1]
        bloco_completo = self.criar_bloco(falso, primeiro_indice, "INICIALIZADOR")
        
        arquivo_genesis = self.encriptador.encrypt(bloco_completo.encode())
        valor = arquivo_genesis
        self.arquivo = [valor]

    def criar_bloco(self, indice_anterior, indice_atual, arquivo):
        hora_atual = datetime.utcnow().timestamp()
        data = str(indice_anterior) + ";" + str(indice_atual) + ";" + str(hora_atual) + ";" + str(arquivo)
        return data

    def descriptar_bloco(self, bloco):
        bloco_desencriptado_byte = self.encriptador.decrypt(bloco)
        bloco_desencriptado = bloco_desencriptado_byte.decode()
        bloco_anterior_dados = bloco_desencriptado.split(";")
        bloco_de_fato = bloco_anterior_dados[3]
        return bloco_de_fato

    def getChaveCripto(self):
        return self.chave_cripto
    
    def novo_bloco(self, arquivo):
        indicelista = len(self.arquivo) - 1
        bloco_anterior = self.arquivo[indicelista]
        bloco_anterior_desencriptado_byte = self.encriptador.decrypt(bloco_anterior)
        bloco_anterior_desencriptado = bloco_anterior_desencriptado_byte.decode()
        bloco_anterior_dados = bloco_anterior_desencriptado.split(";")
        bloco_anterior_ind = bloco_anterior_dados[1]
        indice_bloco = self.indice.bloco_secundario()
        bloco_completo = self.criar_bloco(bloco_anterior_ind, indice_bloco, arquivo)
        
        arquivo_bloco = [self.encriptador.encrypt(bloco_completo.encode())]
        self.arquivo += arquivo_bloco

    def armazenar_dados_locais(self, arquivo_crypto, arquivo_indices):
        armazenamento_crypto = open(arquivo_crypto, "a")
        armazenamento_crypto.writelines(self.arquivo)
        aramazenamento_indices = open(arquivo_indices, "a")
        lista_de_indices = self.indice.getBlocos_Criados()
        aramazenamento_indices.writelines(lista_de_indices)

    def recuperar_dados_locais(self, arquivo_crypto, arquivo_indices):
        armazenamento_crypto = open(arquivo_crypto, "r")
        self.arquivo = armazenamento_crypto.readlines()
        aramazenamento_indices = open(arquivo_indices, "r")
        self.indice.blocos_Criados = aramazenamento_indices.readlines()
    
    
    def exibir_arquivo(self, indice_primario):
        print("raro", indice_primario)

    def verificar_igualdade(self):
        print("d")

    



