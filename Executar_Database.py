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


from Gerador_de_Blocos import*
from funcoes_extras import conversor_list

def principal():
    #USUÁRIOS
    usuarios = Criador_de_Blocos()
    usuarios.criar()
    # Modelo: "usuario"><"E-mail"><"Senha"
    usuarios.novo_bloco("usuario1><usuario1@email.com><senha do usuario1")
    usuarios.novo_bloco("usuario2><usuario2@email.com><senha do usuario2")
    print(usuarios.descriptar_bloco(usuarios.arquivo[0]))
    print(usuarios.descriptar_bloco(usuarios.arquivo[1]))
    print(usuarios.chave_cripto, " - ", usuarios.chave_criacao)
    valor = conversor_list(usuarios.arquivo[0])
    print(valor)

    #PERSONAGENS
    personagens = Criador_de_Blocos()
    personagens.criar()
    personagens.novo_bloco("Primeirosso")
    personagens.novo_bloco("O céu resplandece ao meu redor, ao meu redor, vou vuar e as estrelas")
    print(personagens.descriptar_bloco(personagens.arquivo[0]))
    print(personagens.descriptar_bloco(personagens.arquivo[1]))
    print(personagens.chave_cripto, " - ", personagens.chave_criacao)

    #CYBER ESPAÇOS
    espacos = Criador_de_Blocos()
    espacos.criar()
    espacos.novo_bloco("Primeirosso")
    espacos.novo_bloco("O céu resplandece ao meu redor, ao meu redor, vou vuar e as estrelas")
    print(espacos.descriptar_bloco(espacos.arquivo[0]))
    print(espacos.descriptar_bloco(espacos.arquivo[1]))
    print(espacos.chave_cripto, " - ", espacos.chave_criacao)

if __name__ == '__main__':
    principal()