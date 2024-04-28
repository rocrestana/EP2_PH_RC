from random import *
def cria_mapa(N):
    mapa = []
    for i in range(N):
        mapa.append([])
    for linha in mapa:
        for i in range (N):
            linha.append(' ')
    return mapa