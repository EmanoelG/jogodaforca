
from tkinter import *

import sys
def menu():
    print('\033[31m-=\033[m'*18)
    print('\033[32m\tBem-vindo ao jogo da forca!')
    print()
    print('\033[31m-=\033[m'*18)
    while True:
        print("\033[32m{:.^40}\033[m".format("MENU"))
        menu = str(input("""
        \033[31mSair do Jogo [P]\033[m
        \033[33mRegras [R]\033[m
        \033[34mContinuar [c]\033[m
        """)).upper()
        if menu == 'P':
            sys.exit()
        elif menu == 'R':
            print("""\033[35m
        As regras são as seguintes ; dois jogador devem desputar , um jogador 
        escolhe  uma palvra e outro tenta adivinhar , letra por letra ou chuta a palavra inteiria
        somente letras de A à Z fazem parte, tem 6 tentativas para acertar a palavra 
        caso contrario o jogador que escolheu a palavra vence.
        \033[m""")
        elif menu == 'C':
            print('\033[36m\tESTÃO PREPARADOS?! BORA JOGAR ENTÃO !!!\033[m')
            break


def desenha_jogo(escolhe_palavra, palavra, erros=0, tamanho_palavra=0):
    


    if erros == 0:

        print()

        print(f'\t\t\t\033[31m6 VIDAS !\033[m')

        print("|----- ")

        print("|      ")

        print("|      ")

        print("|      ")

        print("|      ")

        print("|      ")
        # print("_,"*tamanho_palavra)

        
    if erros == 1:
        
        print()
        print(f'\t\t\t\033[31m5 VIDAS !\033[m')

        print("|----- ")

        print("|    | ")

        print("|      ")

        print("|      ")

        print("|      ")

        print("|      ")

        

        print()

        
    elif erros == 2:
        print()
        
        print(f'\t\t\t\033[31m4 VIDAS !\033[m')

        print("|----- ")

        print("|    | ")

        print("|    O ")
        

        print()

    elif erros == 3:

        print()
        
        print(f'\t\t\t\033[31m3 VIDAS !\033[m')

        print("|----- ")

        print("|    | ")

        print("|    O ")

        print("|   /|\ ")
        

        print()
    
    elif erros == 4:

        print()
        
        print(f'\t\t\t\033[31m2 VIDAS !\033[m')

        print("|----- ")

        print("|    | ")

        print("|    O ")

        print("|   /|\ ")

        print("|    | ")
        

        print()

    elif erros == 5:

        print()
        
        print(f'\t\t\t\033[31m1 VIDAS !\033[m')

        print("|----- ")

        print("|    | ")

        print("|    O ")

        print("|   /|\ ")

        print("|    | ")

        print("|   / \ ")
        

        print()


    elif erros == 6:
        print()
        
        print(f'\t\t\t\033[34mA palavra escolhido foi {palavra} !\033[m')
        print(f'\t\t\t\033[31m Jogador {escolhe_palavra} Venceu !\033[m')
        print(
        """ \033[35m 
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
        
        """
        )
         



    

# git remote add origin https://github.com/EmanoelG/jogodaforca.py.git
#  git push -u origin master