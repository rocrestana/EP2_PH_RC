

def inverte_dicionario(dict):
    saida = {}
    for k, v in dict.items():
        saida[v] = k
    return saida

print (inverte_dicionario({0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}))