import random 
from comp_perguntas.valida import comeco
from random import randint


def fim():
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
        
        """)




palavra_escolhida = ()
def input_definicao_palavra(jogador, jog2):
    palavras =['bode , vaca , boi' , 'galinha , coelho, tubarão , bode , vaca','dog , cat , cachorro ,ovelha , coelho ']
    x= random.choice(palavras)
    print(f"""\033[34m
    Jogador {jogador} foi o sorteado !!!
    informe a palava que deseja desafiar o seu adversário. 
    Jogador {jog2} feche os olhos enquanto ele escolhe a palavra!""")

    while True:

        palavra = input(f'Qual palavra deseja usar? (Ex...{x} , ').lower().rstrip()

        if palavra:
            palavra_escolhida = palavra


            break

    

    return palavra



def input_letra(jogador):
    # palavra_escolhida
    while True:

        letra = input(f'\033[33minforme uma letra: ')

        if len(letra) > 1:

            print('É apenas uma letra, seu apedeuta!')

        elif len(letra) < 1 : #valindando a letra(somente de A á Z!)

            print('Por favor, informe uma letra!\033[m')

        elif letra.isnumeric():

            print('Por favor, informe uma letra e não um número, seu apedeuta!')

        else:
    
            break


  
    return letra







