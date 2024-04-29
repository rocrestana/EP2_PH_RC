import time
from random import *

def cria_mapa(N):
    mapa = []
    for i in range(N):
        mapa.append([])
    for linha in mapa:
        for i in range (N):
            linha.append(' ')
    return mapa

def posicao_suporta(mapa, b, l, c, o):
    if l > len(mapa)-1 or c > len(mapa)-1:
        return False
    if o == 'h':
        if c + b > len(mapa):
            return False
        for i in range (c, c + b):
            if mapa[l][i] == 'N':
                return False

    if o == 'v':
        if l + b > len(mapa):
            return False
        for i in range (l, l+b):
            if mapa[i][c] == 'N':
                return False

    return True

def aloca_navios (mapa, blocos):
    import random
    n = len(mapa)
    if posicao_suporta(mapa, blocos, linha, coluna, orientacao) == True:
        if orientacao == 'h':
            for i in range (coluna, coluna + blocos):
                mapa[linha][i] = 'N'

        if orientacao == 'v':
            for i in range (linha, linha + blocos):
                mapa[i][coluna] = 'N'

    return mapa

def aloca_navios2 (mapa, blocos):
    import random
    n = len(mapa)
    for b in blocos:
        linha = random.randint(0, n-1)
        coluna = random.randint(0, n-1)
        orientacao = random.choice(['h', 'v'])
        
        while posicao_suporta(mapa, b, linha, coluna, orientacao) == False:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

        if orientacao == 'h':
            for i in range (coluna, coluna + b):
                mapa[linha][i] = 'N'

        if orientacao == 'v':
            for i in range (linha, linha + b):
                mapa[i][coluna] = 'N'

    return mapa

def foi_derrotado(m):
    for linha in m:
        for p in linha:
            if p == 'N':
                return False
    return True

import random
def tiro_computador(mapa):
    l = random.randint(0, 9)
    c = random.randint(0, 9)
    while mapa[l][c] == 'X' or mapa[l][c] == 'A':
        l = random.randint(0, 9)
        c = random.randint(0, 9)

    if mapa[l][c] == ' ':
        mapa[l][c] = 'A'

    if mapa[l][c] == 'N':
        mapa[l][c] = 'X'

    return mapa

def f(mapa):
    import copy
    lista = copy.deepcopy(mapa)
    for l, linha in enumerate (lista):
        for c, letra in enumerate (linha):
            if letra == 'N':
                lista[l][c] = (u"\u001b[42mN\u001b[0m")
            if letra == 'X':
                lista[l][c] = (u"\u001b[41mX\u001b[0m")
            if letra == 'A':
                lista[l][c] = (u"\u001b[44mA\u001b[0m")
            if letra == ' ':
                lista[l][c] = (u"\u001b[30m \u001b[0m") 
    print ('  A B C D E F G H I J ')
    for i in range (0, 10):
        print (i, lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], i)
    print ('  A B C D E F G H I J ')
    return ''



while True:
    mapa = cria_mapa(10)

    CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

    PAISES =  {
        'Brasil': {
            'cruzador': 1,
            'torpedeiro': 2,
            'destroyer': 1,
            'couracado': 1,
            'porta-avioes': 1
        }, 
        'França': {
            'cruzador': 3, 
            'porta-avioes': 1, 
            'destroyer': 1, 
            'submarino': 1, 
            'couracado': 1
        },
        'Austrália': {
            'couracado': 1,
            'cruzador': 3, 
            'submarino': 1,
            'porta-avioes': 1, 
            'torpedeiro': 1
        },
        'Rússia': {
            'cruzador': 1,
            'porta-avioes': 1,
            'couracado': 2,
            'destroyer': 1,
            'submarino': 1
        },
        'Japão': {
            'torpedeiro': 2,
            'cruzador': 1,
            'destroyer': 2,
            'couracado': 1,
            'submarino': 1
        }
    }

    # alfabeto para montar o nome das colunas
    ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # cores para o terminal
    CORES = {
        'reset': '\u001b[0m',
        'red': '\u001b[31m',
        'black': '\u001b[30m',
        'green': '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue': '\u001b[34m',
        'magenta': '\u001b[35m',
        'cyan': '\u001b[36m',
        'white': '\u001b[37m'
    }
    pais_computador = choice(list(PAISES.keys()))
    print(" =====================================")
    print("|                                     |")
    print("| Bem-vindo ao INSPER - Batalha Naval |")
    print("|                                     |")
    print(" =======   xxxxxxxxxxxxxxxxx   ======= \n")
    print('Iniciando o Jogo!')
    print(f'Computador está alocando os navios de guerra do país {pais_computador}...')
    print('Computador já está em posição de batalha!')

    col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}



    mapa_c = cria_mapa(10)
    lista_blocos = []
    for navio, qntd in PAISES[pais_computador].items():
        for i in range (qntd):
            lista_blocos.append(CONFIGURACAO[navio])
    mapa_c = aloca_navios2(mapa_c, lista_blocos)


    s = 1
    for k,v in PAISES.items():
        print(f'{s}: {k}')
        for navio,blocos in v.items():
            print(f'    {blocos} {navio}')
        s += 1

    while True:
        frota_jogador = int(input('Qual o número da nação da sua frota? '))
        if frota_jogador not in [1,2,3,4,5]:
            print('Opção inválida')
        else:
            pais_jogador = frota_jogador
            break
    i = 0
    for k , v in PAISES.items():
        i+=1
        if i == pais_jogador:
            print(f'Você escolheu a nação {k}')
            print("Agora é sua vez de alocar seus navios de guerra!")
            break

    for navios, qtd in PAISES[k].items():
        for i in range (qtd):
            f(mapa)
            print(f'Alocar: {navios} ({CONFIGURACAO[navios]} bloco(s))')
            c0 = input ('Informe a letra: ')
            c = c0.upper()
            coluna = col[c]
            linha = int(input('Informe a linha: '))
            orientacao = input('Informe a Orientação (v/h): ')

            while posicao_suporta(mapa, CONFIGURACAO[navios], linha, coluna, orientacao) == False:
                print('Posição inválida') 
                print(f'Alocar: {navios} ({CONFIGURACAO[navios]} bloco(s))')
                c0 = input ('Informe a letra: ')
                c = c0.upper()
                coluna = col[c]
                linha = int(input('Informe a linha: '))
                orientacao = input('Informe a Orientação (v/h): ') 

            mapa = aloca_navios(mapa, CONFIGURACAO[navios])

    time.sleep(2)

    print ('Seu mapa ficou assim:')
    f(mapa)

    time.sleep(1)

    mapa_cego = cria_mapa(10)
    print ("O mapa do território do oponente encontra-se abaixo. ")
    f(mapa_cego)

    time.sleep(3)


    while True:
        mapa = tiro_computador(mapa)
        print("Seu oponente jogou! Confira os danos no seu mapa e planeje o proximo ataque!")
        f(mapa)

        time.sleep(2.5)

        c0 = input('Qual é a coluna do seu tiro?(letra)')
        c = c0.upper()
        colunat = col[c]
        linhat = int(input('Qual é a linha do seu tiro?(número)'))

        while mapa_c[linhat][colunat] == 'X'  or mapa_c[linhat][colunat] == 'A':
            print ('Você já atirou aí, escolha outra posição')
            c0 = input('Qual é a coluna do seu tiro?(letra)')
            c = c0.upper()
            colunat = col[c]
            linhat = int(input('Qual é a linha do seu tiro?(número)'))

        time.sleep(1)
        if mapa_c[linhat][colunat] == 'N':
            mapa_c[linhat][colunat] = 'X'
            mapa_cego[linhat][colunat] = 'X'
            print('Acertou!')

        if mapa_c[linhat][colunat] == ' ':
            mapa_c[linhat][colunat] = 'A'
            mapa_cego[linhat][colunat] = 'A'
            print('Água!')
        time.sleep(1)
        
        f(mapa_cego)
        time.sleep(2)
        if foi_derrotado(mapa_c) == True:
            print ('Você ganhou!')
            break

        if foi_derrotado(mapa) == True:
            print ('Você perdeu...')
            break
    
    time.sleep(3)
    jogadnv = input("Quer jogar novamente? (s/n)")
    if jogadnv == 'n' or jogadnv == 'N':
        break 





    
