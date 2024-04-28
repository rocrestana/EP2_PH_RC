
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

mapa = cria_mapa(10)

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

mapa_c = cria_mapa(10)
lista_blocos = []
for blocos in PAISES[pais_computador].values():
    lista_blocos.append(blocos)
mapa_c = aloca_navios2(mapa_c, lista_blocos)


soma = 1
for k,v in PAISES.items():
    print(f'{soma}: {k}')
    for k2,v2 in v.items():
        print(f'    {v2} {k2}')
    soma += 1

while True:
    input_jogador = int(input('Qual o número da nação da sua frota? '))
    if input_jogador not in [1,2,3,4,5]:
        print('Opção inválida')
    else:
        pais_jogador = input_jogador
        break
i = 0
for k , v in PAISES.items():
    i+=1
    if i == pais_jogador:
        print(f'Você escolheu a nação {k}')
        print("Agora é sua vez de alocar seus navios de guerra!")
        break

for navios, blocos in PAISES[k].items():
    print(mapa)
    print(f'Alocar: {navios} ({blocos} bloco(s))')
    coluna = int(input ('Informe a letra: '))
    linha = int(input('Informe a linha: '))
    orientacao = input('Informe a Orientação: ')

    while posicao_suporta(mapa, blocos, linha, coluna, orientacao) == False:
        print('Posição inválida') 
        print(f'Alocar: {navios} ({blocos} bloco(s))')
        coluna = int(input ('Informe a letra: '))
        linha = int(input('Informe a linha: '))
        orientacao = input('Informe a Orientação: ') 

    mapa = aloca_navios(mapa, blocos)

mapa_cego = cria_mapa()
print (mapa_cego)

while True:
    mapa = tiro_computador(mapa)
    print (mapa)

    colunat = input('Qual é a coluna do seu tiro?')
    linhat = int(input('Qual é a linha do seu tiro?'))

    while mapa_c[linhat][colunat] == 'X'  or mapa_c[linhat][colunat] == 'A':
        print ('Você já atirou aí, escolha outra posição')
        colunat = input('Qual é a coluna do seu tiro?')
        linhat = int(input('Qual é a linha do seu tiro?'))


    if mapa_c[linhat][colunat] == 'N':
        mapa_c[linhat][colunat] = 'X'
        mapa_cego[linhat][colunat] = 'X'
        print('Acertou!')

    if mapa_c[linhat][colunat] == '':
        mapa_c[linhat][colunat] = 'A'
        mapa_cego[linhat][colunat] = 'A'
        print('Água!')

    print (mapa_cego)

    if foi_derrotado(mapa) == True:
        print ('Você ganhou!')
        break
    if foi_derrotado(mapa_c) == True:
        print ('Você perdeu...')
        break



    
