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


from random import*

class Identificador_de_Bloco:
    def __init__(self):
        self.inicio = True
        self.blocos_Criados = []
        self.complexidade = 4
        self.validador_inicial = "INICIO-"
        self.validador_fim = "-FIM"
        self.bloco_genesis = self.bloco_primitivo()
        self.tentativashacker = 0
        
    def setValidador(self, metodo):
        recevid = metodo.split("-")
        self.validador_inicial = recevid[0] + "-"
        self.validador_fim = "-" + recevid[1]
        self.bloco_genesis = self.bloco_primitivo()
        rato = [self.bloco_genesis]
        self.blocos_Criados = rato

    def termovalidador(self):
        termov = self.validador_inicial + "TERMO" + self.validador_fim
        return termov

    def verificador_de_validade(self, bloco):
        blocostr = bloco
        validador = blocostr.split("-")
        terv = self.termovalidador()
        componente = terv.split("-")
        carga = len(validador)
        bola = False
        if(carga > 1):
            dado_inicio = str(validador[0])
            inicio = str(componente[0])
            if(dado_inicio == inicio):
                dado_fim = str(validador[2])
                fim = str(componente[2])
                if(dado_fim == fim):
                    bola = True
                else:
                    bola = False
            else:
                bola = False
        else:
            bola = False
        return bola

    def separador(self, banco):
        x = 1
        y = len(banco)
        real = self.getBloco_Genesis()
        t = real
        w = 0
        bancoreal = []
        bancoreal = [real]
        while(x < y):
            t = banco[x]
            z = self.verificador_de_validade(t)
            if(z == True):
                bancor = [banco[x]]
                bancoreal += bancor
            else:
                w =+ 1
            x += 1
        self.tentativashacker += w
        print(bancoreal)
        return bancoreal

    def atulizar_real(self):
        self.blocos_Criados = self.separador(self.blocos_Criados)


    def getBloco_Genesis(self):
        return self.bloco_genesis

    
    def definidor_de_indice(self):
        x = 0
        codigo = self.criador_de_indice()
        resultado = "vazio"
        while(x <= 54):
            cadeiap = self.criador_de_indice()
            codigo[x] = self.sorteio_cadeia(cadeiap)
            if(x == 0):
                resultado = self.validador_inicial + str(codigo[x])
            else:
                resultado = resultado + str(codigo[x])
            x = x + 1
        resultado = resultado + self.validador_fim
        retornador = resultado
        return retornador

        

    def gerar_validador(self):
        
        inicio = self.codigo_pequeno()
        fim = self.codigo_pequeno()
        conjunto = inicio + "-" + fim
        self.setValidador(conjunto)
        return conjunto

    def codigo_pequeno(self):
        x = 0
        codigo = self.criador_de_indice()
        resultado = "vazio"
        while(x < 5):
            cadeiap = self.criador_de_indice()
            codigo[x] = self.sorteio_cadeia(cadeiap)
            if(x == 0):
                resultado = str(codigo[x])
            else:
                resultado = resultado + str(codigo[x])
            x = x + 1
        retornador = resultado
        return retornador

    def sorteio_cadeia(self, cadeia):
        indice = len(cadeia)
        valor = randint(0, (indice - 1))
        return cadeia[valor]

    def setComplexidade(self, dificuldade):
        self.complexidade = dificuldade

    def getBlocos_Criados(self):
        return self.blocos_Criados

    def bloco_primitivo(self):
        indice_primitivo = self.definidor_de_indice()
        return indice_primitivo

    def bloco_secundario(self):
        indice_bloco = self.definidor_de_indice()
        while(indice_bloco == self.bloco_genesis):
            indice_bloco = self.definidor_de_indice()
        indBC = self.indexBlocos_Criados()
        while(indBC == 0):
            while(indice_bloco == self.blocos_Criados[indBC]):
                indice_bloco = self.definidor_de_indice()
            indBC = indBC - 1
        rato2 = [indice_bloco]
        self.blocos_Criados += rato2
        return indice_bloco
    
    def indexBlocos_Criados(self):
        indice = len(self.blocos_Criados)
        return indice 

    def criador_de_indice(self):
        hexadecimal = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F"]
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        letras_maiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        simbolos = ["!", "@", "#", "$", "?","ç","§","£","¢","¥"]
        configurador = hexadecimal
        if(self.complexidade == 0):
            configurador = hexadecimal
        elif(self.complexidade == 1):
            configurador = numeros
        elif(self.complexidade == 2):
            configurador = numeros + letras_minusculas
        elif(self.complexidade == 3):
            configurador = numeros + letras_minusculas + letras_maiusculas
        elif(self.complexidade == 4):
            configurador = numeros + letras_minusculas + letras_maiusculas + simbolos
        else:
            configurador = hexadecimal
        return configurador

#x = identificador()
#rayo = x.gerar_validador()
#print(rayo)
#bola = x.bloco_primitivo()
#csas = x.getBloco_Genesis()
#dado = x.bloco_secundario()
#dado = x.bloco_secundario()
#dado = x.bloco_secundario()
#dado = x.bloco_secundario()
#print(x.getBlocos_Criados())