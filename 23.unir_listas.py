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


def cidade(c):
    def abreviação(a):
        novalista = (c, a)
        return novalista
    return abreviação

lista=[]

for c in cidades:
    teste = cidade(c)
    lista.append(teste(abreviações.pop(0)))

print(lista)