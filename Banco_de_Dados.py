
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

from Gerador_de_Blocos import*

class Gerador_Banco:
    def __init__(self):
        self.usuarios = Criador_de_Blocos()
        self.conector = Criador_de_Blocos()
        self.personagens = Criador_de_Blocos()
        self.espacos = Criador_de_Blocos()
        self.objetos = Criador_de_Blocos()
        self.logsistema = Criador_de_Blocos()
        self.chaves_criptografadas = []
        self.chaves_de_ativacao = []

    def criar(self):
        self.usuarios.criar()
        self.chaves_criptografadas[0] = self.usuarios.chave_cripto
        self.chaves_de_ativacao[0] = self.usuarios.chave_criacao
        self.conector.criar()
        self.chaves_criptografadas[1] = self.conector.chave_cripto
        self.chaves_de_ativacao[1] = self.conector.chave_criacao
        self.personagens.criar()
        self.chaves_criptografadas[2] = self.personagens.chave_cripto
        self.chaves_de_ativacao[2] = self.personagens.chave_criacao
        self.espacos.criar()
        self.chaves_criptografadas[3] = self.espacos.chave_cripto
        self.chaves_de_ativacao[3] = self.espacos.chave_criacao
        self.objetos.criar()
        self.chaves_criptografadas[4] = self.objetos.chave_cripto
        self.chaves_de_ativacao[4] = self.objetos.chave_criacao
        self.logsistema.criar()
        self.chaves_criptografadas[5] = self.logsistema.chave_cripto
        self.chaves_de_ativacao[5] = self.logsistema.chave_criacao


#USUÁRIOS

# Modelo: "usuario"><"E-mail"><"Senha"

#CLIENTES-Servidores

# Modelo: "IP4 do Cliente"><"IP6 do Cliente"><"Dados"><"usuario"

#PERSONAGENS

# Modelo: Nome"><"Sexo"><"Raça"><"Classe"><"MP"><"HP"><"XP"><"AGILIDADE"><"FORÇA"><"CARISMA"><"RESISTÊNCIA"><"INTELIGÊNCIA"><"MAGIA"><"SORTE"><"Armaduras"><"Armas"><"Ferramentas"><"Arma Principal"><"usuario"

#CYBER ESPAÇOS


# Modelo: "Nome do Lugar"><"tipo"><"pisos"><"comprimento_dos_pisos"><"largura_dos_pisos"><"Capacidade_de_Armazenamento"><"usuario"

#OBJETOS

# Modelo: "Nome do Objeto"><"Descrição"><"usuario"

#LOGS

# Modelo de logs: LOG><dado



