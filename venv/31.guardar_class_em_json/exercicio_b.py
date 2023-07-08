from exercicio_a import CAMINHO, Pessoas, fazer_dump
import json
# CAMINHO = 'C:\\Users\\joaoa\\OneDrive - Rumos Consulting, S.A\\Ficheiros trabalho\\git\\Prython_Formacao\\Prython_Formacao-1\\venv\\31.guardar_class_em_json\\base_de_dados.json'

with open(CAMINHO, 'r+') as base_de_dados:
    lista = json.load(base_de_dados)

dict1, dict2, dict3 = lista

p1 = Pessoas(**dict1)
p2 = Pessoas(**dict2)
p3 = Pessoas(**dict3)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# Alternativa
# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     pessoas = json.load(arquivo)
#     p1 = Pessoa(**pessoas[0])
#     p2 = Pessoa(**pessoas[1])
#     p3 = Pessoa(**pessoas[2])

#     print(p1.nome, p1.idade)
#     print(p2.nome, p2.idade)
#     print(p3.nome, p3.idade)