from random import *
def cria_mapa(N):
    mapa = []
    for i in range(N):
        mapa.append([])
    for linha in mapa:
        for i in range (N):
            linha.append(' ')
    return mapa

print (' A B C D E F G H I ')
for i in range (0, 10):
    print (i, ' '* 17, i)
print (' A B C D E F G H I ')


