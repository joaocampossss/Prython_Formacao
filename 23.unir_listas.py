# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abreviações = ['BA', 'SP', 'MG', 'RJ']

def agregação(c):
    nova_lista = []
    def interna(a):
        nova_lista = [(c, a)]
    return interna

for c in cidades:
    agregação(c)



