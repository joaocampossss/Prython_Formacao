
import os
import json
import sys

tarefas = []
tarefas_refazer = []

base_de_dados = 'C:\\Users\\joaoa\\OneDrive - Rumos Consulting, S.A\\Ficheiros trabalho\\git\\Prython_Formacao\\Prython_Formacao-1\\venv\\28.base_de_dados.json'
with open(base_de_dados, 'r+') as cache:
    try:
        tarefas = json.load(cache)
    except json.decoder.JSONDecodeError:
        tarefas = []


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def resetar(tarefas):
    tarefas.clear()
    print()
    print(f'A lista tarefas foi resetada!\n')
    return tarefas

while True:
    print('Comandos: listar, desfazer, refazer, resetar, sair')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'cls': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'resetar': lambda: resetar(tarefas),
        'sair': lambda: sys.exit()
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    with open(base_de_dados, 'w+') as cache:
        json.dump(tarefas, cache)
