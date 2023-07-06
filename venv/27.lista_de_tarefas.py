# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

todo = []
todo_cache = []


def verificar_se_lista_esta_vazia(lista):
    return True if len(lista) == 0 else False


def listar_lista(lista):
    if verificar_se_lista_esta_vazia(lista):
        print('Sem Tarefas para Listar')
        return
    print()
    print('Tarefas')
    for tarefas in lista:
        print(tarefas)
    print()
    return


def desfazer_ultimo(lista, lista_cache):
    desfez = lista.pop()
    lista_cache.append(desfez)
    return lista, lista_cache


while True:
    comando_ou_tarefa = input(
        'Comandos: listar, desfazer, refazer, clear\nInsira uma tarefa ou comando (e para sair): ')
    if comando_ou_tarefa == 'e':
        break
    elif comando_ou_tarefa == 'listar':
        listar_lista(todo)
        continue
    elif comando_ou_tarefa == 'desfazer':
        desfazer_ultimo(todo, todo_cache)
    else:
        todo.append(comando_ou_tarefa)
    
    listar_lista(todo)

print(todo_cache)
