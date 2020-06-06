from  jogo import desenha_jogo
from random import randint
import sys

def input_cria_usuario():

    usuario = dict()

    usuario['nome'] = input('Informe o seu nome: ')

    usuario['pontos'] = 0

    usuario['desafiado'] = False

    return usuario




def comeco(j1, j2):
    j1 = 1
    j2 = 2
    n= randint(j1,j2)
    escolhildo = n 
    
    return escolhildo




            # mexi a aqui
def completou(acertos, pala , jogador_adivinhao):#recebe as letras acertadass e depois verifica se  a   palavra   esta completa
    if acertos == len(pala):## e aqui
        print(f'\t\t\t\t\t \033[37mJogador >> {jogador_adivinhao} << venceu !\033[m')
        print("""
        \033[35m 
         _____      ___       ___  ___   _______
        /  ___|    /   |     /   |/   | |   ____| 
        | |       /    |    / /|   /| | |  |__
        | |  _   /  /| |   / / |__/ | | |   __|
        | |_| | /  ___ |  / /       | | |  |____
        \_____//_/   |_| /_/        |_| |_______|
        
         _____    _     _   ______   ______
        /  _  \  | |   / / | _____| |  _    |
        | | | |  | |  / /  | |__    | |_|   |
        | | | |  | | / /   |  __|   |  _   /
        | |_| |  | |/ /    | |____  | | \  |
        \_____/  |___/     |______| |_|  \_|\033[m 
        
        """)
        



