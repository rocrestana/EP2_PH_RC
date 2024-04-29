from random import *
def cria_mapa(N):
    mapa = []
    for i in range(N):
        mapa.append([])
    for linha in mapa:
        for i in range (N):
            linha.append(' ')
    return mapa

# lista = [['N', ' ', 'N', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# print ('  A B C D E F G H I J ')
# for i in range (0, 10):
#     print (i, lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4],  
#            lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], i)
# print ('  A B C D E F G H I J ')

(u" \u001b[42m N \u001b[0m")
print (u"\u001b[41m X \u001b[0m")
print (u" \u001b[44m   \u001b[0m")
def f(mapa):
    import copy
    lista = copy.deepcopy(mapa)
    for l, linha in enumerate (lista):
        for c, letra in enumerate (linha):
            if letra == 'N':
                lista[l][c] = (u"\u001b[42m   \u001b[0m")
            if letra == 'X':
                lista[l][c] = (u"\u001b[41m   \u001b[0m")
            if letra == 'A':
                lista[l][c] = (u"\u001b[44m   \u001b[0m")
            if letra == ' ':
                lista[l][c] = (u"\u001b[30m   \u001b[0m") 
    print ('   A   B   C   D   E   F   G   H   I   J ')
    for i in range (0, 10):
        print (i, lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], i)
        print (' ', end="\n\n")
    print ('  A   B   C   D   E   F   G   H   I   J ')
    return ''

mapa = [['N', ' ', 'N', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
f(mapa)





