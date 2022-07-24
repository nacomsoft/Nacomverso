from Login import*
from Iniciar_Universo import*

inicio = Acesso()
inicio.menu_inicial()
if(inicio.sair_programa == False):
    dados = Personagem(inicio.usuario)
    dados.carregar_inicial(inicio.dados_personagem)
    aplicativo = Universo(inicio.usuario, inicio.dados_personagem)
    aplicativo.inicio()


