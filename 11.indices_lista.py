"""
Exibir os indices da lista
"""

lista = ["Maria", "Helena", "Luiz"]

"""
i = 0

for nome in lista:
    print(i)
    i += 1
"""
i = range(len(lista))

for indice in i:
    print(indice, "--->", lista[indice])
    
