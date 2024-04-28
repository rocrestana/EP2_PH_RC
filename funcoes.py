from random import *
def cria_mapa(N):
    mapa = []
    for i in range(N):
        mapa.append([])
    for linha in mapa:
        for i in range (N):
            linha.append(' ')
    return mapa

#falta a segunda função



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
    l = random.choice(0, len(mapa)-1)
    c = random.choice(0, len(mapa)-1)
    while mapa[l][c] != 'X' and mapa[l][c] != 'A':
        l = random.choice(0, len(mapa)-1)
        c = random.choice(0, len(mapa)-1)

    if mapa[l][c] == '':
        mapa[l][c] = 'A'

    if mapa[l][c] == 'N':
        mapa[l][c] = 'X'

    return mapa
