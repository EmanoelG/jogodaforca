from comp_perguntas. valida import comeco , completou 
from comp_perguntas.perguntas import  input_definicao_palavra , input_letra , fim
from jogo import desenha_jogo , menu
import sys
from random import randint


############## JOGADORES 
jog_1= list()
jog_2= list()
jogador1= str(input('\033[33mJogador 1 Quer ser chamado como: ')).rstrip()  #1
if jogador1 == '':
    print('COMO USUARIO 1 NÃO INFORMOU NADA , VAI SER CHAMADO DE \033[36mGHOST\033[m')
    jogador1 = 'GHOST'
else:
    jogador1 = jogador1
jog_1=jogador1

jogador2=str(input('\033[33mJogador 2 Quer ser chamado como: ')).rstrip()  #2
if jogador2 == '':
    print('COMO USUARIO 2 NÃO INFORMOU NADA , VAI SER CHAMDO DE \033[31mPATO_DO_TRUCO\033[m') ## giria utilizada para quem perde demais ahahha... 
    jogador2 = 'PATO_DO_TRUCO'
else:
    jogador2 = jogador2    
jog_2=jogador2 



pontos_desafiado = 0
pontos_desafiador = 0
######################################################### JOGADORres QUE ESCOLHERA A : PALAVRA / letra

letra_usadas = dict()
letras_used = list()
while True:
    letra_usadas.clear()
    letras_used.clear()
    desafiado = '' # quem escolhe a palavra
    desafiador = '' #quem adivinha letra
    j1 = 1
    j2 = 2
    n= randint(j1,j2)
    if n == 1:
        desafiado = jogador1
        desafiador = jogador2
    else:
        desafiado = jogador2
        desafiador = jogador1
    
    
    if desafiado == jogador1:
        print(f'\t\t\t\033[35m Nome: {jogador1} Vs {jogador2}\033[m')
        print(f'\t\t\t\033[32m Pontos: {pontos_desafiado} x {pontos_desafiador}\033m')
    else:#desafiado == jogador2:
        print(f'\t\t\t\033[35m Nome: {jogador2} Vs {jogador1}\033[m')
        print(f'\t\t\t\t\033[32m Pontos: {pontos_desafiado} x {pontos_desafiador}\033m')

    palavra = input_definicao_palavra(desafiado, desafiador) #escolherá
    n=menu() ### MENU DE INFORMACAO 

######################################################### A FORCAAA 
    desenha_jogo(0, len(palavra))
    riscos = [" _ "] * len(palavra)
    errados = 0
    certo = 0 
    print(riscos)

############################################################################### JOGO , CHUTAR A PALAVRA , ERRO , ACERTO...

    while True:
        
        chutar = input("""\033[31mSe chutar a palavra e errar voce perde a partida... 
        Deseja chutar a palavra: [S/N]\033[m""").lower().strip()
        if chutar == 's':
            
            chut = str(input('\033[31mChute a palavra: \033[m')).lower().strip()
            if chut == palavra:
                print(f'\033[36m Paranbéns {desafiador} você acertou e venceu a partida !\033[m')
                pontos_desafiador += 1
                xxx=fim()
                jogar_mais = str(input('\033[36mJogar mais [S/N]: \033[m'))
                if jogar_mais == 's':
                    print()
                elif jogar_mais == 'n':
                    sys.exit()
            
            elif chut != palavra:
                print(f'\033[31mVoce errou a palavra (CORRETA : {palavra} ) e o jogador {desafiado} venceu !\033[m')
                pontos_desafiado += 1 
                xxx=fim()
                jogar_mais = str(input('\033[36mJogar mais [S/N]: \033[m'))
                if jogar_mais == 's':
                    print()
                elif jogar_mais == 'n':
                    sys.exit()
            break    

        elif not chutar in  'sn':     
            print('\033[32mSomente S/N !!! \033[m')
            
        elif chutar == 'n':
            print('\033[34mBora entao\033[m')
            pass
############################################################################################################################# VERIFICA AS LETRAS , SE GANHOU ACERTANDO AS LETRAS OU ERRANDO...
    
                        
        letra= input_letra(desafiador)#advinha
        letra_usadas['letra_usada']= letra
        letras_used.append(letra_usadas.copy())
        if letra in palavra:
            ce = palavra.find(letra)                         
            for i in range(ce, len(palavra)):
                if letra == palavra[i]:
                    riscos[i] = letra
                    certo += 1
        else:  

            errados += 1

        for letra in letras_used:
            print(letra.get("letra_usada"))
        desenha_jogo(desafiado,palavra,errados, len(palavra))
        if errados == 6:
            pontos_desafiado += 1
            jogar_mais = str(input('\033[36mJogar mais [S/N]: \033[m'))
            if jogar_mais == 's':
                print()
            elif jogar_mais == 'n':
                sys.exit()
            break
        print(riscos)
####################################### verifica pontos de cada jogador , e se vao jogar mais ou parar... 
        vencedor = 0
        completou(certo, palavra, desafiador)
        if certo == len(palavra):
            pontos_desafiador += 1
            jogar_mais = str(input('\033[36mJogar mais [S/N]: \033[m')).lower()
            if jogar_mais == 's':
                print()
            elif jogar_mais == 'n':
                sys.exit()
            break
        
        
 