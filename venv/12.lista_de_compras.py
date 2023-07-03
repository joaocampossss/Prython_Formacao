"""
Faça uma lista de compras com listas
o utilizador deve ter a possibilidade de inserir, apagar e listar valores da sua lista
mão permita que o programa quebre com
erros de indices inexistentes na lista
"""
import os

lista_de_compras = []

while True:
    opção = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [5] Para Sair ").lower()
    
    os.system("cls")

    if opção == "i":
        produtos = input("Inserir um produto: ")
        lista_de_compras.append(produtos)
    
    elif opção == "l":
        for indice, produto in enumerate(lista_de_compras):
            print(indice, produto)
    
    elif opção == "a":
        produto_para_apagar = input("Indique o indice do produto a apagar: ")
        try:
            del lista_de_compras[int(produto_para_apagar)]
        except IndexError:
            print("O Indice inserido não é válido")
        except ValueError:
            print("O numero não é inteiro")
        except Exception:
            print("Erro Desconhecido")

    elif opção == "5":
        break
    else:
        print(f"{opção} não é uma opção válida!!")
#    print(lista_de_compras)