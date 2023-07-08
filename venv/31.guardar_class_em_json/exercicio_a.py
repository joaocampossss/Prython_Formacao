import json
CAMINHO = 'C:\\Users\\joaoa\\OneDrive - Rumos Consulting, S.A\\Ficheiros trabalho\\git\\Prython_Formacao\\Prython_Formacao-1\\venv\\31.guardar_class_em_json\\base_de_dados.json'


class Pessoas:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoas('João', 30)
p2 = Pessoas('Maria', 45)
p3 = Pessoas('Gabriel', 50)

# print(p1.__dict__)
lista = []
lista.append(p1.__dict__)
lista.append(p2.__dict__)
lista.append(p3.__dict__)
print(lista)

def fazer_dump():
    with open(CAMINHO, 'w+') as base_de_dados:
        json.dump(lista, base_de_dados)

if __name__ == '__main__':
    fazer_dump()